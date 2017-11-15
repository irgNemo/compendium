TITLE = 'COMPENDIUM GENERATOR'
DEFAULT_SELECTED_FILE = 'select a file in the file menu'
DEFAULT_SEARCH_CONCEPT = "type a concept to look for ..."
DEFAULT_MAIL = 'kavilac@gmail.com'
DEFAULT_TERM = 'Human Papillomavirus type 18 complete genome isolate'
FEATURE_NAME_OPTIONS = ['CDS']#['CDS','gene','source']
FEATURE_TAG_OPTIONS = ["gene product","gene","product"]#['gene','product','translation', 'codon_start','protein_id']
FEATURE_TAG_OPTIONS_PER_SEQ =["product"]#,"gene"]
DATABASES = [  'nucleotide','protein','structure', 'genome','cdd', 'gap','gene',
'genomeprj','homologene','ncbisearch','taxonomy']
FORMATS = ['gb','fasta']
ALIGNERS_OPTIONS = ["clustalW", "Muscle"]
FASTA_EXTENSION  = "fasta"
ALING_EXTENSION = "aln"
ALINGING_EXTENSION  = ".aln"
PHILO_EXTENSION = ".dnd"
IMAGE_EXTENSION = ".jpg"
GENBANK_EXTENTION = "gb"
GENBANK_FILE_TYPE = "genbank"
DOT = '.'
FOLDER_POINTER = "./"
NEW_LINE = '\n'
EMPTY_STRING = ""
EMPTY_SEARCH = "Supplied id parameter is empty."
EMPTY_LIST = []
PREFIX_CONSENSUS = "_consensus_th"
FOLDER_SETTINGS_FILENAME = ".main_folder"
PRIMERS_INPUT_FILENAME = '_primers_input'
PREFIX_PRIMERS = "_primers_"
PREFIX_PHILO = "_tree_"
OS_LINUX = "linux"
OS_LINUX_SLASH = "/"
OS_WIN_SLASH = "\\"
CLUSTALW_LINUX_PATH = "../aligners/clustalw/linux/clustalw2"
CLUSTALW_MAC_PATH = "../aligners/clustalw/darwin/clustalw2"
IO_ERROR = '\nSorry! There is an IO error'
ERROR_EMPTY_FILE = 'Sorry! The file is empty. We can not work with it'
ERROR_FOLDER_NAME = 'Sorry! There is no selected folder'
ERROR_MAIL = '\nSorry! There is an error in the email writing'
ERROR_FOLDER_NAME = "\nSorry! The folder name can not be empty"
ERROR_FILE_NAME = "\nSorry! The file name can not be empty"
ERROR_RETMAX = '\nSorry! Retmax should be a number'
ERROR_PROCESSING = '\nSorry! We could not process your petition!'
ERROR_FILTER_ENABLE = '\nSorry! You should check the filter checkbox'
ERROR_SELECTED_FILE = '\nSorry! You should select a file'
ERROR_TAGS_VALUES = '\nSorry! Tags values can not be empty'
ERROR_FILTERING = '\nSorry! We could not find tags values in your sequence data'
ERROR_SETTINGS = '\nSorry! There is a problem with your settings. Please check them.'
ERROR_PHILO = '\nPhilo Tree Error!'
ERROR_CONSENSUS = '\nConsensus Sequence Error!'
ERROR_FILE_LIST = '\nSorry! There is no filename list'
ERROR_PRIMERS = '\nPrimers Error!'
ERROR_NO_PRIMERS = '\n\nSorry! There are not primer data using the selected parameters in: '
ERROR_NO_FILE = '\nThere is not data generated about '
ERROR_CHECKBOX_NEEDED = '\nYou should check the corresponding checkbox: '
EMPTY_DOWNLOAD = '\nWe could not find any sequence using the given term!'
WARNING_CONSENSUS = '\n You should select a file with aln extension'


LOAD_SETTINGS_MSJ = '\nLoading settings ...'
CLUSTALW_SETTINGS_MSJ = '\nGetting ClustalW path ...'
SELECTED_FILE_WARNING = '\nWarning! There is no selected file'
FOLDER_SETTINGS_MSJ = '\nYour Settings are:\n\nMain folder:\n'
AUTOMATIC_SETTINGS_MSJ = '\nThe automatic enable button is:'
DEFAULT_SETTINGS_MSJ = '\nThe default enable button is:'
WORKING_FOLDER_MSJ = '\nWorking folder:\n'
SAVING_CONSENSUS_MSJ = '\nSaving consensus...'
CLUSTAL_ALING_MSJ = '\n\nAligning with ClustalW...'
MUSCLE_ALING_MSJ = '\nAligning with Muscle...'
PHILO_MSJ = '\n\nGetting phylo tree ...'
ALIGN_DATA_MSJ = '\nGetting align data...'
CONSENSUS_MSJ = '\n\nGetting consensus sequence...'
PROCESS_FINISHED_MSJ = '\n\n*****This process was finished*****\n\n'

