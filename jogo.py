from flask import Flask,render_template,request, redirect, session, flash, url_for

class Jogo:
    def __init__(self,nome,console,categoria):
        self.nome = nome
        self.console = console
        self.categoria = categoria

class Usuario:
    def __init__(self,nome,nick,senha):
        self.nome = nome
        self.nick = nick
        self.senha = senha

app = Flask(__name__)
app.secret_key = 'alurar'

us = Usuario('Bagio','rob',"12345")
us1 = Usuario('Materazzi','zidsis',"123456")
us2 = Usuario('Bio','r',"1234567")
users = {us.nick: us, us1.nick: us1, us2.nick: us2}


jogo1 = Jogo("Valorant","PC","Estrategia")
jogo2 = Jogo("FIFA", "PS4", "Esportes")
jogo3 = Jogo("NBA", "XBOX", "Esportes")
jogo4 = Jogo("Uncharted", "Ps3", "Historia")
jogo5 = Jogo("The last of us", "PS5", "Estrategia")
lista_games = [jogo1,jogo2,jogo3,jogo4,jogo5]

@app.route('/')
def inicio():
    return render_template("inicio.html",titulo = "Games",jogos=lista_games)

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['usuario'] in users:
        usuario = users[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nick
            flash(session['usuario_logado'] + ' logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Credenciais inválidas. Tente novamente.')
        return redirect(url_for('login'))
@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash("Logout feito")
    return redirect(url_for('inicio'))
@app.route('/NovoJogo')
def cadastrarJogo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('cadastrarJogo')))
    else:
        tituloo = "Cadastre seus Jogos favoritos"
        return render_template("cadastrarJogo.html",titulo=tituloo)

@app.route('/criar',methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome,console,categoria)
    lista_games.append(jogo)
    return redirect(url_for('inicio'))

app.run(debug=True,port=8080)
