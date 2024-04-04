from ajudas import recupera_img,excluir_img, FormularioJogo
from flask import render_template,request, redirect, session, flash, url_for, send_from_directory
from models import Jogos
from jogo import app,db

@app.route('/')
def inicio():
    lista_games = Jogos.query.order_by(Jogos.id)
    return render_template("inicio.html",titulo = "Games",jogos=lista_games)

@app.route('/NovoJogo')
def cadastrarJogo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('cadastrarJogo')))
    else:
        tituloo = "Cadastre seus Jogos favoritos"
        form = FormularioJogo()
        return render_template("cadastrarJogo.html",titulo=tituloo, form = form)

@app.route('/criar',methods=['POST'])
def criar():
    form = FormularioJogo(request.form)

    if not form.validate_on_submit():
        return redirect(url_for('cadastrarJogo'))


    nome = form.nome.data
    categoria = form.categoria.data
    console = form.console.data


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
    form = FormularioJogo()
    form.nome.data = jogo.nome
    form.categoria.data = jogo.categoria
    form.console.data = jogo.console
    tituloo = "Editar jogo"
    capa_jogo = recupera_img(id)
    return render_template("editar.html",titulo=tituloo,id = id, capa_jogo = capa_jogo, form = form)

@app.route('/atualizaar',methods=['POST'])
def atualizar():

    form = FormularioJogo(request.form)

    if form.validate_on_submit():


        jogo = Jogos.query.filter_by(id=request.form['id']).first()
        jogo.nome = form.nome.data
        jogo.categoria = form.categoria.data
        jogo.console = form.console.data

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

