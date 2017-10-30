import threading
import tkMessageBox
from Tkinter import *
from ttk import *
from basic_tab import *
from gui_constans import *
from gui_utils import *
import sys
sys.path.append("../")
from src.utils import *;
from src.Petitions import *;
from src.Alignments import *;
from src.constans import *;

class Align_tab(Basic_tab):
	def __init__(self,tab,main_window):
		Basic_tab.__init__(self,tab,main_window,ALIGN_INFORMER_HEIGHT,ALIGN_INFORMERS_WIGTH)
		self.cmb_align_tool = self.add_chooser(ALIGNERS_OPTIONS,"Select an alignment tool:",2,200,10)
		self.add_btn_align(800,50)
		self.chkbox_align_seq = self.add_combobox("Align sequence",10,10)
		self.chkbox_philo_tree = self.add_combobox("Philo tree",10,30)
		self.chkbox_consensus_seq= self.add_combobox("Consensus sequence",10,50)
		self.txt_threshold = self.add_field("Threshold",1,200,50,DEFAULT_TXTBOX_HEIGHT,TXTBOX_THRESHOLD_WIGTH)

	def add_btn_align(self,pos_x,pos_y):
		btn_align = Button(self.get_top_panel(), text ="Align",command = self.run_btn_align)
		btn_align.pack()
		btn_align.place(x=pos_x,y=pos_y)

	def run_btn_align(self):
		thread = threading.Thread(target=self.btn_align_call_back)
		thread.start()

	def btn_align_call_back(self):
		filename_list = self.get_main_window().get_filename_list()
		if is_empty(filename_list):
			self.get_main_window().add_to_filename_list(get_selected_file(self.get_main_window()))
			
		for filename_item in filename_list:
			if get_extention(filename_item) == GENBANK_EXTENTION:
				file_data = parse(filename_item,GENBANK_FILE_TYPE)
				new_file_name = writeFile(file_data,get_basic_filename(filename_item),FASTA_EXTENSION)
				update_selected_file(self.get_main_window(), new_file_name)
				filename_item = new_file_name
				print "es gb"
			
			self.get_main_window().println("\n\n---Working with "+get_secction_name(filename_item)+"---")
			#self.get_main_window().get_main_informer().insert(INSERT,"\n\n---Working with "+get_secction_name(filename_item)+"---")
			update_selected_file(self.get_main_window(), filename_item)
			output_filename = get_basic_filename(filename_item)+ALINGING_EXTENSION
			self.disabled(self.txt_threshold)

			if self.chkbox_align_seq.get() == CHKBOX_ON :
				self.get_align(filename_item,output_filename)
				update_selected_file(self.get_main_window(), output_filename)
				open_file(self.get_main_window(),self.get_informer(),output_filename)
				if self.chkbox_philo_tree.get() == CHKBOX_ON:
					self.get_philo_tree(get_basic_filename(filename_item))
				if self.chkbox_consensus_seq.get() == CHKBOX_ON :
					consensus_filename = self.get_consensus(get_basic_filename(filename_item))
					if validate_not_none(consensus_filename):
						self.get_main_window().println("\nConsensus sequence was saved in "+ consensus_filename)
						#self.get_main_window().get_main_informer().insert(INSERT,"\nConsensus sequence was saved in "+ consensus_filename)
						update_selected_file(self.get_main_window(), consensus_filename)
						open_file(self.get_main_window(),self.get_informer(),consensus_filename)
						self.get_informer().see("insert")#Focus the informer's bottom
						self.get_main_window().enable_tab(INDEX_PRIMERS_TAB)
						self.get_main_window().focus_tab(INDEX_PRIMERS_TAB)
					else:
						self.get_main_window().println(ERROR_CONSENSUS)
						#self.get_main_window().get_main_informer().insert(INSERT,ERROR_CONSENSUS)"""
			self.enable(self.txt_threshold)
			#exp_arr = validate_selected_filename(consensus_filename)
			#self.get_main_window().assing_available_tabs(exp_arr[1],exp_arr[2])
				

	def get_align(self,filename,output_filename):
		try:
			if self.cmb_align_tool.get() == ALIGNERS_OPTIONS[INDEX_CLUSTALW]:
				self.get_main_window().println(CLUSTAL_ALING_MSJ)
				clustal_align(filename,get_clustalw_path());
			else:
				self.get_main_window().println(MUSCLE_ALING_MSJ)
				muscle_align(filename, output_filename)

			self.get_main_window().get_main_informer().insert(INSERT,"\nAlignment was finished")
			self.get_main_window().get_main_informer().insert(INSERT,"\nOutput file is "+output_filename)
	
		except:
			self.get_main_window().println("\nAligning Error!")

	def get_philo_tree(self,based_filename):
		try:
			self.get_main_window().println(PHILO_MSJ)
			#self.get_main_window().get_main_informer().insert(INSERT,"\n\nGetting phylo tree ...")
			aling_tree = get_tree(based_filename + PHILO_EXTENSION)
			tree_filename = based_filename + "_tree_" + IMAGE_EXTENSION
			self.get_main_window().println("\nSaving phylo tree in "+tree_filename)
			#self.get_main_window().get_main_informer().insert(INSERT,"\nSaving phylo tree in "+tree_filename)
			save_tree(tree_filename,aling_tree)
		except:
			self.get_main_window().println(ERROR_PHILO)
			#self.get_main_window().get_main_informer().insert(INSERT,ERROR_PHILO)

	def get_consensus(self,based_filename):
		try:
			self.get_main_window().println(ALIGN_DATA_MSJ)
			#self.get_main_window().get_main_informer().insert(INSERT,"\nGetting align data...")
			filename = based_filename + ALINGING_EXTENSION #Genero path aln
			alignment = get_align(filename, "clustal")
			self.get_main_window().println(CONSENSUS_MSJ)
			#self.get_main_window().get_main_informer().insert(INSERT,"\n\nGetting consensus sequence...")
			threshold = float(self.txt_threshold.get("1.0","end-1c"))
			consensus_seq = get_consensus(alignment,threshold)
			consensus_seq_record = SeqRecord(consensus_seq, id =based_filename, description = " Consensus sequence threshold=" + str(threshold))
			threshold_prefix = str(threshold).split('.')[1]
			#consensus_filename = based_filename +PREFIX_CONSENSUS+threshold_prefix+ "." + FASTA_EXTENSION
			self.get_main_window().println(SAVING_CONSENSUS_MSJ)
			#self.get_main_window().get_main_informer().insert(INSERT,"\nSaving consensus...")
			return writeFile(consensus_seq_record,based_filename +PREFIX_CONSENSUS+threshold_prefix, FASTA_EXTENSION)			 
		except:
			self.get_main_window().println(ERROR_CONSENSUS)
			#self.get_main_window().get_main_informer().insert(INSERT,ERROR_CONSENSUS)























