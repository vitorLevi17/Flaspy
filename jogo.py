from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect



app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
csrf = CSRFProtect(app)

from rotas import *
if __name__ == '__main__':
    app.run(debug=True,port=8080)
