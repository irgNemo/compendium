from reportlab.pdfgen import canvas

def pdf_save(data,file_name):
	c = canvas.Canvas(file_name)
	c.drawString(0,800,data)
	c.showPage()
	c.save()
