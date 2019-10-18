from flask import Flask, render_template, request, redirect
from classeclientes import Clientes
from classefilmes import Filmes
from classelocacao import Locacao
import MySQLdb

#filmes
def listar_filmes_db():  ############ MÉTODO PARA LISTAR OS DADOS JÁ CONTIDOS NA TABELA DO BD)
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

def listar_clientes_db():  ############ MÉTODO PARA LISTAR OS DADOS DE CLIENTES JÁ CONTIDOS NA TABELA DO BD)
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

def listar_locacoes_db():  ############ MÉTODO PARA LISTAR OS DADOS DE LOCACOES JÁ CONTIDOS NA TABELA DO BD)
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae07", passwd="grupo02", database="zuplae07")
    cursor = conexao.cursor()
    cursor.execute("SELECT c.NOME, f.TITULO, f.VALOR, l.DATA_LOCACAO from LOCACAO as l join CLIENTE as c on l.ID_CLIENTE = c.ID join FILMES as f on l.ID_FILME = f.ID") 
    listar_locacoes = []
    for i in cursor.fetchall():
        locacao  = Locacao()
        locacao.nome = i[0]
        locacao.id_filme = i[1]
        locacao.valor = i[2]
        locacao.data_locacao = i[3]
        listar_locacoes.append(locacao)
    conexao.close()
    return listar_locacoes


############ MÉTODO PARA SALVAR FILMES NO BD ##############  
def salvar_filmes_db(titulo, ano, valor):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae07", passwd="grupo02", database="zuplae07")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO FILMES (TITULO,ANO,VALOR)" + 
    " VALUES ('{}', '{}', '{}')".format(titulo,ano,valor))
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

def salvar_locacao_db(id_cliente, id_filme, data_locacao):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae07", passwd="grupo02", database="zuplae07")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO LOCACAO (ID_CLIENTE, ID_FILME, DATA_LOCACAO)" + 
    " VALUES ('{}', '{}', '{}')".format(id_cliente, id_filme, data_locacao))
    conexao.commit()
    conexao.close()







#rotas
locadora = "LOCADORA HBSIS"
app= Flask(__name__)
@app.route('/')
def inicio():
    return render_template('index.html', nome_pagina = locadora)

##### rota onde estão os filmes listados
@app.route('/filmes')
def filmes():
    lista_filmes = listar_filmes_db()
    return render_template ('lista_filmes.html', lista = lista_filmes)
######

@app.route('/clientes') 
def clientes():
    lista_clientes = listar_clientes_db()
    return render_template('lista_cliente.html', nome_pagina = locadora, lista = lista_clientes)

@app.route('/filmes/cadastro')
def filmes_cadastro():
    return render_template ('cadastrar_filmes.html')
 

################### ROTA PARA SALVAR NO BANCO DE DADOS ################# 
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

########### Rota de Salvar Cliente no BD ############
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


@app.route('/locacao/salvar', methods = ["POST"])
def salvar_locacao():
    filmes = request.form['filmes']
    cliente = request.form['cliente']
    data_locacao = request.form['data_locacao']
    locacao= Locacao()
    locacao.id_filmes = filmes
    locacao.id_cliente = cliente
    locacao.data_locacao = data_locacao
    salvar_locacao_db(locacao.id_filmes, locacao.id_cliente, locacao.data_locacao)
    return redirect('/locacoes')






@app.route('/clientes/cadastro')
def cliente_cadastro():
    return render_template('cadastrar_clientes.html')


@app.route('/locacoes')
def locacoes():
    lista3 = listar_locacoes_db()
    return render_template('lista_locacoes.html', lista3 = lista3)

@app.route('/locar/filme')
def locar_filme():
    listar_nomes = listar_clientes_db()
    listar_titulos = listar_filmes_db()
    return render_template('cadastrar_locacao.html', lista = listar_nomes, lista2 = listar_titulos)

app.run()



