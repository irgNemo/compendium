import re;
# Agregar un campo para pasar el valor de CDS
# Agregar la posibilidad de que se se llame 'gene' or 'product'
def validateORFs(record_list, type_seq, idents):
	for record in record_list:
		print ("--------------------\n");
		print (record.name);
		for feature in record.features:
			if feature.type == 'CDS':
				qualifiers = feature.qualifiers;
				qualifiersStr = '|'.join(qualifiers.keys());
				m = re.search(type_seq,qualifiersStr);
				if m is not None:
					#print(m.group(0))
					str = "|".join(qualifiers[m.group(0)]);	
					#print(str);
					m2 = re.match(idents,str);
					if m2 is not None:
						print(m2.group());	 
