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

class Filter_tab(Basic_tab):

	def __init__(self,tab,main_window):
		Basic_tab.__init__(self,tab,30,125)
		self.main_window = main_window
		self.add_filename_field(500,50,DEFAULT_TXTBOX_HEIGHT,TXTBOX_FILENAME_WIGTH)
		self.add_tag_values_field(10,50,DEFAULT_TXTBOX_HEIGHT,TXTBOX_TAG_VALUES_WIGTH)
		self.add_feature_name_chooser(10,20)
		self.add_feature_tag_chooser(290,20)
		self.add_feature_tag_per_sequence_chooser(555,20)
		self.add_btn_filter(830,50)

	def add_filename_field(self,pos_x,pos_y,field_height,field_width):
		panel = self.get_top_panel()
		lbl_1 = Label(panel, text='Filename:')
		panel.add(lbl_1)
		lbl_1.place(x=pos_x,y=pos_y)
		self.txt_filename = Text(self.get_tab(),height=field_height,width=field_width)#state='disabled',background="gray75")
		self.txt_filename.pack()
		self.txt_filename.place(x=pos_x+BLANK_SPACE_X,y=pos_y)

	def add_tag_values_field(self,pos_x,pos_y,field_height,field_width):
		panel = self.get_top_panel()
		lbl_1 = Label(panel, text='Tag values (Separeted by whitespace): ')
		panel.add(lbl_1)
		lbl_1.place(x=pos_x,y=pos_y)
		self.txt_tag_values = Text(self.get_tab(),height=field_height,width=field_width)#state='disabled',background="gray75")
		self.txt_tag_values.pack()
		self.txt_tag_values.place(x=pos_x+(BLANK_SPACE_X*3),y=pos_y)

	def disable_filter(self):
		if self.enable_filter_var.get() is CHKBOX_ON:
			self.enable_filter_var.set(CHKBOX_OFF)
			self.println(self.main_window.get_main_informer(),"Filter disable")

	def add_feature_name_chooser(self,pos_x,pos_y):
		panel = self.get_top_panel()
		lbl_1 = Label(panel, text='Feature name: ')
		panel.add(lbl_1)
		lbl_1.place(x=pos_x,y=pos_y)
		self.cmb_feature_name = Combobox(self.get_tab(),values=FEATURE_NAME_OPTIONS,state='readonly')
		self.cmb_feature_name.current(0)
		self.cmb_feature_name.pack();
		self.cmb_feature_name.place(x=pos_x+(BLANK_SPACE_X*1.2),y=pos_y)


	def add_feature_tag_chooser(self,pos_x,pos_y):
		panel = self.get_top_panel()
		lbl_1 = Label(panel, text='Feature tag: ')
		panel.add(lbl_1)
		lbl_1.place(x=pos_x,y=pos_y)
		self.cmb_feature_tag = Combobox(self.get_tab(),values=FEATURE_TAG_OPTIONS,state='readonly')
		self.cmb_feature_tag.current(0)
		self.cmb_feature_tag.pack();
		self.cmb_feature_tag.place(x=pos_x+BLANK_SPACE_X,y=pos_y)

	def add_feature_tag_per_sequence_chooser(self,pos_x,pos_y):
		panel = self.get_top_panel()
		lbl_1 = Label(panel, text='Feature tag per sequence: ')
		panel.add(lbl_1)
		lbl_1.place(x=pos_x,y=pos_y)
		self.cmb_feature_tag_per_seq= Combobox(self.get_tab(),values=FEATURE_TAG_OPTIONS_PER_SEQ,state='readonly')
		self.cmb_feature_tag_per_seq.current(0)
		self.cmb_feature_tag_per_seq.pack();
		self.cmb_feature_tag_per_seq.place(x=pos_x+(BLANK_SPACE_X*2.1),y=pos_y)

	def add_btn_filter(self,pos_x,pos_y):
		btn_filter = Button(self.get_top_panel(), text ="Filter", 
command = self.btn_filter_call_back)
		btn_filter.pack()
		btn_filter.place(x=pos_x,y=pos_y)

	def btn_filter_call_back(self):
		if validate_not_none(self.txt_tag_values.get("1.0","end-1c")):
			self.println(self.main_window.get_main_informer(),"Reading data from selected file...")
			#TODO:Expresion regular para obtener la extencion del archivo
			#TODO:validar expension del arch.
			record = parse(get_selected_file(self.main_window), 'gb')
			self.println(self.main_window.get_main_informer(),"Getting sequences with tag values...")
			records_filtered = filterByNCBITagValue(record,self.cmb_feature_name.get(),self.cmb_feature_tag.get().split(), self.txt_tag_values.get("1.0","end-1c").split());
			if records_filtered != EMPTY_LIST:
				self.println(self.main_window.get_main_informer(),"Filtering tag values...")
				orfs = separate_ORFs_per_sequence(records_filtered,self.cmb_feature_name.get(),self.cmb_feature_tag_per_seq.get(), self.txt_tag_values.get("1.0","end-1c").split());
				self.println(self.main_window.get_main_informer(),"Saving filtered secuences...")
				main_folder = self.main_window.get_main_folder()
				if validate_not_none(main_folder):
					filename = self.txt_filename.get("1.0","end-1c")
					if validate_not_none(filename):
						new_file_name = main_folder + "/"+ filename + "/" + filename
						self.clean_informer(self.get_informer())
						for key in orfs.keys():
							self.println(self.main_window.get_main_informer(),"Saving "+key+"...")
							file_path = writeFile(orfs[key],new_file_name + "_" + key , ALINGING_FORMAT);
							self.println(self.get_informer(),"---"+key+" SEQUENCES---\n")
							open_file(self.main_window,self.get_informer(),file_path)
							self.println(self.main_window.get_main_informer(),key+" sequences were saved at:\n"+file_path)
					else:
						tkMessageBox.showerror("Error", ERROR_FILE_NAME)
				else:
					tkMessageBox.showerror("Error", ERROR_FOLDER_NAME)
			else:
				tkMessageBox.showerror("Error", ERROR_FILTERING)
				self.println(self.get_informer(),ERROR_FILTERING)
		else:
			tkMessageBox.showerror("Error", ERROR_TAGS_VALUES)



	


