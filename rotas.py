from flask import Flask, render_template, request, redirect
from classeclientes import Clientes
from classefilmes import Filmes
from classelocacao import Locacao
import MySQLdb

 ############ MÉTODO PARA LISTAR OS DADOS JÁ CONTIDOS NA TABELA DO BD) #######################################


def listar_filmes_db():  
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae07", passwd="grupo02", database="zuplae07")
    cursor = conexao.cursor()
    cursor.execute("select * from FILMES") 
    listar_filmes = []
    for i in cursor.fetchall():
        filmes  = Filmes()
        filmes.id = i[0]
        filmes.titulo = i[1]
        filmes.ano = i[2]
        filmes.valor = i[3]
        listar_filmes.append(filmes)
    conexao.close()
    return listar_filmes


############ MÉTODO PARA LISTAR OS DADOS DE CLIENTES JÁ CONTIDOS NA TABELA DO BD) ############################

def listar_clientes_db():  
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae07", passwd="grupo02", database="zuplae07")
    cursor = conexao.cursor()
    cursor.execute("select * from CLIENTE") 
    listar_clientes = []
    for i in cursor.fetchall():
        clientes  = Clientes()
        clientes.id = i[0]
        clientes.nome = i[1]
        clientes.telefone = i[2]
        clientes.cpf = i[3]
        listar_clientes.append(clientes)
    conexao.close()
    return listar_clientes


 ############ MÉTODO PARA LISTAR OS DADOS DE LOCACOES JÁ CONTIDOS NA TABELA DO BD) #############################

def listar_locacoes_db(): 
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae07", passwd="grupo02", database="zuplae07")
    cursor = conexao.cursor()
    cursor.execute("SELECT c.NOME, f.TITULO, f.VALOR, l.DATA_LOCACAO, l.ID from LOCACAO as l join CLIENTE as c on l.ID_CLIENTE = c.ID join FILMES as f on l.ID_FILME = f.ID") 
    listar_locacoes = []
    for i in cursor.fetchall():
        locacao  = Locacao()
        locacao.id = i[4]
        locacao.nome = i[0]
        locacao.id_filme = i[1]
        locacao.valor = i[2]
        locacao.data_locacao = i[3]
        listar_locacoes.append(locacao)
    conexao.close()
    return listar_locacoes

############################ DELETAR CLIENTE NO BD ###############################################################
def deletar_cliente(id):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae07", passwd="grupo02", database="zuplae07")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM CLIENTE WHERE id={}".format(id))
    conexao.commit()
    conexao.close()

########################### ALTERAR CLIENTE NO BD ####################################################################

def alterar_cliente_db(cliente):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae07", passwd="grupo02", database="zuplae07")
    cursor = conexao.cursor()
    cursor.execute("UPDATE CLIENTE SET NOME='{}', TELEFONE='{}', CPF='{}' WHERE ID={}"
    .format(cliente.nome, cliente.telefone, cliente.cpf , cliente.id))
    conexao.commit() 
    conexao.close()   


############ MÉTODO PARA SALVAR FILMES NO BD ###############################################################  

def salvar_filmes_db(titulo, ano, valor):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae07", passwd="grupo02", database="zuplae07")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO FILMES (TITULO,ANO,VALOR)" + 
    " VALUES ('{}', '{}', '{}')".format(titulo,ano,valor))
    conexao.commit()
    conexao.close()

############################ DELETAR FILME NO BD ###############################################################
def deletar_filme(id):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae07", passwd="grupo02", database="zuplae07")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM FILMES WHERE id={}".format(id))
    conexao.commit()
    conexao.close()

########################### ALTERAR FILME NO BD ####################################################################

def alterar_filmes_db(filme):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae07", passwd="grupo02", database="zuplae07")
    cursor = conexao.cursor()
    cursor.execute("UPDATE FILMES SET TITULO='{}', ANO='{}', VALOR='{}' WHERE ID={}"
    .format(filme.titulo, filme.ano, filme.valor, filme.id))
    conexao.commit() 
    conexao.close()   

 ############ MÉTODO PARA SALVAR CLIENTE NO BD ##############   

def salvar_clientes_db(nome, telefone, cpf):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae07", passwd="grupo02", database="zuplae07")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO CLIENTE (NOME,TELEFONE,CPF)" + 
    " VALUES ('{}', '{}', '{}')".format(nome,telefone,cpf))
    conexao.commit()
    conexao.close()

############ MÉTODO PARA SALVAR LOCAÇÃO NO BD ##############       

def salvar_locacao_db(id_cliente, id_filme, data_locacao):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae07", passwd="grupo02", database="zuplae07")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO LOCACAO (ID_CLIENTE, ID_FILME, DATA_LOCACAO)" + 
    " VALUES ('{}', '{}', '{}')".format(id_cliente, id_filme, data_locacao))
    conexao.commit()
    conexao.close()


############################ DELETAR LOCAÇÃO NO BD ###############################################################
def deletar_locacao(id):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae07", passwd="grupo02", database="zuplae07")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM LOCACAO WHERE id={}".format(id))
    conexao.commit()
    conexao.close()


def buscar_filme_por_id(id):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae07", passwd="grupo02", database="zuplae07")
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM FILMES WHERE id ={}'.format(id))
    f = Filmes()
    for i in cursor.fetchall():
        f.id = i[0]
        f.titulo = i[1]
        f.ano = i[2]
        f.valor = i[3]
    conexao.close()
    return f

