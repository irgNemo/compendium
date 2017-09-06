from gui_constans import *
from Tkinter import *

def open_file(gui_obj,tab_informer,filename):
	#filename = self.lbl_selected_file['text']
	if filename != DEFAULT_SELECTED_FILE:
	   	try:
			basic_file = open(filename, 'r')
			#gui_obj.clean_informer(tab_informer)
			tab_informer.insert(INSERT,basic_file.read())
		except IOError:
			gui_obj.get_main_informer().insert(INSERT,IO_ERROR)

def update_selected_file(gui_obj, string):
	gui_obj.lbl_selected_file.config(text=string)

