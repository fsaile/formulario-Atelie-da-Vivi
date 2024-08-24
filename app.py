from flask import Flask, request, redirect, render_template, flash
import csv
import os
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'  # Altere para uma chave secreta segura

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    # Validações
    if not name or not email or not password:
        flash('Todos os campos são obrigatórios.')
        return redirect('/')

    # Criptografa a senha
    hashed_password = generate_password_hash(password, method='sha256')

    # Adiciona os dados ao arquivo CSV
    if not os.path.isfile('submissions.csv'):
        with open('submissions.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Email', 'Password'])

    with open('submissions.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, email, hashed_password])

    return redirect('/thankyou')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)
