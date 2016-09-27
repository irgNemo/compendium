import os
from Bio import AlignIO
from Bio import Phylo
#from Bio.Blast import NCBIWWW
#from Bio.Align.Applications import MuscleCommandline
from Bio.Align.Applications import ClustalwCommandline

def clustal_align(input_file):
	#clustalw_exe = "/home/karla/Desktop/ejemplos_biopython/biopython\clustalw2.exe"
	#clustalw_cline = ClustalwCommandline(clustalw_exe, infile=input_file)
	assert os.path.isfile("clustalw2"), "Clustal W executable missing"
	cline = ClustalwCommandline("clustalw2", infile=input_file)
	print(cline)
	
def show_align(input_file):
	align = AlignIO.read(input_file, "clustal")
	print(align)
	
def show_tree(input_file):
	tree = Phylo.read(input_file, "newick")
	Phylo.draw_ascii(tree)
	



