from Tkinter import *
from ttk import *
from gui_constans import *

class Basic_frame:

	def __init__(self,main_window,size,informer):
		self.frame = Toplevel(main_window)
		self.frame.geometry(size)
		self.informer = informer
		self.add_top_panel(self.frame)

	def add_top_panel(self,frame):
		self.top_panel = PanedWindow(self.frame, height=TOP_PANEL_SEARCH_FRAME_HEIGHT)
		self.top_panel.pack(fill=BOTH, expand=PANELS_EXPAND)
		
	def clean_informer(self,informer):
		informer.delete(1.0,END)

	def println(self,informer,msj):
		informer.insert(INSERT,'\n'+msj)

	def get_informer(self):
		return self.informer

	def get_top_panel(self):
		return self.top_panel

	def get_frame(self):
		return self.frame
