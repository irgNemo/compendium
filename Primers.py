import os
import os.path
import re
from Bio.Blast import NCBIWWW

#Constants
EXP_REG_RNA = '[A|C|G|T]{4,}|[a|c|g|t]{4,}'#{4,}filtra que la longitud de la cadena sea mayor a 4 caracteres
SEQUENCE_ID = "SEQUENCE_ID"
SEQUENCE_TEMPLATE = "SEQUENCE_TEMPLATE"
SEQUENCE_TARGET = "SEQUENCE_TARGET"
PRIMER_PRODUCT_SIZE_RANGE = "PRIMER_PRODUCT_SIZE_RANGE"
P3_FILE_FLAG = "P3_FILE_FLAG=1"
EQUAL_SIGN = "="
NEW_LINE = '\n'
SEPARATOR = '--------------------------------------'
DEFAULT_PRODUCT_SIZE = "100-300"
PRIMERS_FOLDER = "/primers/"
LEFT_PRIMERS_EXT = ".for"
RIGHT_PRIMERS_EXT = ".rev"
INTERNAL_PRIMERS_EXT = ".int"
BLAST_PROGRAM = "blastn"
BLAST_DATABASE = "nt"
BLAST_OUT_FORMAT = "text"

#################

def make_primers_dir(based_path):
	os.system('mkdir '+ based_path +PRIMERS_FOLDER);
	return based_path +PRIMERS_FOLDER

def generate_basic_primers_input(filename,seq_id,seq,seq_target,product_size=DEFAULT_PRODUCT_SIZE):
	primers_file = open(filename, 'w')
	lista = [SEQUENCE_ID+EQUAL_SIGN+seq_id+NEW_LINE,
	SEQUENCE_TEMPLATE+EQUAL_SIGN+seq+NEW_LINE,
	SEQUENCE_TARGET+EQUAL_SIGN+seq_target+NEW_LINE,
	PRIMER_PRODUCT_SIZE_RANGE+EQUAL_SIGN+product_size+NEW_LINE,
	P3_FILE_FLAG+NEW_LINE,
	EQUAL_SIGN+NEW_LINE]
	primers_file.writelines(lista)
	primers_file.close()
	
def get_primers(input_filename):
	print 'Getting primers ...'
	os.system('primer3_core < ' + input_filename)

def read_primers_file(filename):
	try:
		primers_file = open(filename,'r')
		data = primers_file.read()
		primers_file.close()
		print'File was successfully opened'
	except IOError:
		print'Error! File cannot be opened'
	return data

def get_file_data(filename,file_type):
	data = ''
	print 'Getting ' + filename + file_type + ' data ...'
	if os.path.isfile(filename + file_type):
		data = data + read_primers_file(filename + file_type)
	else:
		'Error! File does not exist '
	return data 

def set_primers_data_format(data):
	split_data = data.split('PRIMERS')
	print len(split_data)
	title = split_data[0] + "\n                         ."
	primers_data = split_data[1]
	return title + primers_data
	
def read_primers(based_filename):
	separator = NEW_LINE + SEPARATOR + SEPARATOR + NEW_LINE + NEW_LINE
	data = get_file_data(based_filename ,LEFT_PRIMERS_EXT)+ separator
	data = data + get_file_data(based_filename ,RIGHT_PRIMERS_EXT) + separator
	data = data + get_file_data(based_filename ,INTERNAL_PRIMERS_EXT)
	return data

def get_primers_list(filename):
	text = ''
	text = text + get_file_data(filename,LEFT_PRIMERS_EXT)
	text = text + get_file_data(filename,RIGHT_PRIMERS_EXT)
	text = text + get_file_data(filename,INTERNAL_PRIMERS_EXT)
	text_split = text.split('lity')
	new_text = text_split[::1]
	str1 = ''.join(new_text)
	primers_list = re.findall(EXP_REG_RNA, str1)
	return primers_list	

def split_blast_results(results):
	text_split = results.split('<PRE>')
	str1 = ''.join(text_split[1])
	final_split = str1.split('</form>')
	return ''.join(final_split[0])

def run_blast(sequence,blast_program=BLAST_PROGRAM ,database=BLAST_DATABASE):#,output_filename): solo si format_type != "Text"
	print 'Getting blast ' + sequence + ' results ...'
	result_handle = NCBIWWW.qblast(blast_program, database, sequence, format_type=BLAST_OUT_FORMAT)#Es importante manajerlo como "Text" para obtener un String
	print 'Finishing getting ' + sequence + ' blast data.'
	blast_results = result_handle.getvalue() #Se puede retornar como String
	result_handle.close()
	return split_blast_results(blast_results)
	#Asi se evita crear un archivo xml para cada primer
	"""print 'Saving blast results ...'
	out_handle = open(output_filename, "w")
	out_handle.write(result_handle.read())
	result_handle.close()
	out_handle.close()
	print ('Blast results were saved at ' + output_filename)"""

def get_blast_data(primers_list,blast_program=BLAST_PROGRAM ,database=BLAST_DATABASE):
	data = ""
	print 'Getting blast primars information ...'
	for each in primers_list:
		data = data + run_blast(each)
	return data


data = run_blast('GCGCTTTGAGGATCCAACAC')
split_data = data.split('Length=')
print split_data[0]
