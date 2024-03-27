from jogo import db

class Jogos(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    nome = db.Column(db.String(50), nullable = False)
    categoria = db.Column(db.String(50), nullable=False)
    console = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name

class Usuarios(db.Model):
    nick = db.Column(db.String(50), primary_key = True)
    nome = db.Column(db.String(50), nullable = False)
    senha = db.Column(db.String(50), nullable=False)
    def __repr__(self):
        return '<Name %r>' % self.name
