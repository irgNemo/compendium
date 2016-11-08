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
	validateORFs(records, "gene|product", "E6|E7");


if __name__ == "__main__":
	main();

