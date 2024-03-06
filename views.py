from flask import render_template, request, redirect, send_file, url_for
from app import app
from datetime import date
import banco
import recibo

@app.route('/')
def index():
    pacientes = banco.todos()
    
    return render_template('index.html', pacientes=pacientes)

@app.route('/teste')
def teste():
    teste = banco.testeLeft()
    for x in teste:
        print(x)
    return render_template('teste.html')

@app.route('/inicio')
def inicio():
    banco.inicio()
    return redirect('/')

@app.route('/novo')
def novo():
    return render_template('novo.html')

@app.route('/visualizar/<id>')
def visualizar(id):
    paciente = banco.selectOne(id)
    historico = banco.historicoFinanceiroSelAll(id)

    return render_template('visualizar.html', paciente=paciente, historico=historico)

@app.route('/editar/<id>')
def editar(id):
    paciente = banco.selectOne(id)

    return render_template('editar.html', paciente=paciente)

@app.route('/alterar', methods=['POST'])
def alterar():
    id = request.form['id']
    nome = request.form['nome'].strip()
    email = request.form['email1'].strip()
    fone = request.form['fone'].strip()
    cep = request.form['cep'].strip()
    endereco = request.form['endereco'].strip()
    bairro = request.form['bairro'].strip()
    cidade = request.form['cidade'].strip()
    estado = request.form['estado'].strip()
    numero = request.form['numero']
    complemento = request.form['complemento'].strip()
    dataNascimento = request.form['dataNascimento'].strip()
    genero = request.form['genero'].strip()
    cpf = request.form['cpf'].strip()

    if (numero == ""):
        numero = 'NULL'
    if (nome == ""):
        print("Nome não foi preenchido")
        return redirect('/')
    
    banco.alterar(id, nome, email, fone, cep, endereco, bairro, numero, complemento, dataNascimento, genero, cpf, cidade, estado)
    
    return redirect('/')

@app.route('/deletar', methods=['POST'])
def deletar():
    id = request.form['id']
    banco.deletar(id)
    return redirect('/')

@app.route('/inserir', methods=['POST'])
def inserir():    
    nome = request.form['nome'].strip()
    email = request.form['email1'].strip()
    fone = request.form['fone'].strip()
    cep = request.form['cep'].strip()
    endereco = request.form['endereco'].strip()
    bairro = request.form['bairro'].strip()
    cidade = request.form['cidade'].strip()
    estado = request.form['estado'].strip()
    numero = request.form['numero']
    complemento = request.form['complemento'].strip()
    dataNascimento = request.form['dataNascimento'].strip()
    genero = request.form['genero'].strip()
    cpf = request.form['cpf'].strip()

    if (numero == ""):
        numero = 'NULL'
    if (nome == ""):
        print("Nome não foi preenchido")
        return redirect('/')
    
    banco.inserir(nome, email, fone, cep, endereco, bairro, numero, complemento, dataNascimento, genero, cpf, cidade, estado)

    return redirect('/')

@app.route('/gerarRecibo', methods=['POST'])
def gerarRecibo():
    idPaciente = request.form['idPaciente']
    nomePaciente = request.form['nomePaciente']    
    dataRecibo = request.form['dataRecibo'].strip()
    valorRecibo = request.form['valorRecibo']

    banco.historicoFinanceiroAdd(idPaciente, dataRecibo, valorRecibo)
    recibo.gerarPdf(nomePaciente,dataRecibo,valorRecibo)
    #return redirect('/visualizar/'+str(idPaciente))
    return redirect('/download')
    
@app.route('/historicoFinanceiroDel/<id>')
def historicoFinanceiroDel(id):
    idPaciente = banco.historicoFinanceiroSelUnit(id)

    banco.historicoFinanceiroDel(id)
    return redirect('/visualizar/'+str(idPaciente[0][0]))

@app.route('/download')
def download():
     return render_template('download.html')

@app.route('/download2')
def download2():
    p = "./tmp/Recibo01.pdf"
    return send_file(p,as_attachment=True)