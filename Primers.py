#Constants
SEQUENCE_ID = "SEQUENCE_ID"
SEQUENCE_TEMPLATE = "SEQUENCE_TEMPLATE"
SEQUENCE_TARGET = "SEQUENCE_TARGET"
PRIMER_PRODUCT_SIZE_RANGE = "PRIMER_PRODUCT_SIZE_RANGE"
P3_FILE_FLAG = "P3_FILE_FLAG=1"
DEFAULT_PRODUCT_SIZE = "100-300"

def generate_primers_input(nombre_arch,seq_id,seq,seq_target,product_size=DEFAULT_PRODUCT_SIZE):
	archivo = open(nombre_arch, 'w')

