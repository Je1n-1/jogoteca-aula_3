from flask import Flask, render_template, request, redirect, session, flash

# Classe que representa um jogo
class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console

# Instâncias de jogos
jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Hack n Slash', 'PS2')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')
lista = [jogo1, jogo2, jogo3]  # Lista de jogos

app = Flask(__name__)  # Cria a aplicação Flask
app.secret_key = 's3cr3t0'  # Chave secreta para sessões

# Rota principal que exibe a lista de jogos
@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)

# Rota para exibir o formulário de novo jogo
@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')

# Rota para criar um novo jogo a partir do formulário
@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']         # Obtém o nome do formulário
    categoria = request.form['categoria'] # Obtém a categoria do formulário
    console = request.form['console']     # Obtém o console do formulário
    jogo = Jogo(nome, categoria, console) # Cria uma nova instância de Jogo
    lista.append(jogo)                    # Adiciona o novo jogo à lista
    #return render_template('lista.html', titulo='Jogos', jogos=lista)
    return redirect('/')  # Redireciona para a rota principal


# Rota para exibir o formulário de login
@app.route('/login')
def login():
    return render_template('login.html')

# Rota para autenticar o usuário a partir do formulário de login
@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'alohomora' == request.form['senha']:  # Verifica se a senha está correta
        session['usuario_logado'] = request.form['usuario']  # Armazena o usuário na sessão
        flash('Usuário logado com sucesso!')  # Mensagem de sucesso
        return redirect('/')                  # Redireciona para a página principal
    else:
        flash('Usuário não logado, tente novamente!')          # Mensagem de erro
        return redirect('/login')             # Redireciona de volta para o login

app.run(debug=True)  # Executa a aplicação em modo debug


"""
Como funciona o fluxo:
Quando você acessa /, o Flask procura o arquivo lista.html na pasta templates e mostra a lista de jogos.
Se você clicar em "Novo Jogo" (normalmente um botão ou link em lista.html), vai para /novo, que mostra o formulário de novo.html.
Ao enviar o formulário de novo jogo, o método POST vai para /criar, que adiciona o jogo à lista e redireciona de volta para /, mostrando a lista atualizada.
"""