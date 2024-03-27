SECRET_KEY = 'alurar'

SQLALCHEMY_DATABASE_URI = \
    'mysql+mysqlconnector://{usuario}:{senha}@{servidor}/{database}'.format(
        usuario='root',
        senha='',
        servidor='localhost',
        database='jogoteca'
    )
