import re
from gui_constans import *

def validate_mail(mail):
	return bool(re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", mail))

def validate_is_number(data):
	return bool(re.search(r"[0-9]+",data))

def validate_not_none(data):
	if data is None or data is APUNTADOR_CARPETA or data is CADENA_VACIA:
		return False
	elif bool(re.search(r"^\s",data)):#validate not whitespaces
		return False
	else:
		return True

def validate_selected_filename(filename):
	regex = "/(.+)/(.+)/(.+)\.(fasta|gb|aln)"
	match = re.search(regex,filename)
	return [match.group(3), match.group(4)]
