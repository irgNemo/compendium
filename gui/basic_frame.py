from Tkinter import *
from ttk import *
from gui_constans import *

class Basic_frame:

	def __init__(self,main_window,size,informer):
		self.frame = Toplevel(main_window)
		self.frame.geometry(size)
		self.informer = informer
		self.add_top_panel(self.frame)

	def add_field(self,field_label,spaces,pos_x,pos_y,field_height,field_width):
		panel = self.get_top_panel()
		lbl_1 = Label(panel, text=field_label)
		panel.add(lbl_1)
		lbl_1.place(x=pos_x,y=pos_y)
		txt = Text(self.get_top_panel(),height=field_height,width=field_width)#state='disabled',background="gray75")
		txt.pack()
		txt.place(x=pos_x+(BLANK_SPACE_X*spaces),y=pos_y)
		return txt

	def add_chooser(self,option_list,chooser_label,spaces,pos_x,pos_y):
		panel = self.get_top_panel()
		lbl_1 = Label(panel, text=chooser_label)
		panel.add(lbl_1)
		lbl_1.place(x=pos_x,y=pos_y)
		cmb = Combobox(self.get_top_panel(),values=option_list,state='readonly')
		cmb.current(0)
		cmb.pack();
		cmb.place(x=pos_x+(BLANK_SPACE_X*spaces),y=pos_y)
		return cmb

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
