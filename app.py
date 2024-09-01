from flask import Flask, request, redirect, render_template, flash, url_for
import csv
import os
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.secret_key = 'a9c8f5f2b2d23e43cfb8b1f1e5e5aefb'  # Substitua com uma chave secreta segura

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    
    # Verificação básica dos dados
    if not name or not email or not password:
        flash('Por favor, preencha todos os campos!', 'error')
        return redirect(url_for('index'))

    # Criptografia da senha ao salvar
    hashed_password = generate_password_hash(password)

    # Adiciona os dados ao arquivo CSV
    if not os.path.isfile('submissions.csv'):
        with open('submissions.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Email', 'Password'])

    with open('submissions.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, email, hashed_password])

    flash('Dados enviados com sucesso!', 'success')
    return redirect(url_for('thankyou'))

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
