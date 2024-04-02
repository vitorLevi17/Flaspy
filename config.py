import os

SECRET_KEY = 'alurar'

SQLALCHEMY_DATABASE_URI = \
    'mysql+mysqlconnector://{usuario}:{senha}@{servidor}/{database}'.format(
        usuario='root',
        senha='',
        servidor='localhost',
        database='jogoteca'
    )
UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/fotos'

