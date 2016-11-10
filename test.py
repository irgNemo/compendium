#! /usr/bin/env python3
from utils import *;
from Petitions import *;

def main():
	email = "irg_nemo@hotmail.com";
	database = "nucleotide";
	file_format = "gb"
	file_name = "hpv_type6"
	term = "Human Papillomavirus type 6 complete genome isolate";
	file_name_extension = file_name + "." + file_format;
	#print("Searching...");
	#records = search(database, term, email);
	#identificadores = format(records);
	#print("Descargando " + str(len(records)) + " secuencias ....");
	#handler = download(database, identificadores, file_format, email);
	#save(file_name_extension, handler);
	records = parse(file_name_extension, file_format);
	print("Calculando estadisticas ...");
	sequences_filtered = validateORFs(records, "CDS", "gene|product", "E6|E7");
	print("Longitud leidos :" + str(len(records)));
	print("Longitud filtrados :" + str(len(sequences_filtered)));


if __name__ == "__main__":
	main();

