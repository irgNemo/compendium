from Tkinter import *
from ttk import *
from gui_constans import *

class Basic_tab:

	def __init__(self,tab,main_window,height=DEFAULT_TAB_INFORMERS_HEIGHT,width=DEFAULT_TAB_INFORMERS_WIGTH):
		self.tab = tab
		self.main_window = main_window
		self.add_top_panel(tab)
		self.insert_informer(tab,height,width)

	def insert_informer(self,tab,height,width):
		self.informer = Text(tab,height=height,width=width)	
		scroll = Scrollbar(tab,command=self.informer.yview)
		scroll.pack(side=RIGHT, fill=Y)
		self.informer.pack(side=RIGHT, fill=BOTH,expand=True)
		scroll.config(command=self.informer.yview)
		self.informer.config(yscrollcommand=scroll.set)

	def add_top_panel(self,tab,panel_height=TOP_PANEL_TAB_HEIGHT):
		self.top_panel = PanedWindow(tab, height=panel_height)
		self.top_panel.pack(fill=BOTH,expand=PANELS_EXPAND)

	def add_separator(self,widget,pos_x,pos_y,sep_orient):
		separator = Separator(widget, orient='horizontal').pack(fill=X,pady=140)

	def add_field(self,field_label,spaces,pos_x,pos_y,field_height,field_width):
		panel = self.get_top_panel()
		lbl_1 = Label(panel, text=field_label)
		panel.add(lbl_1)
		lbl_1.place(x=pos_x,y=pos_y)
		txt = Text(self.get_tab(),height=field_height,width=field_width)#state='disabled',background="gray75")
		txt.pack()
		txt.place(x=pos_x+(BLANK_SPACE_X*spaces),y=pos_y)
		return txt

	def add_chooser(self,option_list,chooser_label,spaces,pos_x,pos_y):
		panel = self.get_top_panel()
		lbl_1 = Label(panel, text=chooser_label)
		panel.add(lbl_1)
		lbl_1.place(x=pos_x,y=pos_y)
		cmb = Combobox(self.get_tab(),values=option_list,state='readonly')
		cmb.current(0)
		cmb.pack();
		cmb.place(x=pos_x+(BLANK_SPACE_X*spaces),y=pos_y)
		return cmb
		
	def clean_informer(self,tab_informer):
		self.informer.delete(1.0,END)

	def println(self,informer,msj):
		informer.insert(INSERT,'\n'+msj)

	def get_main_window(self):
		return self.main_window

	def get_informer(self):
		return self.informer

	def get_top_panel(self):
		return self.top_panel

	def get_tab(self):
		return self.tab
