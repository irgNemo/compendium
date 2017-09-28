import tkFileDialog
from gui_constans import *
from Tkinter import *
from validations import *

def open_file(gui_obj,tab_informer,filename):
	if filename != DEFAULT_SELECTED_FILE and validate_not_none(filename):
	   	try:
			basic_file = open(filename, 'r')
			tab_informer.insert(INSERT,basic_file.read())
		except IOError:
			update_selected_file(gui_obj, DEFAULT_SELECTED_FILE)
			gui_obj.get_main_informer().insert(INSERT,IO_ERROR)
	else:
		update_selected_file(gui_obj, DEFAULT_SELECTED_FILE)
		gui_obj.get_main_informer().insert(INSERT,SELECTED_FILE_WARNING)

def update_selected_file(gui_obj, string):
	gui_obj.lbl_selected_file.config(text=string)

def get_selected_file(gui_obj):
	return gui_obj.lbl_selected_file.cget("text")

def set_main_folder(folder_settings_file,gui_obj):
   	try:
		basic_file = open(folder_settings_file, 'r')
		return basic_file.read()
	except IOError:
		gui_obj.get_main_informer().insert(INSERT,IO_ERROR)

def create_new_main_folder(gui_obj):
	try:
		new_folder_name = tkFileDialog.askdirectory()
		basic_file = open(FOLDER_SETTINGS_FILENAME, 'w')
		basic_file.write(new_folder_name)
	except IOError:
		gui_obj.get_main_informer().insert(INSERT,IO_ERROR)

