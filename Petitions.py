from Bio import Entrez
from Bio import SeqIO
import os

"""Begins a NCBI connection using your e-mail address.
	INPUTS: email --> e-mail address"""
def init(email):
	Entrez.email = email

"""Closes an open handle.
	INPUTS: data --> an open handle"""
def close(data):
	data.close();

"""Searches specific data into de NCBI database.
	INPUTS: database  --> is an string that specifies the database where you want to search.		Ex.: "nucleotide"
					term --> it's the name of the term that we want to search.		Ex.: "Human papillomavirus"
					email --> it's your e-mail address for begining the NCBI connection
	OUTPUTS: a list of sequence identifiers""""
def search(database,term,email):
	init(email)
	handle = Entrez.esearch(db=database, term=term)
	record = Entrez.read(handle)
	return record["IdList"]

"""Downloads the data based on sequence identifiers
	INPUTS: database  --> it's an string that specifies the database where you want to search.		Ex.: "nucleotide"
					identifier --> it's a string of identifiers separated by commas Ex.: "LC027929,KC470291,FJ237042"
					file_format --> it's a string that specifies the data format.
					email --> it's your e-mail address for begining the NCBI connection
	OUTPUTS: a handle object"""
def download(database,identifier,file_format,email):
	init(email)
	handle = Entrez.efetch(db=database, id=identifier, rettype=file_format, retmode="text")
	return handle

"""Parses a handle data.
	INPUTS: data --> it's a handle object. (It usually gotten by the download method)
					type_file --> it's a string that specifies the format of the handle data. 	Ex.:"genbank" 
	OUTPUTS: list of parsed sequnce (SeqIO list)"""
def parse(data,type_file):
	record = list(SeqIO.parse(data, type_file))
	return record

"""Saves the handle data into a file.
	INPUTS: filename --> it's the name which we want to save the file.
					data --> it's a handle data """
def save(filename,data):	
	if not os.path.isfile(filename):
		out_handle = open(filename, "w")
		out_handle.write(data.read())
		close(out_handle)
		close(data)
		print("Successfully saved")

"""Shows some information of a sequences list like: identifier, sequence and size.
	INPUTS: records_list --> a sequences list"""
def show_info(records_list):
	for i in range(len(records_list)):
		node = records_list[i];
		print("Id: " + node.id)
		print("Secuencia: " + repr(node.seq))
		print("Tam: " +str(len(node)) + "\n")

"""Changes a list of identifier into a string of identifiers separated by commas
	INPUTS: record_list -->a list of identifier
	OUTPUTS: string of identifiers separated by commas """
def format(records_list):
	cadena  = ""
	for i in range(len(records_list)):
		cadena = cadena + records_list[i]
		if i+1 != len(records_list):
			cadena = cadena + ","		
	return cadena

