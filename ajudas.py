import os
from jogo import app

def recupera_img(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if f'{id}' in nome_arquivo:
            return nome_arquivo


    return 'Capa.jpg'

def excluir_img(id):
    arquivo = recupera_img(id)
    if arquivo != 'Capa.jpg':
        os.remove(os.path.join(app.config['UPLOAD_PATH'],arquivo))