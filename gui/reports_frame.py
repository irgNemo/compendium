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
		self.add_combobox("Alignment",pos_x,30)
		self.add_combobox("Philo tree",pos_x,50)
		self.add_combobox("Consensus sequence",pos_x,70)
		self.add_combobox("Primers",pos_x,90)
		self.add_combobox("Blast results",pos_x,110)
		self.add_btn_reports(250,100)

	def add_btn_reports(self,pos_x,pos_y):
		btn_reports = Button(self.get_top_panel(), text ="reports",command = self.run_btn_reports)
		btn_reports.pack()
		btn_reports.place(x=pos_x,y=pos_y)

	def run_btn_reports(self):
		thread = threading.Thread(target=self.btn_reports_call_back)
		thread.start()

	def btn_reports_call_back(self):

		#filename_list = self.main_window.get_filename_list()
		print "Generating report"
		generate_report("holaalignment dali","me llamo","","Karla"," y tu ","dali_avila_cardenas")
		print "Finish report"

