from flask import render_template, url_for, flash, redirect
from projeto import app


@app.route('/')
@app.route('/login')
def login():
    return render_template(url_for('login'), title='Login')

@app.route('/cadastro')
def cadastro():
    return render_template(url_for('cadastro'), title='Cadastro')

@app.route('/chat')
def chat():
    return render_template(url_for('chat'))

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', title='Sobre')

