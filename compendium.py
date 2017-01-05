#!/usr/bin/env python3
from utils import *;
from Petitions import *;
from Alignments import *;
from Bio import Phylo;
from Bio import AlignIO;
from IO import *;

def main():
	# Configuration parameters
	clustalw2_path = "./aligners/clustalw/linux/clustalw2"; # TODO: cambiar la ruta dependiendo del sistema operativo
	sequence_file_path = "";
	alignment_file_name = "";
	database = "nucleotide";
	email = "irg_nemo@hotmail.com";
	file_format = "gb";
	file_name = "hpv_type6";
	term = "Human Papillomavirus type 6 complete genome isolate";

	#filename_path = downloadSequences(database, term, file_name, file_format, email, "./output");
	filename_path = "./output/hpv_type6/hpv_type6.gb"
	fasta_filename = filterSequences(filename_path, file_format, "CDS", ['gene', 'product'], ['E6']); 
	clustal_align(fasta_filename, clustalw2_path); # TODO: Agregar una barra de avance para saber si esta trabajando o no, se podra?
	alignment = get_align(filename_path + '.aln', 'clustal');
	strAlignment = alignment.format("clustal");
	strTree = tree_to_str(filename_path + '.dnd'); # TODO: Ver como podemos imprimir el arbol, puede ser una imagen y ponerla en el documento
	pdf_save(strAlignment, filename_path + ".pdf"); 

def downloadSequences(database,term, file_name, file_format, email, saving_path):
	print ("Searching ...");
	records = search(database, term, email);
	print("Search finished");
	print("Downloading " + str(len(records)) + " sequences ...");
	records_str = format(records);
	record_handler = download(database, records_str, file_format, email);
	file_name_extension = file_name + '.' + file_format;
	if not os.path.exists(saving_path):
		os.makedirs(saving_path);
	if not os.path.exists(saving_path + "/" + file_name):
		os.makedirs(saving_path + "/" + file_name);
	saving_path += "/" + file_name + "/" + file_name_extension;
	save(saving_path, record_handler);
	print("Sequences stored in file " + saving_path);
	return saving_path;
	
def filterSequences(file_name, file_format, feature_name, feature_tag, tag_value):
	records = parse(file_name, file_format);
	records_filtered = filterByNCBITagValue(records, feature_name, feature_tag, tag_value);
	return writeFile(records_filtered, file_name, "fasta");	

if __name__ == "__main__":
	main();


