from reportlab.pdfgen import canvas;
from reportlab.lib.pagesizes import letter;
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

def pdf_save(data,file_name):
	#c = canvas.Canvas(file_name, pagesize=letter);
	#c.drawString(100,750,data);
	#c.showPage();
	#c.save();
	Story=[];
	doc = SimpleDocTemplate(file_name, pagesize=letter,
                        rightMargin=72, leftMargin=72,
                        topMargin=72, bottomMargin=18);
	content = [];
	styles = getSampleStyleSheet()
	styles.fontsize = 18;
	styles.fontName = 'Helvetica'
	ptext = data;
	paragraphStyle = Paragraph(ptext, styles["Normal"]);
	Story.append(paragraphStyle);
	doc.build(Story);
		
