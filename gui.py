from Tkinter import *
from ttk import *
from tkFileDialog import askopenfilename
from gui_constantes import *

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
		self.informer = self.insert_text_area()
		self.make_search_tab()

		self.window.mainloop()

	def insert_panel_opened_file(self):
		#Creando paneles
		top_panel = PanedWindow(height=50)
		top_panel.pack(fill=BOTH, expand=1)
		lbl_1 = Label(top_panel, text='Selected file: ')
		top_panel.add(lbl_1)
		lbl_1.place(x=10,y=16)
		lbl_selected_file = Label(top_panel, text=DEFAULT_SELECTED_FILE)
		top_panel.add(lbl_selected_file)
		lbl_selected_file.place(x=100,y=16)
		return lbl_selected_file

	def insert_menu(self):
		menubar = Menu(self.window)
		filemenu = Menu(menubar, tearoff=0)
		filemenu.add_command(label="Open", command=self.open_file)
		filemenu.add_command(label="Close")
		filemenu.add_separator()
		filemenu.add_command(label="Exit", command=self.window.quit)
		menubar.add_cascade(label="File", menu=filemenu)
		self.window.config(menu=menubar)

	def insert_notebooks(self):
		note = Notebook(padding=[LEFT_PADDING,TOP_PADDING,RIGHT_PADDING,BOTTOM_PADDING])
		tab_search = Frame(note, width=TABS_WIDTH, height=TABS_HEIGHT)
		tab_alignment = Frame(note, width=TABS_WIDTH, height=TABS_HEIGHT)
		tab_primers = Frame(note, width=TABS_WIDTH, height=TABS_HEIGHT)
		tab_blast = Frame(note, width=TABS_WIDTH, height=TABS_HEIGHT)
		tab_reports = Frame(note, width=TABS_WIDTH, height=TABS_HEIGHT)
		note.add(tab_search, text = "Search & download")
		note.add(tab_alignment, text = "Alignments")
		note.add(tab_primers, text = "Primers")
		note.add(tab_blast, text = "Blast")
		note.add(tab_reports, text = "Reports")
		note.pack(side = LEFT)
		return [tab_search,tab_alignment,tab_primers,tab_blast,tab_reports]

	def insert_text_area(self):
		text = Text(self.window,height=41,width=40)
		text.insert(INSERT, "Compendium Generator")
		text.pack()
		return text

	def open_file(self):
		selected_file = askopenfilename()
		self.update_selected_file(selected_file)

	def update_selected_file(self, string):
		self.lbl_selected_file.config(text=string)
		#self.lbl_selected_file.pack()

	def make_search_tab(self):
		print('hello')

my_gui = Gui()

