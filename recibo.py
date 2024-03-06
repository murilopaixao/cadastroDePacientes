from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

pdf = canvas.Canvas('./tmp/Recibo01.pdf', pagesize=A4)

pdf.drawString(250, 750, 'RECIBO')

pdf.save()