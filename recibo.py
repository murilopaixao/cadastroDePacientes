from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def gerarPdf(nomePaciente,dataRecibo,valorRecibo):

    def mm2p(milimetros):
        return milimetros / 0.352777

    pdf = canvas.Canvas('./tmp/Recibo01.pdf', pagesize=A4)

    pdf.drawString(250, 750, 'RECIBO')
    pdf.drawString(150, 550, 'Recebemos do paciente: ' + nomePaciente)
    pdf.drawString(150, 500, 'Na data de: ' + dataRecibo)
    pdf.drawString(150, 450, 'O valor de: ' + str(valorRecibo))

    pdf.save()