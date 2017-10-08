from Tkinter import *
from ttk import *
from basic_tab import *
from gui_constans import *
from gui_utils import *
import sys
sys.path.append("../")
from src.utils import *;
from src.Petitions import *;
from src.Alignments import *;
from src.constans import *;

class Align_tab(Basic_tab):
	def __init__(self,tab,main_window):
		Basic_tab.__init__(self,tab,main_window,ALIGN_INFORMER_HEIGHT,ALIGN_INFORMERS_WIGTH)
		self.add_chooser(ALIGNERS_OPTIONS,"Select an alignment tool:",2,10,10)
		self.add_btn_align(100,100)

	def add_btn_align(self,pos_x,pos_y):
		btn_filter = Button(self.get_top_panel(), text ="Align",command = self.btn_align_call_back)
		btn_filter.pack()
		btn_filter.place(x=pos_x,y=pos_y)

	def btn_align_call_back(self):
		filename = get_selected_file(self.main_window)
		clustal_align(filename, clustalw2_path);



