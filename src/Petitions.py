import os
import re
from Bio import Entrez
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Tkinter import *


def init(email):
	"""
	Begins a NCBI connection using your e-mail address.

	:param email: e-mail address as String
	"""
	Entrez.email = email

def close(data):
	"""
	Closes an open handle.

	:param data: an open handle
	"""
	data.close();

def search(database, term, email, retmax=20):
	"""
	Searches specific data into de NCBI database.

	:param  database: is an string that specifies the database where you want to search. Ex.: "nucleotide"

	:param term: it's the name of the term that we want to search.		Ex.: "Human papillomavirus"

	:param email: it's your e-mail address for begining the NCBI connection as String

	:param retmax: Total number of UIDs from the retrieved set to be shown in the output.

	:returns: a list of sequence identifiers
	"""
	init(email);
	handle = Entrez.esearch(db=database, term=term, retmax=retmax);
	record = Entrez.read(handle);
	return record["IdList"];

def download(database, identifier, file_format, email, retmax):
	"""
	Downloads the data based on sequence identifiers

	:param  database: it's an string that specifies the database where you want to search.	Ex.: "nucleotide"

	:param identifier: it's a string of identifiers separated by commas Ex.: "LC027929,KC470291,FJ237042"

	:param file_format: it's a string that specifies the data format.

	:param email: it's your e-mail address for begining the NCBI connection

	:returns: a handle object
	"""
	init(email)
	handle = Entrez.efetch(db=database, id=identifier, rettype=file_format, retmode="text", retMax = 20)
	return handle

def parse(data,type_file):
	"""
	Parses a handle data.

	:param  data: it's a handle object. (It usually gotten by the download method)

	:param type_file: it's a string that specifies the format of the handle data. Ex.:"genbank" 

	:returns: list of parsed sequnce (SeqIO list)
	"""
	record = list(SeqIO.parse(data, type_file))
	return record

def save(informer,filename,data):
	"""
	Saves the handle data into a file.

	:param  filename: it's the name which we want to save the file.

	:param data: it's a handle data 
	"""	
	if not os.path.isfile(filename):
		out_handle = open(filename, "w")
		out_handle.write(data.read())
		close(out_handle)
		close(data)
		informer.insert(INSERT,"\nSuccessfully saved")

def show_info(records_list):
	"""
	Shows some information of a sequences list like: identifier, sequence and size.

	:param  records_list: a sequences list
	"""
	for i in range(len(records_list)):
		node = records_list[i];
		informer.insert(INSERT,"\nId: " + node.id)
		informer.insert(INSERT,"\nSecuencia: " + repr(node.seq))
		informer.insert(INSERT,"\nTam: " +str(len(node)) + "\n")

def format(records_list):
	"""
	Changes a list of identifier into a string of identifiers separated by commas

	:param record_list: a list of identifier

	:returns: string of identifiers separated by commas 
	"""
	cadena  = ""
	for i in range(len(records_list)):
		cadena = cadena + records_list[i]
		if i+1 != len(records_list):
			cadena = cadena + ","		
	return cadena

def get_ORF(record_list,type_seq,ident):
	"""
	Gets the Open Reading Frame of a sequence.

	:param  record_list: it's a list of sequences (they usually are gotten by parse method)

	:param type_seq: it's an string that specifies the search data. Ex.: "gene"

	:param ident: it's an string that specifies the Open Reading Frame. Ex.: "E6
	
	:returns: Bio.Seq object list
	"""
	dicc = {type_seq : [ident]}
	seq_list = []
	for record in record_list:
		for feature in record.features:
			if feature.qualifiers == dicc:
				pos = str(feature.location)
				match = re.search('<?(\d+):>?(\d+)', pos)
				lower = int(match.group(1))
				uper = int(match.group(2))
				new = record[lower:uper].seq
				#informer.insert(INSERT,"\nLocus: " + record.id + "\n" + str(feature.qualifiers) + "\tLimite inferior: " + str(lower) + "\tLimite superior: " + str(uper))
				#print(new)
				#informer.insert(INSERT,"\n**********************************************************************")
				#new_record = newSequence(new,record.id,record.name,ident,record.dbxrefs)
				new_record = newSequence(new,record.id,record.name,record.description,record.dbxrefs)
				seq_list.append(new_record)
	return seq_list	
				

def newSequence(data,ident,name,description,references):
	"""
	Cretes a new sequence based on the data_sequence input

	:param  data_sequence: a string data

	:returns: a new sequence created based the data_sequence input
	"""
	sequence = SeqRecord(data,ident,name,description,references)
	return sequence

def writeFile(sequence_list,file_name,file_format):
	"""
	Saves a SeqRecord list into a file.
	
	:param  sequence_list: SeqRecord list

	:param filename: a string that specifies the filename

	:param format: a string that specifies the format of the file. 
	
	:returns: a filename as String
	"""
	try:
		fasta_filename = file_name + "." + file_format;
		print fasta_filename
		SeqIO.write(sequence_list, fasta_filename, file_format)
		return fasta_filename
	except:
		print "Error writing the file"

def is_empty(record_list):
	"""
	Checks if a list is empty.

	:param  record_list: a list

	:returns: a boolean (TRUE if is empty and False if it's not).
	"""
	if len(record_list) == 0:
		return True
	else:
		return False
	
def downloadSequences(informer,database, term, file_name, file_format, email, saving_path, retmax = 20):
	"""Searches and downloads sequences by the term and database. 

	:param informer: Tkinter Text Object

	:param database: specifies the NCBI database. It's a String.

	:param term: a sercheable term in NCBI. It's a String.

	:param file_name: a string that specifies the filename

	:param file_format: a string that specifies the file format

	:param email: it's your e-mail address for begining the NCBI connection
	
	:param saving_path: the directory path where the file will be saved. It's a String.

	:param retmax: maximum number of downloaded sequences.
	
	:returns: the absolute file path where they were saved.
	"""
	informer.insert(INSERT,"\nSearching ...");
	records = search(database, term, email, retmax);
	informer.insert(INSERT,"\nSearch finished");
	if len(records) != 0:
		informer.insert(INSERT,"\nDownloading " + str(len(records)) + " sequences ...");
		records_str = format(records);
		record_handler = download(database, records_str, file_format, email, retmax);
		file_name_extension = file_name + '.' + file_format;
		if not os.path.exists(saving_path):
			os.makedirs(saving_path);
		if not os.path.exists(saving_path + "/" + file_name):
			os.makedirs(saving_path + "/" + file_name);
		saving_path += "/" + file_name + "/" + file_name_extension;
		save(informer,saving_path, record_handler);
		informer.insert(INSERT,"\nSequences stored in file " + saving_path + "\n");
	return saving_path;

def save_new_file(informer,filename,data):
	"""
	Saves String data into a file.
	
	:param informer: Tkinter Text Object

	:param filename: a string that specifies the filename

	:param data: contains the information that will be saved. It's a String.
	"""
	try:
		file_in = open(filename, "w")
		file_in.write(data)
		file_in.close()
	except:
		informer.insert(INSERT,"\nError saving " + filename + "\n");







