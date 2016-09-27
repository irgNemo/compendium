from Bio import Entrez
from Bio import SeqIO
import os

def init(email):
	Entrez.email = email
	
def close(data):
	data.close();
	
def search(data_base,term,email):
	init(email)
	handle = Entrez.esearch(db=data_base, term=term)
	record = Entrez.read(handle)
	return record["IdList"]
	
def download(data_base,identifier,file_format,email):
	init(email)
	handle = Entrez.efetch(db=data_base, id=identifier, rettype=file_format, retmode="text")
	return handle

def parse(data,type_file):
	record = list(SeqIO.parse(data, type_file))
	return record

def save(file_name,data):	
	if not os.path.isfile(file_name):
		out_handle = open(file_name, "w")
		out_handle.write(data.read())
		close(out_handle)
		close(data)
		print("Successfully saved")

def show_info(records_list):
	for i in range(len(records_list)):
		node = records_list[i];
		print("Id: " + node.id)
		print("Secuencia: " + repr(node.seq))
		print("Tam: " +str(len(node)) + "\n")

def format(records_list):
	cadena  = ""
	for i in range(len(records_list)):
		cadena = cadena + records_list[i]
		if i+1 != len(records_list):
			cadena = cadena + ","		
	return cadena

