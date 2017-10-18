import threading
from Tkinter import *
from ttk import *
from basic_tab import *
from gui_constans import *
from gui_utils import *
import sys
sys.path.append("../")
from src.utils import *;
from src.Petitions import *;
from src.Alignments import *;
from src.constans import *;

filename = "/home/karla/Escritorio/mis_repositorios/compendium/gui/out/hpv_tipo_18/hpv_tipo_18_E7.aln"
threshold = 0.6
alinging_format='fasta'
print ("Getting  consensus ...")
#Obteniendo MultipleSeqAlignment object
alignment = get_align(filename, "clustal")
print filename
#Obteniendo secuencia consenso
consensus_seq_record = SeqRecord(get_consensus(alignment,threshold), id ="hpv_tipo_18" , description = " Consensus sequence ")
print ("Saving  consensus ...");
writeFile(consensus_seq_record,filename + "_consensus_", alinging_format)
