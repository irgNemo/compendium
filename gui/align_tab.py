from Tkinter import *
from ttk import *
from basic_tab import *
from gui_constans import *
from gui_utils import *
import sys
sys.path.append("../")
from src.utils import *;
from src.Petitions import *;
from src.constans import *;

class Align_tab(Basic_tab):
	def __init__(self,tab):
		Basic_tab.__init__(self,tab,DEFAULT_TAB_INFORMERS_HEIGHT,DEFAULT_TAB_INFORMERS_WIGTH)
		self.y = 2

	def adios(self):
		self.println(self.get_informer(),"hola")
