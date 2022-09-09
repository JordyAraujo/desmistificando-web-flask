import os
import db

from flask import Flask, render_template, request


def create_app():
    app = Flask(__name__)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, f'{__name__}.sqlite'),
    )

    db.init_app(app)

    @app.route('/ola')
    def ola_mundo():
        return '<h1>Olá, mundo!</h1>'

    @app.route('/ola/<nome>')
    def ola_nome(nome):
        return f'Olá, {nome}!'

    @app.route('/cadastrar')
    def form_cadastrar():
        return render_template('cadastrar.html')

    @app.route('/cadastrar', methods=['POST'])
    def cadastrar():
        nome = request.form['nome']
        banco = db.get_db()
        banco.execute(
            "INSERT INTO pessoa (nome) VALUES (?)",
            [nome],
        )
        banco.commit()

        return f'Olá, {nome}!'

    return app