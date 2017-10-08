from Tkinter import *
from ttk import *
from basic_tab import *
from gui_constans import *
from gui_utils import *
import sys
sys.path.append("../")
from src.utils import *;
from src.Petitions import *;
from src.constans import *;

class Primers_tab(Basic_tab):
	def __init__(self,tab,main_window):
		Basic_tab.__init__(self,tab,main_window,ALIGN_INFORMER_HEIGHT,ALIGN_INFORMERS_WIGTH)
		#fields for primer size
		self.txt_primer_min_size = self.add_field("Minimum primer size:",2,10,40,DEFAULT_TXTBOX_HEIGHT,TXTBOX_PRIMER_SIZE_WIGTH)
		self.txt_primer_opt_size = self.add_field("Optimal primer size:",2,250,40,DEFAULT_TXTBOX_HEIGHT,TXTBOX_PRIMER_SIZE_WIGTH)	
		self.txt_primer_max_size = self.add_field("Maximum primer size:",2,500,40,DEFAULT_TXTBOX_HEIGHT,TXTBOX_PRIMER_SIZE_WIGTH)
		#fields for primer tm
		self.txt_primer_min_tm = self.add_field("Minimum primer tm:",2,10,80,DEFAULT_TXTBOX_HEIGHT,TXTBOX_PRIMER_SIZE_WIGTH)
		self.txt_primer_opt_tm = self.add_field("Optimal primer tm:",2,250,80,DEFAULT_TXTBOX_HEIGHT,TXTBOX_PRIMER_SIZE_WIGTH)
		self.txt_primer_max_tm = self.add_field("Maximum primer tm:",2,500,80,DEFAULT_TXTBOX_HEIGHT,TXTBOX_PRIMER_SIZE_WIGTH)
		#fields for primer gc%
		self.txt_primer_min_gc = self.add_field("Minimum primer gc:",2,10,120,DEFAULT_TXTBOX_HEIGHT,TXTBOX_PRIMER_SIZE_WIGTH)
		self.txt_primer_opt_gc = self.add_field("Optimal primer gc:",2,250,120,DEFAULT_TXTBOX_HEIGHT,TXTBOX_PRIMER_SIZE_WIGTH)
		self.txt_primer_max_gc = self.add_field("Maximum primer gc:",2,500,120,DEFAULT_TXTBOX_HEIGHT,TXTBOX_PRIMER_SIZE_WIGTH)	

