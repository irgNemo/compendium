from Tkinter import *
from ttk import *
from tkFileDialog import askopenfilename
from gui_constans import *
from gui_utils import *
from search_tab import *
from align_tab import *
class Gui:
	
	def __init__(self):
		self.window = Tk()
		self.window.geometry(SIZE)
		self.window.title(TITLE)
		self.lbl_selected_file = self.insert_panel_opened_file()
		self.insert_menu()	
		tabs = self.insert_notebooks()
		self.tab_search = tabs[INDEX_SEARCH_TAB]
		self.tab_alignment = tabs[INDEX_ALIGNMENT_TAB]
		self.tab_primers = tabs[INDEX_PRIMERS_TAB]
		self.tab_blast = tabs[INDEX_BLAST_TAB]
		self.tab_reports = tabs[INDEX_REPORTS]
		self.insert_text_area()
		self.make_search_tab()
		self.make_alignment_tab()

		self.window.mainloop()

	def get_main_informer(self):
		return self.main_informer

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
		menubar = Menu(self.window)
		filemenu = Menu(menubar, tearoff=MENU_TEAROFF)
		filemenu.add_command(label="Open", command=self.select_file)
		filemenu.add_command(label="Close")
		filemenu.add_separator()
		filemenu.add_command(label="Exit", command=self.window.quit)
		menubar.add_cascade(label="File", menu=filemenu)
		self.window.config(menu=menubar)

	def insert_notebooks(self):
		self.note = Notebook(padding=[LEFT_PADDING,TOP_PADDING,RIGHT_PADDING,BOTTOM_PADDING])
		tab_search = Frame(self.note, width=TABS_WIDTH, height=TABS_HEIGHT)
		tab_alignment = Frame(self.note, width=TABS_WIDTH, height=TABS_HEIGHT)
		tab_primers = Frame(self.note, width=TABS_WIDTH, height=TABS_HEIGHT)
		tab_blast = Frame(self.note, width=TABS_WIDTH, height=TABS_HEIGHT)
		tab_reports = Frame(self.note, width=TABS_WIDTH, height=TABS_HEIGHT)
		self.note.add(tab_search, text = "Search & download")
		self.note.add(tab_alignment, text = "Alignments")
		self.note.add(tab_primers, text = "Primers")
		self.note.add(tab_blast, text = "Blast")
		self.note.add(tab_reports, text = "Reports")
		self.note.pack(side = LEFT)
		return [tab_search,tab_alignment,tab_primers,tab_blast,tab_reports]

	def insert_text_area(self):
		self.main_informer = Text(self.window, height=INFORMER_HEIGHT, width=INFORMER_WIGTH)
		scroll = Scrollbar(self.window,command=self.main_informer.yview)
		scroll.pack(side=RIGHT, fill=Y)
		self.main_informer.insert(INSERT, TITLE)
		self.main_informer.pack()
		scroll.config(command=self.main_informer.yview)

	def get_selected_tab_informer(self):
		current_tab = self.note.index("current")
		informers = { 0: self.search_frame.get_informer(), 1: 10, 2: 30 }
		return informers[current_tab]

	def select_file(self):
		selected_file = askopenfilename()
		update_selected_file(self,selected_file)
		open_file(self,self.get_selected_tab_informer(),self.lbl_selected_file['text'])

	def clean_informer(self,tab_informer):
		tab_informer.delete(1.0,END)

	def close_selected_file(self):
		update_selected_file(self, DEFAULT_SELECTED_FILE)

	"""def insert_informer(self,tab,height,width):
		text = Text(tab,height=height,width=width)	
		scroll = Scrollbar(tab,command=text.yview)
		scroll.pack(side=RIGHT, fill=Y)
		text.pack(side=RIGHT, fill=Y)
		scroll.config(command=text.yview)
		text.config(yscrollcommand=scroll.set)
		return text

	def add_top_panel(self,tab):
		top_panel = PanedWindow(tab, height=TOP_PANEL_SEARCH_TAB_HEIGHT)
		top_panel.pack(fill=BOTH, expand=PANELS_EXPAND)
		return top_panel"""

	def make_search_tab(self):
		self.search_frame = Search_tab(self.tab_search,self)

	def make_alignment_tab(self):
		self.align_frame = Align_tab(self.tab_alignment)		
		self.align_frame.adios()	

















my_gui = Gui()

