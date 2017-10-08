import tkFileDialog
from gui_constans import *
from Tkinter import *
from validations import *

def open_file(gui_obj,tab_informer,filename):
	if filename != DEFAULT_SELECTED_FILE and validate_not_none(filename):
	   	try:
			basic_file = open(filename, 'r')
			data = basic_file.read()
			if data is EMPTY_SEARCH:
				update_selected_file(gui_obj, DEFAULT_SELECTED_FILE)
				tkMessageBox.showerror("Error", ERROR_EMPTY_FILE)
			else:
				tab_informer.insert(INSERT,data)
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
		gui_obj.get_main_informer().insert(INSERT,LOAD_SETTINGS_MSJ)
		basic_file = open(folder_settings_file, 'r')
		data = basic_file.read()
		print data
		basic_file.close()
		return data
	except IOError:
		gui_obj.get_main_informer().insert(INSERT,IO_ERROR)

def create_new_main_folder(gui_obj):
	try:
		new_folder_name = tkFileDialog.askdirectory()
		if validate_not_none(new_folder_name):
			basic_file = open(FOLDER_SETTINGS_FILENAME, 'w')
			basic_file.write(new_folder_name)
		else:
			gui_obj.get_main_informer().insert(INSERT,"Erroor no se selecciono ninguna carpeta")
	except IOError:
		gui_obj.get_main_informer().insert(INSERT,IO_ERROR)


def assing_job(gui_obj,selected_filename):
	exp_arr = validate_selected_filename(selected_filename)
	gui_obj.working_folder = exp_arr[0]
	gui_obj.get_main_informer().insert(INSERT,WORKING_FOLDER_MSJ + gui_obj.working_folder)
	gui_obj.assing_available_tabs(exp_arr[1],exp_arr[2])
	#gui_obj.filter_frame.set_filename()
		
def get_basic_filename(filename):
	return filename.split('.')[0]