def buscar_cliente_por_id(id):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae07", passwd="grupo02", database="zuplae07")
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM CLIENTE WHERE id ={}'.format(id))
    c = Clientes()
    for i in cursor.fetchall():
        c.id = i[0]
        c.nome = i[1]
        c.telefone = i[2]
        c.cpf = i[3]
    conexao.close()
    return c




####################### ROTA INICIAL  ###########################################


locadora = "LOCADORA HD"
app= Flask(__name__)
@app.route('/')
def inicio():
    return render_template('index.html', nome_pagina = locadora)


####################### ROTA PARA LISTAR FILMES ###########################################

@app.route('/filmes')
def filmes():
    lista_filmes = listar_filmes_db()
    return render_template ('lista_filmes.html', lista = lista_filmes)


####################### ROTA PARA LISTAR CLIENTES #################################################

@app.route('/clientes') 
def clientes():
    lista_clientes = listar_clientes_db()
    return render_template('lista_cliente.html', nome_pagina = locadora, lista = lista_clientes)

####################### ROTA CADASTRAR FILME ###########################################

@app.route('/filmes/cadastro')
def filmes_cadastro():
    return render_template ('cadastrar_filmes.html')
 

################### ROTA PARA SALVAR CLIENTE NO BANCO DE DADOS ################# 

@app.route('/filmes/salvar', methods = ["POST"])
def salvar():
    titulo = request.form['titulo']
    ano = request.form['ano']
    valor = request.form['valor']
    filme= Filmes()
    filme.titulo = titulo 
    filme.ano = ano 
    filme.valor = valor
    salvar_filmes_db(filme.titulo, filme.ano, filme.valor)
    return redirect('/filmes')

################### ROTA PARA SALVAR NO BANCO DE DADOS ################# 

@app.route('/filmes/alterar/salvar', methods = ["POST"])
def salvar_f():
    id = request.form['id']
    titulo = request.form['titulo']
    ano = request.form['ano']
    valor = request.form['valor']
    filme= Filmes()
    filme.id = id
    filme.titulo = titulo 
    filme.ano = ano 
    filme.valor = valor
    alterar_filmes_db(filme)
    return redirect('/filmes')


   ####################### ROTA PARA ALTERAR FILME ###########################################

@app.route('/filmes/alterar')
def filme_alterar():
    id = request.args['id']    
    filme = buscar_filme_por_id(id)
    return render_template('editar_filme.html', filme=filme)

################### ROTA PARA SALVAR NO BANCO DE DADOS ################# 

@app.route('/clientes/alterar/salvar', methods = ["POST"])
def salvar_cliente_alterado():
    id = request.form['id']
    nome = request.form['nome']
    telefone = request.form['telefone']
    cpf = request.form['cpf']
    cliente= Clientes()
    cliente.id = id
    cliente.nome = nome 
    cliente.telefone = telefone 
    cliente.cpf = cpf
    alterar_cliente_db(cliente)
    return redirect('/clientes')


   ####################### ROTA PARA ALTERAR CLIENTE ###########################################

@app.route('/cliente/alterar')
def cliente_alterar():
    id = request.args['id']    
    cliente = buscar_cliente_por_id(id)
    return render_template('editar_cliente.html', cliente1 =cliente)

########### ROTA PARA SALVAR CLIENTES ############


@app.route('/clientes/salvar', methods = ["POST"])
def salvar_clientes():
    nome = request.form['nome']
    telefone = request.form['telefone']
    cpf = request.form['cpf']
    cliente= Clientes()
    cliente.nome = nome 
    cliente.telefone = telefone 
    cliente.cpf = cpf
    salvar_clientes_db(cliente.nome, cliente.telefone, cliente.cpf)
    return redirect('/clientes')

 

####################### ROTA PARA SALVAR LOCAÇÃO ###########################################

@app.route('/locacao/salvar', methods = ["POST"])
def salvar_locacao():
    filmes = request.form['filmes']
    cliente = request.form['cliente']
    data_locacao = request.form['data_locacao']
    locacao= Locacao()
    locacao.ID_FILME = filmes
    locacao.ID_CLIENTE = cliente
    locacao.DATA_LOCACAO = data_locacao
    salvar_locacao_db(locacao.ID_CLIENTE, locacao.ID_FILME, locacao.DATA_LOCACAO)
    return redirect('/locacoes')




####################### ROTA PARA CADASTRO CLIENTE ###########################################

@app.route('/clientes/cadastro')
def cliente_cadastro():
    return render_template('cadastrar_clientes.html')



####################### ROTA PARA DELETAR CLIENTE ###########################################
@app.route('/cliente/delete')
def deletar():
    id = request.args['id']
    deletar_cliente(id)
    return redirect ('/clientes')


####################### ROTA PARA DELETAR FILME ###########################################

@app.route('/filmes/delete')
def deletar_filmes():
    id = request.args['id']
    deletar_filme(id)
    return redirect ('/filmes')


####################### ROTA PARA DELETAR LOCAÇÃO ###########################################

@app.route('/locacoes/delete')
def deletar_locacoes():
    id = request.args['id']
    deletar_locacao(id)
    return redirect ('/locacoes')



####################### ROTA PARA LISTAR LOCAÇÕES ###########################################

@app.route('/locacoes')
def locacoes():
    lista3 = listar_locacoes_db()
    return render_template('lista_locacoes.html', lista = lista3)

####################### ROTA PARA LOCAR FILME ###########################################    

@app.route('/locar/filme')
def locar_filme():
    listar_nomes = listar_clientes_db()
    listar_titulos = listar_filmes_db()
    return render_template('cadastrar_locacao.html', lista = listar_nomes, lista2 = listar_titulos)

app.run(debug=True)



