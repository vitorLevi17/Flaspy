import os
from jogo import app
from flask_wtf import FlaskForm
from wtforms import StringField, validators , SubmitField ,PasswordField

def recupera_img(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if f'{id}' in nome_arquivo:
            return nome_arquivo


    return 'Capa.jpg'

def excluir_img(id):
    arquivo = recupera_img(id)
    if arquivo != 'Capa.jpg':
        os.remove(os.path.join(app.config['UPLOAD_PATH'],arquivo))

class FormularioJogo(FlaskForm):
    nome = StringField('Nome do jogo',[validators.DataRequired(),validators.Length(min = 1 , max=50)])
    categoria = StringField('Categoria',[validators.DataRequired(),validators.Length(min = 1 , max=50)])
    console = StringField('Console',[validators.DataRequired(),validators.Length(min = 1 , max=50)])
    salvar = SubmitField('Salvar')

class FormularioUsuario(FlaskForm):
    nick = StringField('Nick',[validators.DataRequired(),validators.Length(min = 1,max=50)])
    senha = PasswordField('Senha',[validators.DataRequired(),validators.Length(min = 1,max=50)])
    login = SubmitField('Login')