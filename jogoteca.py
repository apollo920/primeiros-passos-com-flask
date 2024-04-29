from flask import Flask, render_template, request

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console
jogo1= Jogo('Mortal Kombat', 'Jogo de luta', 'XBOX e PLAY STATION')
jogo2 = Jogo('God of War', 'Rack n Slash', 'PS2')
jogo3 = Jogo('Overwatch', 'FPS', 'XBOX e PLAY STATION')
lista_jogo = [jogo1,jogo2,jogo3]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista_jogo)

@app.route('/novo')
def novo():
    return render_template('novo_jogo.html',titulo='Cadastrar Jogos')

@app.route('/criar', methods=['POST','GET'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome,categoria,console)
    lista_jogo.append(jogo)
    return render_template('lista.html', titulo='Jogos', jogos=lista_jogo)

app.run(debug=True)
