from flask import Flask

app = Flask(__name__)

@app.route('/ola')
def ola_mundo():
    return '<h1>Olá, mundo!</h1>'

@app.route('/ola/<nome>')
def ola_nome(nome):
    return f'Olá, {nome}!'
