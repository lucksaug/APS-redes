from flask import render_template, url_for, flash, redirect
from projeto import app


@app.route('/')
@app.route('/login')
def login():
    return render_template('login.html', title='Login')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', title='Cadastro')

@app.route('/chat')
def chat():
    return render_template('chat.html', title='Chat')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', title='Sobre')

