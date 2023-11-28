from flask import Flask, render_template, request, redirect
import psycopg2
from APP.info_pessoal import *

conn= psycopg2.connect(
    dbname= db_name,
    user= db_user,
    password= db_password,
    host= db_host
)
cur= conn.cursor()
app= Flask(__name__)

#=======================================================

#====================CADASTRO USUARIO=========================

@app.route('/cadastro/', methods=['GET'])
def mostrando_usuarios():
    return render_template('registro.html')



@app.route('/verificando/cadastro/', methods=['POST'])
def verificando_cadastro():
    cur.execute("SELECT email FROM usuarios")
    verificando_email= cur.fetchall()

    for email in verificando_email:
        if request.form['email'] == email[0]:
            return redirect('/cadastro/')
    

    cur.execute(f"INSERT INTO usuarios(nome_usuario, email, senha) VALUES('{request.form['nome_usuario']}', '{request.form['email']}', {request.form['senha']})")
    conn.commit()


    return redirect('/login/')

#====================CADASTRO USUARIO=========================





#====================LOGIN USUARIO=========================
@app.route('/login/', methods=['GET'])
def mostrando_usuarios_ordem():
    return render_template('login.html')


@app.route('/verificando/login/', methods=['POST'])
def verificando_login():
    cur.execute("SELECT email, senha FROM usuarios")
    verificando_registros= cur.fetchall()

    for registro in verificando_registros:
        if request.form['email'] == registro[0]:
            if int(request.form['senha']) == registro[1]:
                return redirect('/login/')

    return redirect('/cadastro/')

#====================LOGIN USUARIO=========================

#=======================================================

