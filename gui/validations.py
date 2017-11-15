import re
import os
import os.path
from gui_constans import *

def validate_mail(mail):
	return bool(re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", mail))

def validate_is_number(data):
	return bool(re.search(r"[0-9]+",data))

def validate_not_none(data):
	if data is None or data is FOLDER_POINTER or data is "":
		return False
	elif bool(re.search(r"^\s",data)):#validate not whitespaces
		return False
	else:
		return True

def validate_selected_filename(filename):
	try:
		regex = "/(.+)/(.+)/(.+)\.(fasta|gb|aln|dnd|all)"
		match = re.search(regex,filename)
		return [match.group(2), match.group(3), match.group(4)]
	except:
		print "IT's default"

def is_consensus_file(filename):
	if PREFIX_CONSENSUS in filename:
		return True

def get_secction_name(filename):
	regex = "(\w+)\."
	match = re.search(regex,filename)
	return match.group(0).replace(".","")

def get_basic_path(filename): 
	regex = "(.+)/(.+)/(\w+)\."
	match = re.search(regex,filename)
	return match.group(0)

def is_empty_primers_output(filename):
	filesize = os.path.getsize(filename)
	if filesize <= PRIMERS_OUTPUT_FILE_MIN_SIZE:
		return True

def exists(filename):
	return  os.path.exists(filename)


def is_current(filaname_list,current_section):
	filename = "hola"
	size = len(filaname_list)
	for i in range(0,size):
		print "i : " + i
		print "value: " + filaname_list[i]
		if "E7" in filaname_list[i]:
			filename = filaname_list[i]
	return filename

def get_threshold(data_list):
	threshold = ""
	for item in data_list:
		regex = "(.+)th(\d+)(.+)"
		match = re.search(regex,item)
		if match.group(2):
			threshold = match.group(2)
	return threshold,item


















