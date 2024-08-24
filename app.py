from flask import Flask, request, redirect, render_template
import csv
import os
from werkzeug.security import generate_password_hash

app = Flask(__name__)

# Rota para exibir o formulário
@app.route('/')
def index():
    return render_template('index.html')

# Rota para processar o formulário
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    
    # Criptografa a senha
    hashed_password = generate_password_hash(password)

    # Adiciona os dados ao arquivo CSV
    if not os.path.isfile('submissions.csv'):
        with open('submissions.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Email', 'Password'])

    with open('submissions.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, email, hashed_password])

    return redirect('/thankyou')

# Rota para página de agradecimento
@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)
