import re;
def validateORFs(sequence_records, feature_to_filter, feature_tag, tag_value):
	sequences_filtered = [];
	for record in sequence_records:
		print ("--------------------\n");
		print (record.name);
		for feature in record.features:
			if re.search(feature_to_filter, feature.type) is not None:
				qualifiers = feature.qualifiers;
				qualifiersStr = '|'.join(qualifiers.keys());
				m = re.search(feature_tag, qualifiersStr);
				if m is not None:
					str = "|".join(qualifiers[m.group(0)]);	
					m2 = re.match(tag_value,str);
					if m2 is not None:
						sequences_filtered.append(record);	
						print(m2.group());
	return sequences_filtered; 
