#!/usr/bin/env python3
from utils import *;
from Petitions import *;
from Alignments import *;
from Primers import *;
from Bio import Phylo;
from Bio import AlignIO;
from IO import *;
from time import time;
import sys

PRIMERS_INPUT_FILENAME = 'primers_input'

def main():
	# Configuration parameters
	platform = sys.platform;
	clustalw2_path = "/home/karla/Desktop/mis_repositorios/compendioBioPython/compendium/aligners/clustalw/linux/clustalw2"
	#clustalw2_path = "./aligners/clustalw/" + platform  + "/clustalw2"; # TODO: cambiar la ruta dependiendo del sistema operativo
	sequence_file_path = "";
	alignment_file_name = "";
	database = "nucleotide";
	email = "irg_nemo@hotmail.com";
	tag_values_list = ['E6', 'E7']
	file_format = "gb";
	alinging_format = "fasta"
	output_aling_format = ".aln"
	philo_format = ".dnd"
	image_format = ".jpg"
	file_name = "hpv_type18";
	term = "Human Papillomavirus type 18 complete genome isolate";
	retmax = 50; # Total number of UID from the retrieved set to be shown
	main_folder = "./output/"
	tool = "clustalw"
	threshold = 0.6
	seq_target = '37,21'

	#Buscando y descargando las secuencias correspondientes
	filename_path = downloadSequences(database, term, file_name, file_format, email, main_folder, retmax); 
	#Leyendo secuencias descargadas	
	record = parse(filename_path, file_format);
	#Filtrando secuencias que contengan las secciones buscadas
	records_filtered = filterByNCBITagValue(record, "CDS", ['gene', 'product'], tag_values_list);
	#Filtrando por secciones 
	orfs = separate_ORFs_per_sequence(records_filtered, "CDS", tag_values_list);
	#Generando base para nuevo nombre de archivo filtrado
	new_file_name = main_folder + file_name + "/" + file_name
	#Guardando secciones filtradas 
	for key in orfs.keys():
		writeFile(orfs[key],new_file_name + "_" + key , alinging_format);
	p3_filename = main_folder + file_name
	primers_folder  = 	make_primers_dir(p3_filename)
	print (primers_folder + '\n.............................')
	
	
	"""Procesando ...
		Generando alineamiento, secuencia consenso, arbol filogenetico y primers"""
	for key in orfs.keys():
		print("Aligning sequences " + key +"...");
		initial_time = time(); # Comienza el conteo del tiempo de alineamiento
		#Alineando segun la herramienta seleccionada
		if tool == "muscle":
			muscle_align(new_file_name + "_" + key + "."+ alinging_format, new_file_name + "_" + key + output_aling_format)
			final_time = time(); # Termina el tiempo de alieamiento
		else:
			clustal_align(new_file_name + "_" + key + "." + alinging_format, clustalw2_path);
			print ("Getting " + key + " phylo tree ...")
			aling_tree = get_tree(new_file_name + "_" + key + philo_format)
			tree_filename = new_file_name + "_tree_" + key + image_format
			print ("Saving " + key + " phylo tree ...")
			save_tree(tree_filename,aling_tree)
			final_time = time(); # Termina el tiempo de alieamiento
		# Calculo del tiempo transcurrido
		elapsed_time = final_time - initial_time; 
		print("Alignment " + key + " elapsed time: " + str(elapsed_time));
		print ("Getting " + key + " consensus ...")
		#Obteniendo MultipleSeqAlignment object
		alignment = get_align(new_file_name + "_" + key + output_aling_format, "clustal")
		#Obteniendo secuencia consenso
		consensus_seq_record = SeqRecord(get_consensus(alignment,threshold), id = term + " " +key, description = " Consensus sequence ")
		print ("Saving " + key + " consensus ...")		
		writeFile(consensus_seq_record,new_file_name + "_consensus_" + key, alinging_format)
		
		full_primers_input_filename = primers_folder + PRIMERS_INPUT_FILENAME
		print full_primers_input_filename
		seq_id = primers_folder+ 'primers_' +key
		generate_basic_primers_input(full_primers_input_filename, seq_id, str(consensus_seq_record.seq),seq_target)
		print 'Generated' + key +' primers input file'

		#Generando reporte pdf
		report_filename = new_file_name + "_" + key + ".pdf"
		strAlignment = alignment.format("clustal")
		print report_filename
		generate_report(strAlignment,consensus_seq_record,tree_filename,report_filename)
	
	get_primers(full_primers_input_filename)

if __name__ == "__main__":
	main();



