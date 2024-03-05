import sqlite3

def inicio():
    conexao = sqlite3.connect('cadastro.db')
    cursor = conexao.cursor()

    cursor.execute('CREATE TABLE pacientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(50), email VARCHAR(50), fone VARCHAR(50), cep VARCHAR(50), endereco VARCHAR(50), bairro VARCHAR(50), numero INT, complemento VARCHAR(30), dataNascimento VARCHAR(15), genero VARCHAR(20), cpf VARCHAR(20))')
    conexao.commit()
    conexao.close()
    print("Create Table successfully")

def todos():
    conexao = sqlite3.connect('cadastro.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM pacientes")
    pacientes = cursor.fetchall()
    
    conexao.close()
    return pacientes

def selectOne(id):
    conexao = sqlite3.connect('cadastro.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM pacientes WHERE id="+id)

    paciente = cursor.fetchall()
    conexao.close()
    return paciente

def inserir(nome, email, fone, cep, endereco, bairro, numero, complemento, dataNascimento, genero, cpf):
    conexao = sqlite3.connect('cadastro.db')
    cursor = conexao.cursor()

    sqlQuery = f"INSERT INTO pacientes (nome, email, fone, cep, endereco, bairro, numero, complemento, dataNascimento, genero, cpf) VALUES ('{nome}', '{email}', '{fone}', '{cep}', '{endereco}', '{bairro}', {numero}, '{complemento}', '{dataNascimento}', '{genero}', '{cpf}')"
    cursor.execute(sqlQuery)

    conexao.commit()
    conexao.close()
    #print(f"Paciente: {nome} inserido")

def alterar(id, nome, email, fone, cep, endereco, bairro, numero, complemento, dataNascimento, genero, cpf):
    conexao = sqlite3.connect('cadastro.db')
    cursor = conexao.cursor()
    sqlQuery = f"UPDATE pacientes SET nome = '{nome}', email = '{email}', fone = '{fone}', cep = '{cep}', endereco = '{endereco}', bairro = '{bairro}', numero = {numero} , complemento = '{complemento}', dataNascimento = '{dataNascimento}', genero = '{genero}', cpf = '{cpf}' WHERE id={id}"
    print("Alterado: "+ nome)
    cursor.execute(sqlQuery)
    
    conexao.commit()
    conexao.close()

def deletar(id):
    conexao = sqlite3.connect('cadastro.db')
    cursor = conexao.cursor()
    sqlQuery = f"DELETE FROM pacientes WHERE id={id}"    
    cursor.execute(sqlQuery)

    conexao.commit()
    conexao.close()


