from ajudas import recupera_img,excluir_img
from flask import render_template,request, redirect, session, flash, url_for, send_from_directory
from models import Jogos, Usuarios
from jogo import app,db

@app.route('/')
def inicio():
    lista_games = Jogos.query.order_by(Jogos.id)
    return render_template("inicio.html",titulo = "Games",jogos=lista_games)

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    usuario = Usuarios.query.filter_by(nick = request.form['usuario']).first()
    if usuario:
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nick
            flash(usuario.nick + ' logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Usuário não logado.')
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


    jogo = Jogos.query.filter_by(nome = nome).first()
    if jogo:
        flash("O jogo já é existente!")
        return redirect(url_for('inicio'))
    new_game = Jogos(nome = nome,categoria = categoria,console = console)
    db.session.add(new_game)
    db.session.commit()

    arquivo = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']
    arquivo.save(f'{upload_path}/{new_game.id}.jpg')

    return redirect(url_for('inicio'))

@app.route('/Editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('editar')))
    jogo = Jogos.query.filter_by(id=id).first()
    tituloo = "Editar jogo"
    capa_jogo = recupera_img(id)
    return render_template("editar.html",titulo=tituloo,jogo = jogo, capa_jogo = capa_jogo)

@app.route('/atualizaar',methods=['POST'])
def atualizar():

    jogo = Jogos.query.filter_by(id=request.form['id']).first()
    jogo.nome = request.form['nome']
    jogo.categoria = request.form['categoria']
    jogo.console = request.form['console']

    db.session.add(jogo)
    db.session.commit()

    arquivo = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']
    excluir_img(jogo.id)
    arquivo.save(f'{upload_path}/{jogo.id}.jpg')

    return redirect(url_for('inicio'))


@app.route('/Excluir/<int:id>')
def excluir(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))

    jogo = Jogos.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Jogo deletado com sucesso')

    return redirect(url_for('inicio'))

@app.route('/fotos/<nome>')
def imagem(nome):
    return send_from_directory('fotos',nome)

