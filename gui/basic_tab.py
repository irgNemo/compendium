from Tkinter import *
from ttk import *
from gui_constans import *

class Basic_tab:

	def __init__(self,tab,height=DEFAULT_TAB_INFORMERS_HEIGHT,width=DEFAULT_TAB_INFORMERS_WIGTH):
		self.tab = tab
		self.add_top_panel(tab)
		self.insert_informer(tab,height,width)

	def insert_informer(self,tab,height,width):
		self.informer = Text(tab,height=height,width=width)	
		scroll = Scrollbar(tab,command=self.informer.yview)
		scroll.pack(side=RIGHT, fill=Y)
		self.informer.pack(side=RIGHT, fill=Y)
		scroll.config(command=self.informer.yview)
		self.informer.config(yscrollcommand=scroll.set)

	def add_top_panel(self,tab,panel_height=TOP_PANEL_TAB_HEIGHT):
		self.top_panel = PanedWindow(tab, height=panel_height)
		self.top_panel.pack(fill=BOTH,expand=PANELS_EXPAND)

	def add_separator(self,widget,pos_x,pos_y,sep_orient):
		separator = Separator(widget, orient='horizontal').pack(fill=X,pady=140)
		
	def clean_informer(self,tab_informer):
		self.informer.delete(1.0,END)

	def println(self,informer,msj):
		informer.insert(INSERT,'\n'+msj)

	def get_informer(self):
		return self.informer

	def get_top_panel(self):
		return self.top_panel

	def get_tab(self):
		return self.tab
