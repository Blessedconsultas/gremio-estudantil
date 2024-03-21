from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de candidatos
candidatos = {
    "Candidato A": 0,
    "Candidato B": 0,
    "Candidato C": 0
}

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html', candidatos=candidatos)

# Rota para registrar o voto
@app.route('/votar', methods=['POST'])
def votar():
    candidato_votado = request.form['candidato']
    candidatos[candidato_votado] += 1
    return redirect(url_for('index'))

# Rota para exibir os resultados
@app.route('/resultados')
def resultados():
    return render_template('resultados.html', candidatos=candidatos)

if __name__ == '__main__':
    app.run(debug=True)
