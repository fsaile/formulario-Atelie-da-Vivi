from flask import Flask, request, redirect, render_template
import csv
import os
from werkzeug.security import generate_password_hash  # Adicionado

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    # Criptografa a senha
    hashed_password = generate_password_hash(password, method='sha256')  # Adicionado

    # Adiciona os dados ao arquivo CSV
    if not os.path.isfile('submissions.csv'):
        with open('submissions.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Email', 'Password'])
    
    with open('submissions.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, email, hashed_password])  # Alterado para armazenar a senha criptografada

    return redirect('/thankyou')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)
