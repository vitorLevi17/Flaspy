from ajudas import FormularioUsuario
from jogo import app
from flask import render_template,request, redirect, session, flash, url_for
from models import Usuarios
from flask_bcrypt import check_password_hash

@app.route('/login')
def login():
    form = FormularioUsuario(request.form)
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima, form=form)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    form = FormularioUsuario(request.form)
    usuario = Usuarios.query.filter_by(nick = form.nick.data).first()
    senha = check_password_hash(usuario.senha,form.senha.data)
    if usuario and senha:
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