from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aula')
@app.route('/aula/<nome>')
@app.route('/aula/<nome>/<curso>/<int:ano>')
def aula(nome = 'Maria', curso = 'Informática', ano = 1):
    dados = {'Nome':nome, 'curso':curso, 'ano':ano} 
    return render_template('aula.html', dados_html=dados)

if __name__ == '__main__':
    app.run()