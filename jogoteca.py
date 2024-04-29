from flask import Flask, render_template, request

#trabalhando com POO 
class Jogo:
    def __init__(self,nome,categoria,console):
        self.nome=nome
        self.categoria=categoria
        self.console=console
jogo1= Jogo('Valorant','FPS','Computador')
lista_jogos=[jogo1]

#Estrutura do flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('lista.html',titulo='Jogos',lista_jogos=lista_jogos)

@app.route('/novo')
def novo():
    return render_template('novo_jogo.html',titulo='Cadastrar novo jogo')

@app.route('/criar',methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome,categoria,console)
    lista_jogos.append(jogo)
    return render_template('lista.html',titulo='Lista de Jogos', lista_jogos=lista_jogos)
app.run(debug=True)