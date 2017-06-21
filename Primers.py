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
	#archivo.seek(2);
	lista = [SEQUENCE_ID+EQUAL_SIGN+seq_id+NEW_LINE,
	SEQUENCE_TEMPLATE+EQUAL_SIGN+seq+NEW_LINE,
	SEQUENCE_TARGET+EQUAL_SIGN+seq_target+NEW_LINE,
	PRIMER_PRODUCT_SIZE_RANGE+EQUAL_SIGN+product_size+NEW_LINE,
	P3_FILE_FLAG+NEW_LINE,
	EQUAL_SIGN+NEW_LINE]
	#print lista
	archivo.writelines(lista)
	archivo.close()
	
def get_primers(input_filename):
	
	#os.system('primer3_core -output=./output/hpv_type18/* '+ input_filename)
	print 'READY'
	os.system('primer3_core < ' + input_filename)
	
	"""primer3_core -output='/home/karla/Desktop/mis_repositorios/compendioBioPython/compendium/output/hpv_type18/hola' archPruebaPrimers.txt """
	#[ -d ./compendium/ ] && echo "yes"
	"""primer3_core -output='./output/hpv_type18/holito' archPruebaPrimers.txt"""
	
	
nombre_arch = './output/hpv_type18/'
#'./output/hpv_type18/primers/input'
"""seq_id = "1"
seq = 'GTAGTCAGTAGACNATGACNACTGACGATGCAGACNACACACACACACACAGCACACAGGTATTAGTGGGCCATTCGATCCCGACCCAAATCGATAGCTACGATGACG'
seq_target = '37,21'

nombre_arch = nombre_arch + seq_id
print 'Generating basic primers input ...'
generate_basic_primers_input(nombre_arch,seq_id,seq,seq_target)

print 'Getting primers ... '
get_primers(nombre_arch)"""

make_primers_dir(nombre_arch)
