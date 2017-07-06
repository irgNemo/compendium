from reportlab.pdfgen import canvas;
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from Alignments import *;

TREE_TITLE = "Multiple Sequence Alignment tree"
CONSENSUS_TITLE = "Consensus sequence"
PRIMERS_TITLE = 'Primers data'
CONSENSUS_X = 50
CONSENSUS_Y = 760
PRIMERS_X = 50
PRIMERS_Y = 760
TEXT_ORIGIN_X = 30
TEXT_ORIGIN_Y = 785
TITLE_X = 30
TITLE_Y = 800
FONT = 'Courier'
FONT_SIZE = 10
TRIM = 2
IMAGE_ORIGIN_X = 10
IMAGE_ORIGIN_Y = 300
SCALE = 0.70
PAGE_LIMIT = 47
LINE_LIMIT = 80
POS_TABS = 247
"""Creates a new canvas page
	INPUTS: canvas --> canvas object"""
def new_page(canvas):
	canvas.showPage()

"""Creates a  new ReportLab text object
	INPUTS: data--> it's a string 
			canvas --> A ReportLab canvas
			pos_x --> It's the x position where the text is gonna be written
			pos_y --> It's the y position where the text is gonna be written
	OUTPUTS: textobject --> A ReportLab text object"""
def new_textobject(data,canvas,pos_x,pos_y):
	textobject = canvas.beginText()
	textobject.setTextOrigin(pos_x,pos_y)
	textobject.setFont(FONT,FONT_SIZE)
	textobject.textLines(data,TRIM)
	return textobject

"""Splits and adds the alignment data into the report
	INPUTS: canvas--> A ReportLab canvas
			title--> A string that describes the report section at the page's beginning
			data--> Alignment data to be save as MultipleSeqAlignment
			page_limit--> Integer that defines the number of new lines per page"""
def add_split_data(canvas,title,data,page_limit=PAGE_LIMIT):
	data_list = data.split('\n')
	data_list_lenght = len(data_list)
	i = 0	
	x = TEXT_ORIGIN_X
	y = TEXT_ORIGIN_Y
	for i in range(data_list_lenght):
		canvas.drawText(new_textobject(title,canvas,TITLE_X,TITLE_Y))
		string = data_list[i] + '\n'
		if string.find('*') != -1:
			x = POS_TABS
			canvas.drawText(new_textobject(string,canvas,x,y))
			x = TEXT_ORIGIN_X
		else:
			canvas.drawText(new_textobject(string,canvas,x,y))
		y = y - 15
		if i % page_limit == 0 and i != 0:
			canvas.showPage()
			y = TEXT_ORIGIN_Y
	canvas.showPage()

"""Adds an image into the report
	INPUTS: canvas--> A ReportLab canvas
			title--> A string that describes the report section at the page's beginning
			image--> It's the Image filename
			scale--> A number that defines the image scale. Default is 0.7 that means 70% of the original image size"""
def add_image(canvas,title,image,scale=SCALE):
	canvas.drawText(new_textobject(title,canvas,TITLE_X,TITLE_Y))
	w, h = ImageReader(image).getSize()
	canvas.drawInlineImage(image,IMAGE_ORIGIN_X,IMAGE_ORIGIN_Y,w * scale,h * scale)
	canvas.showPage()

"""Adds the consensus sequence data into the report
	INPUTS: canvas--> A ReportLab canvas
			title--> A string that describes the report section at the page's beginning
			data--> Consensus sequence data to be save as Seq Object
			page_limit--> Integer that defines the number of new lines per page
			line_limit-->Integer that defines the number of characters contained in each line"""
def add_consensus(canvas,title,data,page_limit=PAGE_LIMIT,line_limit=LINE_LIMIT):
	data_lenght = len(data)
	i = 0
	j = 0
	y = CONSENSUS_Y
	x = CONSENSUS_X
	string = ""
	canvas.drawText(new_textobject(title,canvas,TITLE_X,TITLE_Y))
	for i in range(data_lenght):
		string = string + data[i]
		if i % line_limit == 0 and i != 0:
			canvas.drawText(new_textobject(string,canvas,x,y))			
			y = y - 15
			string = ""
			j = j + 1
		if j % page_limit == 0 and j != 0:
			canvas.showPage()
			canvas.drawText(new_textobject(title,canvas,TITLE_X,TITLE_Y))
			y = CONSENSUS_Y
			j = 0
	
"""Generates a pdf report based on the alignment, consensus sequence and the philo tree
	INPUTS: data--> alignment data
			consensus_data --> consensus sequence by Seq object
			image_name--> It's the image filename
			file_name--> A string that specifies the report filename"""
def generate_report(data,consensus_data,image_name,primers_data,file_name):
	c = canvas.Canvas(file_name)
	title,align = data.split("alignment")
	title = title + "alignment"
	add_split_data(c,title,align)
	add_image(c,TREE_TITLE,image_name)
	add_consensus(c,CONSENSUS_TITLE,consensus_data)
	new_page(c)
	add_split_data(c,PRIMERS_TITLE,primers_data)
	c.save()	

