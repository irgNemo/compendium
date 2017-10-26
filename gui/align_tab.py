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
		self.add_btn_align(800,100)
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
		consensus_list = EMPTY_LIST
		if len(filename_list) != 0:
			for filename_item in filename_list:
				update_selected_file(self.get_main_window(), filename_item)
				output_filename = get_basic_filename(filename_item)+ALINGING_EXTENSION
				#self.clean_informer(self.get_informer())

				if self.chkbox_align_seq.get() == CHKBOX_ON :#and self.chkbox_consensus_seq.get() == CHKBOX_ON :
					self.get_align(filename_item,output_filename)
					update_selected_file(self.get_main_window(), output_filename)
					open_file(self.get_main_window(),self.get_informer(),output_filename)

				if self.chkbox_philo_tree.get() == CHKBOX_ON:
					self.get_philo_tree(get_basic_filename(filename_item))

				if self.chkbox_consensus_seq.get() == CHKBOX_ON :
					consensus_filename = self.get_consensus(get_basic_filename(filename_item))
					if validate_not_none(consensus_filename):
						consensus_list.append(consensus_filename)
						update_selected_file(self.get_main_window(), consensus_filename)
						open_file(self.get_main_window(),self.get_informer(),consensus_filename)
						self.get_informer().see("insert")
					else:
						self.get_main_window().get_main_informer().insert(INSERT,ERROR_CONSENSUS)
			self.get_main_window().clean_filename_list()		
			self.get_main_window().assign_to_filename_list(consensus_list)
			print self.get_main_window().get_filename_list()[0]
		else:
			print "No hay nada en la lista de archivos"

	def get_align(self,filename,output_filename):
		try:
			if self.cmb_align_tool.get() == ALIGNERS_OPTIONS[INDEX_CLUSTALW]:
				self.get_main_window().get_main_informer().insert(INSERT,"\nAligning with ClustalW...")
				clustal_align(filename,get_clustalw_path());
			else:
				self.get_main_window().get_main_informer().insert(INSERT,"\nAligning with Muscle...")
				muscle_align(filename, output_filename)
		except:
			self.get_main_window().get_main_informer().insert(INSERT,"\nAligning Error...")
		self.get_main_window().get_main_informer().insert(INSERT,"\nAlignment was finished")
		self.get_main_window().get_main_informer().insert(INSERT,"\nOutput file is "+output_filename)

	def get_philo_tree(self,based_filename):
		try:
			self.get_main_window().get_main_informer().insert(INSERT,"\nGetting phylo tree ...")
			aling_tree = get_tree(based_filename + PHILO_EXTENSION)
			tree_filename = based_filename + "_tree_" + IMAGE_EXTENSION
			self.get_main_window().get_main_informer().insert(INSERT,"\nSaving phylo tree in "+tree_filename)
			save_tree(tree_filename,aling_tree)
		except:
			self.get_main_window().get_main_informer().insert(INSERT,ERROR_PHILO)

	def get_consensus(self,based_filename):
		try:
			self.get_main_window().get_main_informer().insert(INSERT,"\nGetting align data...")
			filename = based_filename + ALINGING_EXTENSION
			alignment = get_align(filename, "clustal")
			self.get_main_window().get_main_informer().insert(INSERT,"\nGetting consensus sequence...")
			threshold = float(self.txt_threshold.get("1.0","end-1c"))
			consensus_seq = get_consensus(alignment,threshold)
			consensus_seq_record = SeqRecord(consensus_seq, id =based_filename, description = " Consensus sequence threshold=" + str(threshold))
			threshold_prefix = str(threshold).split('.')[1]
			consensus_filename = based_filename +PREFIX_CONSENSUS+threshold_prefix+ "." + FASTA_EXTENSION
			self.get_main_window().get_main_informer().insert(INSERT,"\nSaving consensus sequence in "+ consensus_filename)
			writeFile(consensus_seq_record,consensus_filename.split('.')[0], FASTA_EXTENSION)
			return consensus_filename
		except:
			self.get_main_window().get_main_informer().insert(INSERT,ERROR_CONSENSUS)























