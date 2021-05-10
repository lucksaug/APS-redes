from flask import render_template, url_for, flash, redirect, request
from projeto import app
from projeto.forms import FormularioLogin, FormularioCadastro
from flask_login import login_user, current_user, logout_user, login_required

# Rota para telas: "/" e "chat"
@app.route('/')
@app.route('/chat')
def chat():
    return render_template('chat.html')

# Rota para tela "Login"
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = FormularioLogin()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.senha.data == 'senha':
           flash('Você está conectado!')
           return redirect(url_for('chat'))
        else:
            flash('Login Unseccessful. Por favor confira o email e a senha')
    return render_template('login.html', title='Login', form=form)

# Rota para tela "Cadastro"
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = FormularioCadastro()
    if form.validate_on_submit():
        flash(f'Conta criada com sucesso!',)
        return redirect(url_for('login'))
    return render_template('cadastro.html', title='Cadastro', form=form)

# Rota para tela "Sobre"
@app.route('/sobre')
def sobre():
    return render_template('sobre.html', title='Sobre')
