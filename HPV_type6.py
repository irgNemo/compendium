from Petitions import *
from Alignments import *

######Descargando archivo de Human papillomavirus
correo = "kavilac@gmail.com"
database = "nucleotide"
term = "Human Papillovamirus type 6 isolate"
print("Buscando . . .")
lista_records = search(database,term,correo)
identificadores = format(lista_records)
print("Descargando . . .")
mi_handle = download(database,identificadores,"gb",correo)
archivo = "hpv_6.gb"
save(archivo,mi_handle)
print("Guardando . . .")
######Valor en memoria:
my_record = parse(archivo,"gb")
print("Obteniendo ORF . . .")
mi_lista = get_ORF(my_record,"gene","E6")
archivoListo = "virusE6.fasta"
print("Guardando . . .")
writeFile(mi_lista,archivoListo,"fasta")
print("Alineando . . .")
clustalw2_path = "/home/karla/Desktop/ejemplos_biopython/biopython/clustalw2"
clustal_align(archivoListo,clustalw2_path)
show_align("virusE6.aln","clustal") #Mostrar alineamiento"""
show_tree("virusE6.dnd")
	



		
