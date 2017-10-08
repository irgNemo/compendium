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

class Download_frame(Basic_frame):

	def __init__(self,informer,main_window):
		Basic_frame.__init__(self,main_window.get_window(),SEARCH_FRAME_SIZE,informer)
		self.main_window = main_window
		self.txt_mail = self.add_field("e-mail:",1,400,16,DEFAULT_TXTBOX_HEIGHT,TXTBOX_MAIL_WIGTH)
		self.txt_term = self.add_field("Term:",1,10,40,DEFAULT_TXTBOX_HEIGHT,TXTBOX_TERM_WIGTH)
		self.txt_filename = self.add_field("Filename:",1,10,70,DEFAULT_TXTBOX_HEIGHT,TXTBOX_FILENAME_WIGTH)
		self.txt_retmax = self.add_field("Retmax: ",1,400,70,DEFAULT_TXTBOX_HEIGHT,TXTBOX_RETMAX_WIGTH)
		self.cmb_database = self.add_chooser(DATABASES,"Database:",1,10,16)
		self.cmb_format = self.add_chooser(FORMATS,"Format: ",1,600,70)
		self.add_btn_search(780,100)

	def add_btn_search(self,pos_x,pos_y):
		btn_search = Button(self.get_top_panel(), text ="Search",command = self.run_btn_search)
		btn_search.pack()
		btn_search.place(x=pos_x,y=pos_y)

	def run_btn_search(self):
		thread = threading.Thread(target=self.btn_search_call_back)
		thread.start()

	def btn_search_call_back(self):
		db = self.cmb_database.get()
		mail = self.txt_mail.get("1.0","end-1c")
		if validate_mail(mail):
			main_folder = self.main_window.get_main_folder()
			if validate_not_none(main_folder):
				filename = self.txt_filename.get("1.0","end-1c")
				self.println(self.get_informer(),filename)
				if validate_not_none(filename):
					retmax = self.txt_retmax.get("1.0","end-1c")	
					if validate_is_number(retmax):
						format = self.cmb_format.get()
						term = self.txt_term.get("1.0","end-1c")
						filename_path = downloadSequences(self.main_window.get_main_informer()
,db, term, filename, format, mail, main_folder, retmax);	
						update_selected_file(self.main_window, filename_path)
						assing_job(self.main_window,filename_path)
						open_file(self.main_window,self.main_window.filter_frame.get_informer(),filename_path)
						self.get_frame().destroy()
					else:
						tkMessageBox.showerror("Error", ERROR_RETMAX)
				else:
					tkMessageBox.showerror("Error", ERROR_FILE_NAME)
			else:
				tkMessageBox.showerror("Error", ERROR_FOLDER_NAME)
		else:
			tkMessageBox.showerror("Error", ERROR_MAIL)

