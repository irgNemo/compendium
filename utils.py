import re;
def filterByNCBITagValue(sequence_records, feature_name, feature_tag, tag_value):
	sequences_filtered = [];
	feature_tag_regex = '(' + '|'.join(feature_tag) + ')'; # Se construye la expresion regular para no dejar la responsabilidad al usuario.
	tag_value_regex = '(' + '|'.join(tag_value) + ')'; # Se construye la expresion regular para no dejar la responsabilidad al usuario
	for record in sequence_records:
		tag_value_found = "";
		for feature in record.features:
			n = re.search(feature_name,feature.type);
			if n is not None:
				qualifiers = feature.qualifiers;
				qualifiersStr = ','.join(qualifiers.keys());
				m = re.search(feature_tag_regex, qualifiersStr);
				if m is not None:
					tag_value_found += ','.join(qualifiers[m.group(0)]) + ',';
		values_found = re.findall(tag_value_regex, tag_value_found);
		save = True;
		for value in tag_value:
			save = save and (value in values_found);
		if save :
			sequences_filtered.append(record);
	return sequences_filtered; 