REPORTS_FRAME_SIZE ='350x180'
PRIMERS_OUTPUT_FILE_MIN_SIZE = 200
INICIAL = 0
SIZE = '1200x600'
SEARCH_FRAME_SIZE = '900x150'
TOP_PANEL_MAINWINDOW_HEIGHT = 50
TOP_PANEL_TAB_HEIGHT = 50
CLUSTAL_PANEL_HEIGHT = 10
TOP_PANEL_SEARCH_FRAME_HEIGHT = 50
PANELS_EXPAND = 1
LBL_SELECTED_FILE_X = 100
LBL_SELECTED_FILE_Y = 16
MENU_TEAROFF = 0
INFORMER_HEIGHT = 41
INFORMER_WIGTH = 40
DEFAULT_TAB_INFORMERS_HEIGHT = 20
DEFAULT_TAB_INFORMERS_WIGTH = 125
ALIGN_INFORMER_HEIGHT = 30
ALIGN_INFORMERS_WIGTH = 125
PRIMERS_INFORMER_HEIGHT = 22
PRIMERS_INFORMERS_WIGTH = 125
BLAST_INFORMER_HEIGHT = 30
BLAST_INFORMERS_WIGTH = 125
TABS_WIDTH = 900
TABS_HEIGHT = 550
LEFT_PADDING = 10
TOP_PADDING = 0
RIGHT_PADDING = 10
BOTTOM_PADDING = 15
CHKBOX_OFF = 0
CHKBOX_ON = 1
INDEX_CLUSTALW = 0
INDEX_FILTER_TAB = 0
INDEX_ALIGNMENT_TAB = 1
INDEX_PRIMERS_TAB = 2
INDEX_BLAST_TAB = 3
INDEX_REPORTS = 4
BLANK_SPACE_X = 80
BLANK_SPACE_Y = 20
DEFAULT_TXTBOX_HEIGHT = 1
TXTBOX_MAIL_WIGTH = 54
TXTBOX_TERM_WIGTH = 110
TXTBOX_RETMAX_WIGTH = 10
TXTBOX_FILENAME_WIGTH = 30
TXTBOX_FOLDER_WIGTH = 30
TXTBOX_FEATURE_NAME_WIGTH = 40
TXTBOX_FEATURE_TAG_WIGTH = 40
TXTBOX_TAG_VALUES_WIGTH = 30
TXTBOX_THRESHOLD_WIGTH = 10
TXTBOX_PRIMER_SIZE_WIGTH = 10
TXTBOX_THRESHOLD_WIGTH = 10
"""
##PRIMERS PREFIX
PREFIX_PRIMER_NUMBER = "PRIMER_NUM_RETURN"
#PREFIX_MAX_SELF_COMPLEMENTARY = PRIMER_PAIR_MAX_COMPL_END
PREFIX_SALT_MONOVALENT = "PRIMER_SALT_MONOVALENT"
PREFIX_PRODUCT_RANGE = "PRIMER_PRODUCT_SIZE_RANGE"
PREFIX_MAX_3_STABILITY = "PRIMER_MAX_END_STABILITY "
#PREFIX_MAX_3_SELF_COMPLEMENTARY =
PREFIX_PRIMER_MIN_SIZE = "PRIMER_MIN_SIZE"
PREFIX_PRIMER_OPT_SIZE = "PRIMER_OPT_SIZE"
PREFIX_PRIMER_MAX_SIZE = "PRIMER_MAX_SIZE"
PREFIX_PRIMER_MIN_TM = "PRIMER_MIN_TM"
PREFIX_PRIMER_OPT_TM = "PRIMER_OPT_TM"
PREFIX_PRIMER_MAX_TM = "PRIMER_MAX_TM"
PREFIX_PRIMER_MIN_GC = "PRIMER_MIN_GC"
PREFIX_PRIMER_MAX_GC = "PRIMER_MAX_GC"
PREFIX_PRIMER_SEQ_TARGET = "SEQUENCE_TARGET"
PREFIX_MAX_POLY_X = "PRIMER_MAX_POLY_X"



##PRIMER DEFAULT VALUES
PRIMER_NUMBER = 5
#MAX_SELF_COMPLEMENTARY = DUDA
SALT_MONOVALENT = 50.0
PRODUCT_RANGE = "100-300"
#MAX_3_STABILITY = DUDA
#MAX_3_SELF_COMPLEMENTARY = DUDA
PRIMER_MIN_SIZE = 15
PRIMER_OPT_SIZE = 18
PRIMER_MAX_SIZE = 21
PRIMER_MIN_TM = 57.0
PRIMER_OPT_TM = 60.0
PRIMER_MAX_TM = 63.0
PRIMER_MIN_GC = 20.0
PRIMER_MAX_GC = 80.0
PRIMER_SEQ_TARGET = "37,21"
MAX_POLY_X = 5
"""





















