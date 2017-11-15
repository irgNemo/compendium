import threading
from Tkinter import *
import tkMessageBox
from ttk import *
from basic_frame import *
from gui_constans import *
from gui_utils import *
from validations import *
import subprocess 
import os
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

	def open_report(self,filename):
		#subprocess.call(['evince ',filename])	
		#command = "'evince "+filename+ "'" 
		thread = threading.Thread(target=subprocess.call("evince " + filename, shell=True))
		thread.start() 

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
			self.main_window.println("\n\n---Working with "+ current_section)
			if self.algnment_checkbox.get() == CHKBOX_ON:
				self.main_window.println("\nReading Alignment data...")
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
				self.main_window.println("\nReading philo tree data...")
				if exists(my_tree_file):
					tree_filename = my_tree_file
				else:
					tree_filename = ""
					tkMessageBox.showinfo("Information", ERROR_NO_FILE+"Philo tree")
			else:
				tree_filename = ""

			if self.consensus_checkbox.get() == CHKBOX_ON:
				consensus_file = consensus_list[item]
				self.main_window.println("\nReading Consensus Sequence data...")
				if exists(consensus_file):
					consensus_data = get_file_data(consensus_file)
				else:
					consensus_data = ""
					tkMessageBox.showinfo("\nInformation", ERROR_NO_FILE+"Consensus")
			else:
				consensus_data = ""

			if self.primer_checkbox.get() == CHKBOX_ON:
				self.main_window.println("\nReading Primers data...")
				for primer in primers_list:
					if current_section in primer:
						primers_file = primer+".all"
						if exists(primers_file):
							primers_data = get_file_data(primers_file)
						else:
							self.main_window.println(ERROR_NO_FILE + primers_file)
			else:
				primers_data = ""
				
			if self.blast_checkbox.get() == CHKBOX_ON:
				self.main_window.println("\nReading Blast data...")
				for primer in primers_list:
					print current_section
					print primer
					if current_section in primer:
						blast_file = primer+"blast"
						print blast_file
						if exists(blast_file):
							blast_data = get_file_data(blast_file)
						else:
							self.main_window.println(ERROR_NO_FILE + blast_file)
			else:
				blast_data = ""
			
			pdf_filename = get_basic_filename(filename_list[item]) +".pdf"
			self.main_window.println("\n\nGenerating report...")
			generate_report(data,consensus_data,tree_filename,primers_data,blast_data,pdf_filename)
			self.main_window.println("\nThe report was saved in "+ pdf_filename)
			self.get_frame().destroy()
			self.open_report(pdf_filename)			



















