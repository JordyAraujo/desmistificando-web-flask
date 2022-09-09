import os

from flask import Flask


def create_app():
    app = Flask(__name__)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/ola')
    def ola_mundo():
        return '<h1>Olá, mundo!</h1>'

    @app.route('/ola/<nome>')
    def ola_nome(nome):
        return f'Olá, {nome}!'

    @app.route('/cadastrar')
    def form_cadastrar():
        return render_template('cadastrar.html')

    return app