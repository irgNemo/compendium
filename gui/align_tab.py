import threading
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
		self.threshold_field = self.add_field("Threshold",1,200,50,DEFAULT_TXTBOX_HEIGHT,TXTBOX_THRESHOLD_WIGTH)

	"""def add_clustal_panel(self,panel_height=CLUSTAL_PANEL_HEIGHT):
		self.clustal_panel = PanedWindow(self.get_top_panel(), height=panel_height)
		self.clustal_panel.pack(fill=Y)#,expand=PANELS_EXPAND
		label = Label(self.clustal_panel, text="hola")
		self.clustal_panel.add(label)
		self.clustal_panel.proxy_place(10, 20)"""

	def add_btn_align(self,pos_x,pos_y):
		btn_filter = Button(self.get_top_panel(), text ="Align",command = self.run_btn_align)
		btn_filter.pack()
		btn_filter.place(x=pos_x,y=pos_y)

	def run_btn_align(self):
		thread = threading.Thread(target=self.btn_align_call_back)
		thread.start()

	def btn_align_call_back(self):
		filename = get_selected_file(self.main_window)
		output_filename = get_basic_filename(filename)+ALINGING_EXTENSION

		if self.chkbox_align_seq.get() == CHKBOX_ON:
			self.get_align(filename,output_filename)

		if self.chkbox_philo_tree.get() == CHKBOX_ON:
			self.get_philo_tree(get_basic_filename(filename))

		if self.chkbox_consensus_seq.get() == CHKBOX_ON:
			self.get_consensus(get_basic_filename(filename))

		self.clean_informer(self.get_informer())
		open_file(self.get_main_window(),self.get_informer(),output_filename)

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

	def get_philo_tree(self,based_filename):
		try:
			self.get_main_window().get_main_informer().insert(INSERT,"\nGetting phylo tree ...")
			aling_tree = get_tree(based_filename + PHILO_EXTENSION)
			tree_filename = based_filename + "_tree_" + IMAGE_EXTENSION
			self.get_main_window().get_main_informer().insert(INSERT,"\nSaving phylo tree in "+tree_filename)
			save_tree(tree_filename,aling_tree)
		except:
			self.get_main_window().get_main_informer().insert(INSERT,"\nPhilo tree Error")
		self.get_main_window().get_main_informer().insert(INSERT,"\nAlignment was finished")
		self.get_main_window().get_main_informer().insert(INSERT,"\nOutput file is "+output_filename)

	def get_consensus(self,based_filename):
		self.get_main_window().get_main_informer().insert(INSERT,"\nGetting align data...")
		alignment = get_align(based_filename + ALINGING_EXTENSION, "clustal")
		self.get_main_window().get_main_informer().insert(INSERT,"\nGetting consensus sequence...")
		consensus_seq_record = SeqRecord(get_consensus(alignment,threshold), id = term + " " +key, description = " Consensus sequence ")
		self.get_main_window().get_main_informer().insert(INSERT,"\nSaving consensus sequence...")
		writeFile(consensus_seq_record,based_filename + "_consensus_" , FASTA_EXTENSION)
























