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

def historicoFinanceiro():
    sqlQuery = 'CREATE TABLE historicoFinanceiro (id INTEGER PRIMARY KEY AUTOINCREMENT, idPaciente INTEGER, dataRecibo VARCHAR(15), valorRecibo REAL)'
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

def historicoFinanceiroAdd(idPaciente, dataRecibo, valorRecibo):
    sqlQuery = f"INSERT INTO historicoFinanceiro (idPaciente, dataRecibo, valorRecibo) VALUES ('{idPaciente}', '{dataRecibo}', '{valorRecibo}')"
    conexao(sqlQuery,"altera")

def historicoFinanceiroDel(id):
    sqlQuery = f"DELETE FROM historicoFinanceiro WHERE id={id}"
    conexao(sqlQuery,"altera")

def historicoFinanceiroSelAll(id):
    sqlQuery = f'SELECT * FROM historicoFinanceiro as hf LEFT JOIN pacientes as p on hf.idPaciente=p.id where p.id={id} order by hf.id desc'
    historico = conexao(sqlQuery,"select")    
    return historico

def historicoFinanceiroSelUnit(id):
    sqlQuery = f'SELECT idPaciente FROM historicoFinanceiro WHERE id={id}'
    historico = conexao(sqlQuery,"select")    
    return historico

if os.path.isfile('cadastro.db'):
    print("Banco existe")
else:
    inicio()
    historicoFinanceiro()

def testeLeft():
    sqlQuery = 'SELECT historicoFinanceiro.id, historicoFinanceiro.dataRecibo, pacientes.nome FROM historicoFinanceiro LEFT JOIN pacientes on historicoFinanceiro.idPaciente=pacientes.id where pacientes.id=2'
    historico = conexao(sqlQuery,"select")    
    return historico