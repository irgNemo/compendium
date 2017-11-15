import threading
from Tkinter import *
import tkMessageBox
from ttk import *
from basic_frame import *
from gui_constans import *
from gui_utils import *
from validations import *
import sys
sys.path.append("../")
from src.utils import *;
from src.Petitions import *;
from src.constans import *;
from src.IO import *

class Reports_frame(Basic_frame):

	def __init__(self,informer,main_window):
		Basic_frame.__init__(self,main_window.get_window(),REPORTS_FRAME_SIZE,informer)
		self.main_window = main_window
		panel = self.get_top_panel()
		lbl_1 = Label(panel, text="Select the items you want to apeer in the report")
		panel.add(lbl_1)
		lbl_1.place(x=10,y=10)
		pos_x = 10
		self.algnment_checkbox = self.add_combobox("Alignment",pos_x,30)
		self.philo_checkbox = self.add_combobox("Philo tree",pos_x,50)
		self.consensus_checkbox = self.add_combobox("Consensus sequence",pos_x,70)
		self.primer_checkbox = self.add_combobox("Primers",pos_x,90)
		self.blast_checkbox = self.add_combobox("Blast results",pos_x,110)
		self.add_btn_reports(250,100)

	def add_btn_reports(self,pos_x,pos_y):
		btn_reports = Button(self.get_top_panel(), text ="reports",command = self.run_btn_reports)
		btn_reports.pack()
		btn_reports.place(x=pos_x,y=pos_y)

	def run_btn_reports(self):
		thread = threading.Thread(target=self.btn_reports_call_back)
		thread.start()

	def btn_reports_call_back(self):
		item = 0
		primers_list = self.main_window.get_primers_id_list()
		consensus_list = self.main_window.get_consensus_list()
		filename_list = self.main_window.get_filename_list()

		for item in range(len(filename_list)):
			current_section = get_secction_name(filename_list[item])
			if self.algnment_checkbox.get() == CHKBOX_ON:
				if exists(filename_list[item]):
					alignment = get_align(get_basic_filename(filename_list[item])+ALINGING_EXTENSION,"clustal")
					data = alignment.format("clustal")
				else:
					data = ""
					tkMessageBox.showinfo("Information", ERROR_NO_FILE+"Alignment")
			else:
				data = ""

			if self.philo_checkbox.get() == CHKBOX_ON:
				my_tree_file = get_basic_filename(filename_list[item]) + PREFIX_PHILO + IMAGE_EXTENSION
				if exists(my_tree_file):
					tree_filename = my_tree_file
				else:
					tree_filename = ""
					tkMessageBox.showinfo("Information", ERROR_NO_FILE+"Philo tree")
			else:
				tree_filename = ""

			if self.consensus_checkbox.get() == CHKBOX_ON:
				consensus_file = consensus_list[item]
				if exists(consensus_file):
					consensus_data = get_file_data(consensus_file)
				else:
					consensus_data = ""
					tkMessageBox.showinfo("Information", ERROR_NO_FILE+"Consensus")
			else:
				consensus_data = ""

			if self.primer_checkbox.get() == CHKBOX_ON:
				for item in primers_list:
					if current_section in item:
						primers_file = item+".all"
						if exists(primers_file):
							primers_data = get_file_data(primers_file)
			else:
				primers_data = ""
				
			if self.blast_checkbox.get() == CHKBOX_ON:
				for item in primers_list:
					if current_section in item:
						primers_file = item+"blast"
						if exists(primers_file):
							blast_data = get_file_data(primers_file)
			else:
				blast_data = ""

			generate_report(data,consensus_data,tree_filename,primers_data,blast_data,item+".pdf")





















