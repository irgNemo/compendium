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
		self.add_mail_field(400,16,DEFAULT_TXTBOX_HEIGHT,TXTBOX_MAIL_WIGTH)
		self.add_term_field(10,40,DEFAULT_TXTBOX_HEIGHT,TXTBOX_TERM_WIGTH)
		self.add_filename_field(10,70,DEFAULT_TXTBOX_HEIGHT,TXTBOX_FILENAME_WIGTH)
		self.add_retmax_field(400,70,DEFAULT_TXTBOX_HEIGHT,TXTBOX_RETMAX_WIGTH)
		self.add_db_chooser(10,16)
		self.add_format_chooser(600,70)
		self.add_btn_search(780,100)

	def add_mail_field(self,pos_x,pos_y,field_height,field_width):
		panel = self.get_top_panel()
		lbl_1 = Label(panel, text='e-mail: ')
		panel.add(lbl_1)
		lbl_1.place(x=pos_x,y=pos_y)
		self.txt_mail = Text(self.get_frame(),height=field_height,width=field_width)	
		self.txt_mail.insert(INSERT, DEFAULT_MAIL)
		self.txt_mail.pack()
		self.txt_mail.place(x=pos_x+BLANK_SPACE_X,y=pos_y)

	def add_term_field(self,pos_x,pos_y,field_height,field_width):
		panel = self.get_top_panel()
		lbl_1 = Label(panel, text='Term: ')
		panel.add(lbl_1)
		lbl_1.place(x=pos_x,y=pos_y)
		self.txt_term = Text(self.get_frame(),height=field_height,width=field_width)	
		self.txt_term.insert(INSERT, DEFAULT_TERM)
		self.txt_term.pack()
		self.txt_term.place(x=pos_x+BLANK_SPACE_X,y=pos_y)

	def add_retmax_field(self,pos_x,pos_y,field_height,field_width):
		panel = self.get_top_panel()
		lbl_1 = Label(panel, text='Retmax: ')
		panel.add(lbl_1)
		lbl_1.place(x=pos_x,y=pos_y)
		self.txt_retmax = Text(self.get_frame(),height=field_height,width=field_width)	
		self.txt_retmax.insert(INSERT, DEFAULT_RETMAX)
		self.txt_retmax.pack()
		self.txt_retmax.place(x=pos_x+BLANK_SPACE_X,y=pos_y)

	def add_filename_field(self,pos_x,pos_y,field_height,field_width):
		panel = self.get_top_panel()
		lbl_1 = Label(panel, text='Filename: ')
		panel.add(lbl_1)
		lbl_1.place(x=pos_x,y=pos_y)
		self.txt_filename = Text(self.get_frame(),height=field_height,width=field_width)
		self.txt_filename.pack()
		self.txt_filename.place(x=pos_x+BLANK_SPACE_X,y=pos_y)
	
	def add_db_chooser(self,pos_x,pos_y):
		panel = self.get_top_panel()
		lbl_1 = Label(panel, text='Database: ')
		panel.add(lbl_1)
		lbl_1.place(x=pos_x,y=pos_y)
		self.cmb_database = Combobox(self.get_frame(),values=DATABASES,state='readonly')
		self.cmb_database.current(0)
		self.cmb_database.pack();
		self.cmb_database.place(x=pos_x+BLANK_SPACE_X,y=pos_y)

	def add_format_chooser(self,pos_x,pos_y):
		panel = self.get_top_panel()
		lbl_1 = Label(panel, text='Format: ')
		panel.add(lbl_1)
		lbl_1.place(x=pos_x,y=pos_y)
		self.cmb_format = Combobox(self.get_frame(),values=FORMATS,state='readonly')
		self.cmb_format.current(0)
		self.cmb_format.pack();
		self.cmb_format.place(x=pos_x+BLANK_SPACE_X,y=pos_y)

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
						open_file(self.main_window,self.get_informer(),filename_path)
					else:
						tkMessageBox.showerror("Error", ERROR_RETMAX)
				else:
					tkMessageBox.showerror("Error", ERROR_FILE_NAME)
			else:
				tkMessageBox.showerror("Error", ERROR_FOLDER_NAME)
		else:
			tkMessageBox.showerror("Error", ERROR_MAIL)

