from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
@app.route('/login')
def login():
    return render_template('login.html', title='Login')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', title='Cadastro')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', title='Sobre')



if __name__ == "__main__":
    app.run(debug=True)