import os
import re
from Bio import AlignIO
from Bio import Phylo
from Bio.Align.Applications import MuscleCommandline
from Bio.Align.Applications import ClustalwCommandline

"""Generates the aling file (*.aln) and the PhyloTree file (*.dnd) using ClustalW
	INPUTS: input_file --> it's the name of a FASTA sequence(s) file.	Ex.:"opuntia.fasta"
					path-->it's the ubication of ClustalW CommanLine Ex.:"/home/user/Desktop/clustalw2"""
def clustal_align(input_file,path):
	assert os.path.isfile(path), "Clustal W executable missing"
	cline = ClustalwCommandline(path, infile=input_file)
	cline()

"""Generates the aling file (*.aln) compatible with ClustalW using Muscle
	INPUTS: input_file --> it's the name of a FASTA sequence(s) file.	Ex.:"opuntia.fasta"
					output_file --> it's the file name used for the MULSCLE output with "aln" extension. 	Ex.:"opuntia.aln""""
def muscle_align(input_file,output_file):
	cline = MuscleCommandline(input=input_file, out=output_file,clw=True)
	cline()

"""Shows the synthesized aling conteined in the input file
	INPUTS: input_file --> it's the name of a alignment file. Ex.: "opuntia.aln"
					file_type --> it's an string refering to the file type. Ex.: "fasta""""
def show_align(input_file,file_type):
	align = get_align(input_file,file_type)
	print(align)

"""Shows the complite aling conteined in the input file 
	INPUTS: input_file --> it's the name of a alignment file. Ex.: "opuntia.aln"
					file_type --> it's an string refering to the file type. Ex.: "fasta""""
def show_complite_align(input_file,file_type):
	align = get_align(input_file,file_type)
	for record in align:
		print("%s - %s \n" % (record.seq, record.id))

"""Gets the aling data form the input file
	INPUTS: input_file --> it's the name of a alignment file. Ex.: "opuntia.aln"
					file_type --> it's an string refering to the file type. Ex.: "fasta"""
def get_align(input_file,file_type):
	align = AlignIO.read(input_file, file_type)
	return align

"""Shows the tree based in PhyloTree file (*.dnd) 
	INPUTS: input_file --> it's the name of a PhyloTree file. Ex.: "opuntia.dnd""""
def show_tree(input_file):
	tree = Phylo.read(input_file, "newick")
	Phylo.draw_ascii(tree)

"""Gets the Open Reading Frame of a sequence.
	INPUTS: record_list --> it's a list of sequences (they usually are gotten by parse method)
					type_seq --> it's an string that specifies the search data. 		Ex.: "gene"
					ident --> it's an string that specifies the Open Reading Frame.		Ex.: "E6""""
def get_ORF(record_list,type_seq,ident):
	dicc = {type_seq : [ident]}
	for record in record_list:
		for feature in record.features:
			if feature.qualifiers == dicc:
				pos = str(feature.location)
				match = re.search('(\d+):(\d+)', pos)
				lower = int(match.group(1))
				uper = int(match.group(2))
				print("Locus: " + record.id + "\n" + str(feature.qualifiers) + "\tLimite inferior: " + str(lower) + "\tLimite superior: " + str(uper))
				print(record[lower:uper].seq)
				print("**********************************************************************")

	
	


