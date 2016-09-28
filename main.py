from Petitions import *
from Alignments import *
from Bio.Align.Applications import ClustalwCommandline
def main():
	clustalw2_path = "./aligners/clustalw/clustalw2";
	sequences_file_path = "opuntia.fasta";
	clustal_align(sequences_file_path, clustalw2_path);
	show_align("opuntia.aln"); #Mostrar alineamiento
	show_tree("opuntia.dnd");

if __name__ == "__main__":
	main()
