from Tkinter import *
import tkMessageBox
from ttk import *
from basic_tab import * 
from gui_constans import *
from gui_utils import *
from validations import *
import sys
sys.path.append("../")
from src.utils import *;
from src.Petitions import *;
from src.constans import *;

import sys
print '\n'.join(sys.modules.keys())

class Filter_tab(Basic_tab):

	def __init__(self,tab,main_window):
		Basic_tab.__init__(self,tab,main_window,30,125)
		self.txt_filename = self.add_field("Filename:",1,500,50,DEFAULT_TXTBOX_HEIGHT,TXTBOX_FILENAME_WIGTH)
		self.txt_tag_values = self.add_field("Tag values (Separeted by whitespace):",3,10,50,DEFAULT_TXTBOX_HEIGHT,TXTBOX_TAG_VALUES_WIGTH)
		self.cmb_feature_name = self.add_chooser(FEATURE_NAME_OPTIONS,"Feature name: ",1.2,10,20)
		self.cmb_feature_tag = self.add_chooser(FEATURE_TAG_OPTIONS,"Feature tag:",1,290,20)
		self.cmb_feature_tag_per_seq = self.add_chooser(FEATURE_TAG_OPTIONS_PER_SEQ,"Feature tag per sequence:",2.1,555,20)
		self.add_btn_filter(830,50)

	def set_filename(self,filename):
		self.txt_filename.insert(INSERT,filename)
		self.txt_filename.config(state='disabled',background="light gray")

	def add_btn_filter(self,pos_x,pos_y):
		btn_filter = Button(self.get_top_panel(), text ="Filter",command = self.btn_filter_call_back)
		btn_filter.pack(expand=True)
		btn_filter.place(x=pos_x,y=pos_y)

	def btn_filter_call_back(self):
		try:
			if validate_not_none(self.txt_tag_values.get("1.0","end-1c")):
				self.println(self.get_main_window().get_main_informer(),"Reading data from selected file...")
				record = parse(get_selected_file(self.get_main_window()), 'gb')
				self.println(self.get_main_window().get_main_informer(),"Getting sequences with tag values...")
				records_filtered = filterByNCBITagValue(record,self.cmb_feature_name.get(),self.cmb_feature_tag.get().split(), self.txt_tag_values.get("1.0","end-1c").split());
				if records_filtered != EMPTY_LIST:
					self.println(self.get_main_window().get_main_informer(),"Filtering tag values...")
					orfs = separate_ORFs_per_sequence(records_filtered,self.cmb_feature_name.get(),self.cmb_feature_tag_per_seq.get(), self.txt_tag_values.get("1.0","end-1c").split());
					self.println(self.get_main_window().get_main_informer(),"Saving filtered secuences...")
					main_folder = self.get_main_window().get_main_folder()
					if validate_not_none(main_folder):
						filename = self.txt_filename.get("1.0","end-1c")
						if validate_not_none(filename):
							new_file_name = main_folder + "/"+ filename + "/" + filename
							self.clean_informer(self.get_informer())
							for key in orfs.keys():
								self.println(self.get_main_window().get_main_informer(),"\nSaving "+key+"...\n")
								if orfs[key] == EMPTY_LIST:
									self.get_main_window().get_main_informer().insert(INSERT,key + " sequences are not contained in the file")
								else:
									file_path = writeFile(orfs[key],new_file_name + "_" + key , FASTA_EXTENSION);
									update_selected_file(self.get_main_window(),file_path)
									if validate_not_none(file_path):
										self.get_main_window().add_to_filename_list(file_path)
										self.println(self.get_main_window().get_main_informer(),"\nThe file was saved in: "+file_path)
									else:
										self.println(self.get_main_window().get_main_informer(),"Error al filtrar")
									self.println(self.get_informer(),"---"+key+" SEQUENCES---\n")
									open_file(self.get_main_window(),self.get_informer(),file_path)
						else:
							tkMessageBox.showerror("Error", ERROR_FILE_NAME)
					else:
						tkMessageBox.showerror("Error", ERROR_FOLDER_NAME)
				else:
					tkMessageBox.showerror("Error", ERROR_FILTERING)
					self.println(self.get_informer(),ERROR_FILTERING)
			else:
				tkMessageBox.showerror("Error", ERROR_TAGS_VALUES)
			self.get_main_window().println(PROCESS_FINISHED_MSJ)
		except:
			self.get_main_window().println(ERROR_PROCESSING)
			self.println(self.get_informer(),"Prueba print")
		
		if len(self.get_main_window().get_filename_list()) != 0:
			update_selected_file(self.get_main_window(), self.get_main_window().get_filename_list()[INICIAL])
	


