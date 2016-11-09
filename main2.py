from Petitions import *
from Alignments import *

######Descargando archivo de Human papillomavirus
correo = "kavilac@gmail.com"
database = "nucleotide"
term = "Papillomaviridae"
seccion = "E2"
print("Buscando . . .")
lista_records = search(database,term,correo)
if is_empty(lista_records):
	print('No se ha encontrado el termino {0} en la base da datos {1}.'.format(term,database))
else:
	identificadores = format(lista_records)
	print("Descargando . . .")
	mi_handle = download(database,identificadores,"gb",correo)
	archivo = "papiloma.gb"
	save(archivo,mi_handle)
	print("Guardando . . .")
	######Valor en memoria:
	my_record = parse(archivo,"gb")
	print("Obteniendo ORF . . .")
	mi_lista = get_ORF(my_record,"gene",seccion)
	if is_empty(mi_lista):
		print('No se ha encontrado la seccion {0} en los datos del termino {1}.'.format(seccion,term))
	else:
		archivoListo = "virusE6.fasta"
		print("Guardando . . .")
		writeFile(mi_lista,archivoListo,"fasta")
		print("Alineando . . .")
		clustalw2_path = "/home/karla/Desktop/ejemplos_biopython/biopython/clustalw2"
		clustal_align(archivoListo,clustalw2_path)
		show_align("virusE6.aln","clustal") #Mostrar alineamiento"""
		show_tree("virusE6.dnd")
	



		
