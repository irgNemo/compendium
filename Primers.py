import os

#Constants
SEQUENCE_ID = "SEQUENCE_ID"
SEQUENCE_TEMPLATE = "SEQUENCE_TEMPLATE"
SEQUENCE_TARGET = "SEQUENCE_TARGET"
PRIMER_PRODUCT_SIZE_RANGE = "PRIMER_PRODUCT_SIZE_RANGE"
P3_FILE_FLAG = "P3_FILE_FLAG=1"
EQUAL_SIGN = "="
NEW_LINE = '\n'
DEFAULT_PRODUCT_SIZE = "100-300"
PRIMERS_FOLDER = "/primers/"
#################

def make_primers_dir(based_path):
	os.system('mkdir '+ based_path +PRIMERS_FOLDER);
	return based_path +PRIMERS_FOLDER

def generate_basic_primers_input(nombre_arch,seq_id,seq,seq_target,product_size=DEFAULT_PRODUCT_SIZE):
	archivo = open(nombre_arch, 'a')
	lista = [SEQUENCE_ID+EQUAL_SIGN+seq_id+NEW_LINE,
	SEQUENCE_TEMPLATE+EQUAL_SIGN+seq+NEW_LINE,
	SEQUENCE_TARGET+EQUAL_SIGN+seq_target+NEW_LINE,
	PRIMER_PRODUCT_SIZE_RANGE+EQUAL_SIGN+product_size+NEW_LINE,
	P3_FILE_FLAG+NEW_LINE,
	EQUAL_SIGN+NEW_LINE]
	archivo.writelines(lista)
	archivo.close()
	
def get_primers(input_filename):
	print 'Getting primers ...'
	os.system('primer3_core < ' + input_filename)

