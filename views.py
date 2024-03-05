from flask import render_template, request, redirect, url_for, jsonify, make_response
from app import app
from datetime import date

import json
import banco

@app.route('/')
def index():
    pacientes = banco.todos()
    
    return render_template('index.html', pacientes=pacientes)

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

    return render_template('visualizar.html', paciente=paciente)

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
    numero = request.form['numero']
    complemento = request.form['complemento'].strip()
    dataNascimento = request.form['dataNascimento'].strip()
    genero = request.form['genero'].strip()
    cpf = request.form['cpf'].strip()
    banco.alterar(id, nome, email, fone, cep, endereco, bairro, numero, complemento, dataNascimento, genero, cpf)
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
    
    banco.inserir(nome, email, fone, cep, endereco, bairro, numero, complemento, dataNascimento, genero, cpf)

    return redirect('/')

@app.route('/teste')
def teste():
    banco.inserirTeste()
    return redirect('/')