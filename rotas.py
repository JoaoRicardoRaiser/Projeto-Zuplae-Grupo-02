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


def salvar_filmes_db(titulo, ano, valor):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae07", passwd="grupo02", database="zuplae07")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO FILMES (TITULO,ANO,VALOR)" + 
    " VALUES ('{}', '{}', '{}')".format(titulo,ano,valor))
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
    return render_template ('lista_filmes.html')
######

@app.route('/clientes') 
def clientes():
    return render_template('clientes.html', nome_pagina = locadora)

@app.route('/filmes/cadastro')
def filmes_cadastro():
    return render_template ('cadastrar_filmes.html')
 
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



app.run(debug=True)



