from flask import Flask,render_template,request, redirect, session, flash

class Jogo:
    def __init__(self,nome,console,categoria):
        self.nome = nome
        self.console = console
        self.categoria = categoria

app = Flask(__name__)
app.secret_key = 'alurar'

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
    return render_template("login.html")

@app.route('/autenticar',methods = ['POST'])
def autenticar():
    if "fifa" == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + 'Usuario logado')
        return redirect("/")
    else:
        flash('TA ERRADO PAE')
        return redirect("/login")

@app.route('/NovoJogo')
def cadastrarJogo():
    tituloo = "Cadastre seus Jogos favoritos"
    return render_template("cadastrarJogo.html",titulo=tituloo)

@app.route('/criar',methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome,console,categoria)
    lista_games.append(jogo)
    return redirect("/")

app.run(debug=True,port=8080)
