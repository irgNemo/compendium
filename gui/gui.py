from Tkinter import *
from ttk import *
import tkFileDialog
#from tkFileDialog import askopenfilename,filedialog
from gui_constans import *
from validations import *
from gui_utils import *
from download_frame import *
from filter_tab import *
from align_tab import *

class Gui:
	
	def __init__(self):
		self.window = Tk()
		self.window.geometry(SIZE)
		self.window.title(TITLE)
		self.lbl_selected_file = self.insert_panel_opened_file()
		self.insert_menu()	
		tabs = self.insert_notebooks()
		self.tab_filter = tabs[INDEX_FILTER_TAB]
		self.tab_alignment = tabs[INDEX_ALIGNMENT_TAB]
		self.tab_primers = tabs[INDEX_PRIMERS_TAB]
		self.tab_blast = tabs[INDEX_BLAST_TAB]
		self.tab_reports = tabs[INDEX_REPORTS]
		self.insert_text_area()
		self.make_Filter_tab()
		self.make_alignment_tab()
		self.load_settings()
		self.disable_all_tabs()
		self.window.mainloop()

	def get_main_informer(self):
		return self.main_informer

	def get_main_folder(self):
		return self.main_folder

	def get_window(self):
		return self.window		

	def insert_panel_opened_file(self):
		#Creando paneles
		top_panel = PanedWindow(height=TOP_PANEL_MAINWINDOW_HEIGHT)
		top_panel.pack(fill=BOTH, expand=PANELS_EXPAND)
		lbl_1 = Label(top_panel, text='Selected file: ')
		top_panel.add(lbl_1)
		lbl_1.place(x=10,y=16)
		lbl_selected_file = Label(top_panel, text=DEFAULT_SELECTED_FILE)
		top_panel.add(lbl_selected_file)
		lbl_selected_file.place(x=LBL_SELECTED_FILE_X,y=LBL_SELECTED_FILE_Y)
		return lbl_selected_file

	def insert_menu(self):
		self.menubar = Menu(self.window)
		#sequence menu
		sequences_menu = Menu(self.menubar, tearoff=0)
		sequences_menu.add_command(label="Load from computer", command=self.select_file)
		sequences_menu.add_command(label="Search and download", command=self.make_download_frame)
		sequences_menu.add_command(label="Close")
		sequences_menu.add_separator()
		sequences_menu.add_command(label="Exit", command=self.window.quit)
		self.menubar.add_cascade(label="Sequences", menu=sequences_menu,state="disabled")
		#Settings menu
		self.automatic_setting = BooleanVar()
		self.default_setting = BooleanVar()
		settings_menu = Menu(self.menubar, tearoff=0)
		settings_menu.add_command(label="Set main folder", command=self.setting_main_folder)
		settings_menu.add_checkbutton(label="Automatic", onvalue=True, offvalue=False, variable=self.automatic_setting, command=self.setting_automatic)
		settings_menu.add_checkbutton(label="Default", onvalue=True, offvalue=False, variable=self.default_setting, command=self.setting_default)
		self.menubar.add_cascade(label="Settings", menu=settings_menu)	
		#Run menu
		self.menubar.add_command(label="Run", command=self.setting_main_folder)	

		self.window.config(menu=self.menubar)

	def insert_notebooks(self):
		self.note = Notebook(padding=[LEFT_PADDING,TOP_PADDING,RIGHT_PADDING,BOTTOM_PADDING])
		tab_filter = Frame(self.note, width=TABS_WIDTH, height=TABS_HEIGHT)
		tab_alignment = Frame(self.note, width=TABS_WIDTH, height=TABS_HEIGHT)
		tab_primers = Frame(self.note, width=TABS_WIDTH, height=TABS_HEIGHT)
		tab_blast = Frame(self.note, width=TABS_WIDTH, height=TABS_HEIGHT)
		tab_reports = Frame(self.note, width=TABS_WIDTH, height=TABS_HEIGHT)
		self.note.add(tab_filter, text = "Filtering")
		self.note.add(tab_alignment, text = "Alignments")
		self.note.add(tab_primers, text = "Primers")
		self.note.add(tab_blast, text = "Blast")
		self.note.add(tab_reports, text = "Reports")
		self.note.pack(side = LEFT,expand=True, fill=BOTH)
		return [tab_filter,tab_alignment,tab_primers,tab_blast,tab_reports]

	def insert_text_area(self):
		self.main_informer = Text(self.window, height=INFORMER_HEIGHT, width=INFORMER_WIGTH)
		scroll = Scrollbar(self.window,command=self.main_informer.yview)
		scroll.pack(side=RIGHT, fill=Y)
		self.main_informer.insert(INSERT, TITLE)
		self.main_informer.pack(expand=True, fill=BOTH)
		scroll.config(command=self.main_informer.yview)

	def get_selected_tab_informer(self):
		current_tab = self.note.index("current")
		informers = { 0: self.filter_frame.get_informer(), 1: self.align_frame.get_informer(), 2: 30 }
		return informers[current_tab]

	def select_file(self):
		selected_file = tkFileDialog.askopenfilename()
		update_selected_file(self,selected_file)
		selected_file= self.lbl_selected_file['text']
		if  selected_file != DEFAULT_SELECTED_FILE and validate_not_none(selected_file):
			assing_job(self,selected_file)
			open_file(self,self.get_selected_tab_informer(),selected_file)
		else:
			update_selected_file(self, DEFAULT_SELECTED_FILE)
			self.clean_informer(self.get_informer())
			self.disable_all_tabs()
			tkMessageBox.showwarning("Warning", SELECTED_FILE_WARNING)		

	def clean_informer(self,tab_informer):
		tab_informer.delete(1.0,END)

	def close_selected_file(self):
		update_selected_file(self, DEFAULT_SELECTED_FILE)

	def assing_available_tabs(self,filename,file_extention):
		if file_extention == "gb":
			self.enable_tab(INDEX_FILTER_TAB)
			self.enable_tab(INDEX_ALIGNMENT_TAB)
			self.focus_tab(INDEX_FILTER_TAB)
			self.filter_frame.set_filename(filename)
		if file_extention == "fasta":
			self.enable_tab(INDEX_ALIGNMENT_TAB)
			self.focus_tab(INDEX_ALIGNMENT_TAB)
		if file_extention == "aln":
			self.enable_tab(INDEX_PRIMERS_TAB)
			self.enable_tab(INDEX_ALIGNMENT_TAB)
			self.focus_tab(INDEX_ALIGNMENT_TAB)

	def make_download_frame(self):
		self.download_frame = Download_frame(self.download_informer,self)

	def make_Filter_tab(self):
		self.filter_frame = Filter_tab(self.tab_filter,self)
		self.download_informer = self.filter_frame.get_informer()		

	def make_alignment_tab(self):
		self.align_frame = Align_tab(self.tab_alignment,self)

	def make_primers_tab(self):
		self.primers_frame = Primers_tab(self.tab_primers,self)		

	def setting_main_folder(self):
		create_new_main_folder(self)
		self.main_folder = set_main_folder(self)

	def setting_automatic(self):
		if self.automatic_setting.get():
			print("Automatic")
		else:
			print("NO Automatic")

	def setting_default(self):
		if self.automatic_setting.get():
			print("Default")
		else:
			print("NO Default")
		

	def disable_all_tabs(self):
		for index in range(INDEX_FILTER_TAB, INDEX_REPORTS+1):
			self.disable_tab(index)

	def focus_tab(self,tab_index):
		self.note.select(tab_index)
	
	def enable_tab(self,tab_index):
		self.note.tab(tab_index, state="normal")		

	def disable_tab(self,tab_index):
		self.note.tab(tab_index, state="disabled")

	def load_settings(self):
		self.main_folder = set_main_folder(self)
		if validate_not_none(self.main_folder):
			self.menubar.entryconfig("Sequences",state="normal")
			self.setting_automatic()
			self.setting_default()
			self.print_settings()
		else:
			tkMessageBox.showerror("Error", ERROR_SETTINGS)
	
	def print_settings(self):
		self.get_main_informer().insert(INSERT,FOLDER_SETTINGS_MSJ + self.main_folder + NEW_LINE)
		self.get_main_informer().insert(INSERT,AUTOMATIC_SETTINGS_MSJ + str(self.automatic_setting.get()) + NEW_LINE)
		self.get_main_informer().insert(INSERT,DEFAULT_SETTINGS_MSJ + str(self.default_setting.get()) + NEW_LINE)

my_gui = Gui()

