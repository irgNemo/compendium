import tkFileDialog
#from os import scandir, getcwd
from os import walk
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

def get_selected_file(gui_obj):
	return gui_obj.lbl_selected_file.cget("text")

def update_selected_file(gui_obj, string):
	gui_obj.lbl_selected_file.config(text=string)
	#exp_arr = validate_selected_filename(string)
	#gui_obj.assing_available_tabs(exp_arr[1],exp_arr[2])

def set_main_folder(gui_obj,folder_settings_file=FOLDER_SETTINGS_FILENAME):
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
			gui_obj.get_main_informer().insert(INSERT,ERROR_FOLDER_NAME)
	except IOError:
		gui_obj.get_main_informer().insert(INSERT,IO_ERROR)


def assing_job(gui_obj,selected_filename):
	exp_arr = validate_selected_filename(selected_filename)
	gui_obj.working_folder = exp_arr[0]
	gui_obj.get_main_informer().insert(INSERT,WORKING_FOLDER_MSJ + gui_obj.working_folder)
	gui_obj.assing_available_tabs(exp_arr[1],exp_arr[2])
	#gui_obj.filter_frame.set_filename()



def get_extention(filename):		
	return filename.split('.')[1]

def get_basic_filename(filename):
	return filename.split('.')[0]

def get_clustalw_path():
	platform = sys.platform;
	if "linux" in platform:
		return CLUSTALW_LINUX_PATH
	else:
		return CLUSTALW_MAC_PATH

def get_current_files(path):
	#return [filename.name for filename in scandir(path) if filename.is_file()]	
	directories, subdirs, filenames = next(walk(path))
	return filenames

def show_path_files(path):
	files_list = get_current_files(path)
	files_list.sort()
	print path
	for filename in files_list:
		print filename













