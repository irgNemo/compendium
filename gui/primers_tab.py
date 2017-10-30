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
from src.constans import *;

class Primers_tab(Basic_tab):
	def __init__(self,tab,main_window):
		Basic_tab.__init__(self,tab,main_window,PRIMERS_INFORMER_HEIGHT,PRIMERS_INFORMERS_WIGTH)
		#field for number to return
		self.txt_primer_number = self.add_field("Returned primer's number:",2.1,10,10,DEFAULT_TXTBOX_HEIGHT,TXTBOX_PRIMER_SIZE_WIGTH,PRIMER_NUMBER)
		#field for Max self complementary
		self.txt_primer_max_self = self.add_field("Maximum self complementary:",2.5,260,10,DEFAULT_TXTBOX_HEIGHT,TXTBOX_PRIMER_SIZE_WIGTH)
		#field for concentration of monoralent cations
		self.txt_primer_salt_monovalent = self.add_field("Concentration of monoralent cations:",3,550,10,DEFAULT_TXTBOX_HEIGHT, TXTBOX_PRIMER_SIZE_WIGTH,SALT_MONOVALENT)
		#field for product range
		self.txt_primer_product_range = self.add_field("Primer product range:",2,10,40,DEFAULT_TXTBOX_HEIGHT,TXTBOX_PRIMER_SIZE_WIGTH,PRODUCT_RANGE)
		#field Max 3' stability
		self.txt_primer_max_3_stability = self.add_field("Maximum 3' stability:",2,260,40,DEFAULT_TXTBOX_HEIGHT,TXTBOX_PRIMER_SIZE_WIGTH)
		#field Max 3' self complementary
		self.txt_primer_max_3_self = self.add_field("Maximum 3' self complementary:",2.5,550,40,DEFAULT_TXTBOX_HEIGHT,TXTBOX_PRIMER_SIZE_WIGTH)
		#fields for primer size
		self.txt_primer_min_size = self.add_field("Minimum primer size:",2,10,70,DEFAULT_TXTBOX_HEIGHT,TXTBOX_PRIMER_SIZE_WIGTH,PRIMER_MIN_SIZE)
		self.txt_primer_opt_size = self.add_field("Optimal primer size:",2,260,70,DEFAULT_TXTBOX_HEIGHT,TXTBOX_PRIMER_SIZE_WIGTH,PRIMER_OPT_SIZE)	
		self.txt_primer_max_size = self.add_field("Maximum primer size:",2,550,70,DEFAULT_TXTBOX_HEIGHT,TXTBOX_PRIMER_SIZE_WIGTH,PRIMER_MAX_SIZE)
		#fields for primer tm
		self.txt_primer_min_tm = self.add_field("Minimum primer tm:",2,10,100,DEFAULT_TXTBOX_HEIGHT,TXTBOX_PRIMER_SIZE_WIGTH,PRIMER_MIN_TM)
		self.txt_primer_opt_tm = self.add_field("Optimal primer tm:",2,260,100,DEFAULT_TXTBOX_HEIGHT,TXTBOX_PRIMER_SIZE_WIGTH,PRIMER_OPT_TM)
		self.txt_primer_max_tm = self.add_field("Maximum primer tm:",2,550,100,DEFAULT_TXTBOX_HEIGHT,TXTBOX_PRIMER_SIZE_WIGTH,PRIMER_MAX_TM)
		#fields for primer gc%
		self.txt_primer_min_gc = self.add_field("Minimum primer gc:",2,10,130,DEFAULT_TXTBOX_HEIGHT,TXTBOX_PRIMER_SIZE_WIGTH,PRIMER_MIN_GC)
		self.txt_primer_max_gc = self.add_field("Maximum primer gc:",2,260,130,DEFAULT_TXTBOX_HEIGHT,TXTBOX_PRIMER_SIZE_WIGTH,PRIMER_MAX_GC)	
		#field for Max PolyX
		self.txt_primer_max_poly_x = self.add_field("Maximum primer Poly X:",2,550,130,DEFAULT_TXTBOX_HEIGHT,TXTBOX_PRIMER_SIZE_WIGTH,MAX_POLY_X)
		#field for sequence target
		self.txt_primer_seq_target = self.add_field("Sequence target:",2,10,160,DEFAULT_TXTBOX_HEIGHT,TXTBOX_PRIMER_SIZE_WIGTH,PRIMER_SEQ_TARGET)
		self.add_btn_primers(800,160)

	def add_btn_primers(self,pos_x,pos_y):
		btn_primers = Button(self.get_top_panel(), text ="Primers",command = self.run_btn_primers)
		btn_primers.pack()
		btn_primers.place(x=pos_x,y=pos_y)

	def run_btn_primers(self):
		thread = threading.Thread(target=self.btn_primers_call_back)
		thread.start()

	def btn_primers_call_back(self):
		consensus = parse(get_selected_file(self.main_window),FASTA_EXTENSION)
		consensus_seq = consensus[0].seq
		basic_filename = get_basic_filename(get_selected_file(self.main_window)).replace(PREFIX_CONSENSUS, "_th")
		
		full_primers_input_filename = basic_filename + PRIMERS_INPUT_FILENAME
		self.get_main_window().println("\nGetting primers input file...\n in "+full_primers_input_filename)
		add_parameter_to(full_primers_input_filename,PREFIX_SEQUENCE_ID,get_secction_name(get_selected_file(self.main_window)),self.get_main_window())
		add_parameter_to(full_primers_input_filename,PREFIX_SEQUENCE_TEMPLATE,consensus_seq,self.get_main_window())	
		add_parameter_to(full_primers_input_filename,PREFIX_PRIMER_SEQ_TARGET,PRIMER_SEQ_TARGET,self.get_main_window())
		
		add_parameter_to(full_primers_input_filename,PREFIX_PRODUCT_RANGE,PRODUCT_RANGE,self.get_main_window())	
		
		#....Todos los demas parametros iran aqui

		add_parameter_to(full_primers_input_filename,PREFIX_P3_FILE_FLAG,P3_FILE_FLAG_VALUE,self.get_main_window())
		add_parameter_to(full_primers_input_filename,EMPTY_STRING,EMPTY_STRING,self.get_main_window())

		"""self.get_main_window().println("\nParsing consensus sequence...")
		consensus = parse(get_selected_file(self.main_window),FASTA_EXTENSION)
		consensus_seq = consensus[0].seq
		full_primers_input_filename = get_basic_filename(get_selected_file(self.main_window))+PRIMERS_INPUT_FILENAME
		print ("nombre arch input: " + full_primers_input_filename)
		self.get_main_window().println("\nGetting primers input file...")
		generate_basic_primers_input(full_primers_input_filename, PRIMERS_INPUT_FILENAME, str(consensus_seq),"37,21")
		self.get_main_window().println("\nGetting primers...")
		get_primers(full_primers_input_filename,self.get_main_window()) 
		#self.get_main_window().println("\nReading primers output...")
		#primers_data = read_primers(PRIMERS_INPUT_FILENAME)
		#print primers_data"""






