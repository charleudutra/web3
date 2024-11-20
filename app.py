"""
@author: charleu
"""

from aula02_rota import app_charleu,saudacoes

print("o objetvo Flask foi importado com sucesso")

print( saudacoes ('charleu'))

app_charleu = Falsk (__name__ , template_folder='template')

@app_charleu.route("/")
def homepage():
    return render_template ("homepage.html")

@app_charleu.route("/index")
def indice():
    return render_template("index.html")

@app_charleu.route("/contato")
def contato():
    return render_template("contato.html")

@app_charleu.route("/usuario")
def dados_usuario():
    nome_usuario="charleu"
    dados_usu ={"profissao": "Professora EBTT", "disciplina":"Desenvolvimento Web III"}
    return render_template("usuario.html", nome = nome_usuari, dados = dados_usu)
@app_charleu.route('/rota1')

@app_charleu.route('/ola')
def rota1():
    return 'ola, turma!'

@app_charleu.route('/rota2')
def rota2():
    resposta ="<H3> essa e outra pagina da rota 2 <H3>"
    return resposta

def raiz():

def saudacoes (nome):
    return f'olá,{nome}!'

if __name__ == "__main__" :

    app_charleu.run(port = 8000)