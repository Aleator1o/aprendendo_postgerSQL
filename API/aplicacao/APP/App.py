from flask import Flask, render_template
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

@app.route('/')
def rota_vaizia():
    return 'Deu bom a troca, sem falhas'


@app.route('/usuarios/')
def mostrando_usuarios():
    cur.execute('SELECT * FROM usuarios ORDER BY id_usuario ASC')
    mostrando_usuarios_ordem_crescente_id= cur.fetchall()
    return render_template('index.html', mostrando_usuarios_crescente_id= mostrando_usuarios_ordem_crescente_id)


@app.route('/usuario_ordem/')
def mostrando_usuarios_ordem():
    cur.execute('SELECT * FROM usuarios ORDER BY id_usuario ASC')
    mostrando_usuarios_ordem_crescente_id= cur.fetchall()
    return render_template('usuario_ordem.html', mostrando_usuarios_crescente_id= mostrando_usuarios_ordem_crescente_id)

#=======================================================

