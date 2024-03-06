import sqlite3
import os.path

def conexao(sqlQuery, tipo):
    conexao = sqlite3.connect('cadastro.db')
    cursor = conexao.cursor()
    cursor.execute(sqlQuery)
    
    if (tipo == "altera"):
        conexao.commit()
        conexao.close()
    else:
        paciente = cursor.fetchall()
        conexao.close()
        return paciente

def inicio():
    sqlQuery = 'CREATE TABLE pacientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(50), email VARCHAR(50), fone VARCHAR(50), cep VARCHAR(50), endereco VARCHAR(50), bairro VARCHAR(50), numero INT, complemento VARCHAR(30), dataNascimento VARCHAR(15), genero VARCHAR(20), cpf VARCHAR(20), cidade  VARCHAR(30), estado VARCHAR(2))'
    conexao(sqlQuery,"altera")

def todos():
    sqlQuery = 'SELECT * FROM pacientes'
    pacientes = conexao(sqlQuery,"select")
    
    return pacientes

def selectOne(id):
    sqlQuery = f"SELECT * FROM pacientes WHERE id={id}"    
    paciente = conexao(sqlQuery,"select")
    return paciente

def inserir(nome, email, fone, cep, endereco, bairro, numero, complemento, dataNascimento, genero, cpf, cidade, estado):
    sqlQuery = f"INSERT INTO pacientes (nome, email, fone, cep, endereco, bairro, numero, complemento, dataNascimento, genero, cpf, cidade, estado) VALUES ('{nome}', '{email}', '{fone}', '{cep}', '{endereco}', '{bairro}', {numero}, '{complemento}', '{dataNascimento}', '{genero}', '{cpf}', '{cidade}', '{estado}')"
    conexao(sqlQuery,"altera")


def alterar(id, nome, email, fone, cep, endereco, bairro, numero, complemento, dataNascimento, genero, cpf, cidade, estado):
    sqlQuery = f"UPDATE pacientes SET nome = '{nome}', email = '{email}', fone = '{fone}', cep = '{cep}', endereco = '{endereco}', bairro = '{bairro}', numero = {numero} , complemento = '{complemento}', dataNascimento = '{dataNascimento}', genero = '{genero}', cpf = '{cpf}', cidade = '{cidade}', estado='{estado}' WHERE id={id}"
    conexao(sqlQuery,"altera")

def deletar(id):
    sqlQuery = f"DELETE FROM pacientes WHERE id={id}"    
    conexao(sqlQuery,"altera")

if os.path.isfile('cadastro.db'):
    print("Banco existe")
else:
    inicio()
