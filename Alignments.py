import os
from Bio import AlignIO
from Bio import Phylo
from Bio.Align.Applications import MuscleCommandline
from Bio.Align.Applications import ClustalwCommandline

def clustal_align(input_file,path):
	assert os.path.isfile(path), "Clustal W executable missing"
	cline = ClustalwCommandline(path, infile=input_file)
	cline()
	
def show_align(input_file):
	align = get_align(input_file)
	print(align)
	
def get_align(input_file):
	align = AlignIO.read(input_file, "clustal")
	return align
		
def show_tree(input_file):
	tree = Phylo.read(input_file, "newick")
	Phylo.draw_ascii(tree)
	



