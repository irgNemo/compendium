#!/usr/bin/env python
from utils import *;
from Petitions import *;
from Alignments import *;

def main():
	# Configuration parameters
	clustalw2_path = "./aligners/clustalw/clustalw2";
	sequence_file_path = "";
	alignment_file_name = "";
	tree_file_name = "";
	database = "nucleotide";
	email = "irg_nemo@hotmail.com";
	file_format = "gb";
	file_name = "hpv_type6";
	term = "Human Papillomavirus type 6 complete genome isolate";

	#downloadSequences(database, term, file_name, file_format, email);
	alignSequences(file_name, file_format, clustalw2_path);

def downloadSequences(database,term, file_name, file_format, email):
	print ("Searching ...");
	records = search(database, term, email);
	print("Search finished");
	print("Downloading " + str(len(records)) + " sequences ...");
	records_str = format(records);
	record_handler = download(database, records_str, file_format, email);
	file_name_extension = file_name + '.' + file_format;
	save(file_name_extension, record_handler);
	print("Sequences stored in file " + file_name_extension);
	return 1;
	
def alignSequences(file_name, file_format, aligner_path):

	records = parse(file_name + '.' + file_format, file_format);
	selected_records = get_ORF(records, 'gene', 'E6');
	output_fasta_file = file_name + '.' + 'fasta'; # Eliminar el archivo del disco 
	clustal_align(output_fasta_file, clustalw2_path);
	show_align(file_name + '.' + 'aln', 'clustal');
	show_tree(file_name + '.' + 'dnd');
	return 1;
	

	

if __name__ == "__main__":
	main();


