from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def gerarPdf(nomePaciente,dataRecibo,valorRecibo):

    profissional='Dr. Tarsila do Amaral'

    def mm2p(milimetros):
        return milimetros / 0.352777

    pdf = canvas.Canvas('./tmp/Recibo01.pdf', pagesize=A4)
    pdf.setTitle("Recibo")
    
    pdf.rect(mm2p(20),mm2p(140),mm2p(160),mm2p(130))
    pdf.drawImage("static/logo.png", mm2p(25), mm2p(240), width=50, height=50)
    pdf.drawString(mm2p(50), mm2p(250), profissional)
    pdf.drawString(mm2p(50), mm2p(245), 'Psicóloga')
    pdf.drawString(mm2p(50), mm2p(240), 'CRP 00/0000')

    pdf.setFont("Helvetica", 20)
    pdf.drawString(mm2p(25), mm2p(230), 'RECIBO')
    pdf.setFont("Helvetica", 10)
    pdf.drawString(mm2p(150), mm2p(230), 'R$ ' + str(valorRecibo))

    pdf.drawString(mm2p(25), mm2p(220), 'Recebi(emos) de : ' + nomePaciente)
    pdf.drawString(mm2p(25), mm2p(210), 'a importância de ')
    pdf.drawString(mm2p(25), mm2p(200), 'Proveniente de ')
    pdf.drawString(mm2p(25), mm2p(190), 'para clareza formo(amos) o presente. ')
    pdf.drawString(mm2p(140), mm2p(180), dataRecibo)

    pdf.drawString(mm2p(90), mm2p(165), '____________________________________')
    pdf.drawString(mm2p(110), mm2p(160), profissional)

    pdf.save()
