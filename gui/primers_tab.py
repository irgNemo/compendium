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
		#field for number to return
		self.txt_primer_number = self.add_field("Returned primer's number:",2.1,10,10,DEFAULT_TXTBOX_HEIGHT,TXTBOX_PRIMER_SIZE_WIGTH)
		#field for Max self complementary
		self.txt_primer_max_self = self.add_field("Maximum self complementary:",2.5,260,10,DEFAULT_TXTBOX_HEIGHT,TXTBOX_PRIMER_SIZE_WIGTH)
		#field for concentration of monoralent cations
		self.txt_primer_salt_monovalent = self.add_field("Concentration of monoralent cations:",3,550,10,DEFAULT_TXTBOX_HEIGHT, TXTBOX_PRIMER_SIZE_WIGTH)
		#fields for primer size
		self.txt_primer_min_size = self.add_field("Minimum primer size:",2,10,40,DEFAULT_TXTBOX_HEIGHT,TXTBOX_PRIMER_SIZE_WIGTH)
		self.txt_primer_opt_size = self.add_field("Optimal primer size:",2,250,40,DEFAULT_TXTBOX_HEIGHT,TXTBOX_PRIMER_SIZE_WIGTH)	
		self.txt_primer_max_size = self.add_field("Maximum primer size:",2,500,40,DEFAULT_TXTBOX_HEIGHT,TXTBOX_PRIMER_SIZE_WIGTH)
		#fields for primer tm
		self.txt_primer_min_tm = self.add_field("Minimum primer tm:",2,10,70,DEFAULT_TXTBOX_HEIGHT,TXTBOX_PRIMER_SIZE_WIGTH)
		self.txt_primer_opt_tm = self.add_field("Optimal primer tm:",2,250,70,DEFAULT_TXTBOX_HEIGHT,TXTBOX_PRIMER_SIZE_WIGTH)
		self.txt_primer_max_tm = self.add_field("Maximum primer tm:",2,500,70,DEFAULT_TXTBOX_HEIGHT,TXTBOX_PRIMER_SIZE_WIGTH)
		#fields for primer gc%
		self.txt_primer_min_gc = self.add_field("Minimum primer gc:",2,10,100,DEFAULT_TXTBOX_HEIGHT,TXTBOX_PRIMER_SIZE_WIGTH)
		self.txt_primer_max_gc = self.add_field("Maximum primer gc:",2,250,100,DEFAULT_TXTBOX_HEIGHT,TXTBOX_PRIMER_SIZE_WIGTH)	
		#field for Max PolyX
		self.txt_primer_max_poly_x = self.add_field("Maximum primer Poly X:",2,500,100,DEFAULT_TXTBOX_HEIGHT,TXTBOX_PRIMER_SIZE_WIGTH)
		#field for product range
		self.txt_primer_product_range = self.add_field("Primer product range:",2,10,130,DEFAULT_TXTBOX_HEIGHT,TXTBOX_PRIMER_SIZE_WIGTH)
		#field Max 3' stability
		self.txt_primer_max_3_stability = self.add_field("Maximum 3' stability:",2,250,130,DEFAULT_TXTBOX_HEIGHT,TXTBOX_PRIMER_SIZE_WIGTH)
		#field Max 3' self complementary
		self.txt_primer_max_3_self = self.add_field("Maximum 3' self complementary:",2.5,500,130,DEFAULT_TXTBOX_HEIGHT,TXTBOX_PRIMER_SIZE_WIGTH)
		self.add_btn_primers(800,150)

	def add_btn_primers(self,pos_x,pos_y):
		btn_primers = Button(self.get_top_panel(), text ="Primers",command = self.run_btn_primers)
		btn_primers.pack()
		btn_primers.place(x=pos_x,y=pos_y)

	def run_btn_primers(self):
		thread = threading.Thread(target=self.btn_align_call_back)
		thread.start()

	def btn_primers_call_back(self):
		print "primers tab is runing"









