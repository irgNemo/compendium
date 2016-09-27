from Petitions import *
from Alignments import *
from Bio.Align.Applications import ClustalwCommandline
def main():
	clustal_align("opuntia.fasta")
	#show_align("opuntia.aln") #Mostrar alineamiento
	#show_tree("opuntia.dnd")
if __name__ == "__main__":
	main()
