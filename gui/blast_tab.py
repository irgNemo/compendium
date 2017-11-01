import threading
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
from src.Primers import *;

class Blast_tab(Basic_tab):
	def __init__(self,tab,main_window):
		Basic_tab.__init__(self,tab,main_window,BLAST_INFORMER_HEIGHT,BLAST_INFORMERS_WIGTH)
		self.add_btn_blast(800,30)

	def add_btn_blast(self,pos_x,pos_y):
		btn_blast = Button(self.get_top_panel(), text ="Blast",command = self.run_btn_blast)
		btn_blast.pack()
		btn_blast.place(x=pos_x,y=pos_y)

	def run_btn_blast(self):
		thread = threading.Thread(target=self.btn_blast_call_back)
		thread.start()

	def btn_blast_call_back(self):
		primers_id_list = self.get_main_window().get_primers_id_list()

		if is_empty(primers_id_list):
			self.get_main_window().add_to_primers_id_list(get_selected_file(self.get_main_window()).split("input")[0])		

		for primer_id in primers_id_list:
			self.get_main_window().println("\n\n---Working with "+primer_id+"---\n")
			primers_list = get_primers_list(primer_id,self.get_main_window())
			self.get_main_window().println("\n\nGetting blast data...")
			blast_data = get_blast_data(primers_list[0:2],self.get_main_window())
			self.get_main_window().println("\n\nSaving blast file")
			save_new_file(self.get_main_window(),all_primers_filename+"blast",blast_data)
			self.get_main_window().println("\n\nBlast file was save in "+ all_primers_filename+"blast")





