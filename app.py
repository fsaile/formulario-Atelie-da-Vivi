from flask import Flask, request, redirect, render_template, flash, url_for, session
import csv
import os
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'a9c8f5f2b2d23e43cfb8b1f1e5e5aefb'  # Substitua com uma chave secreta segura

# Redirecionamento HTTP para HTTPS
@app.before_request
def before_request():
    if request.headers.get('X-Forwarded-Proto') == 'http':
        return redirect(request.url.replace('http://', 'https://'))

# Dados de usuários para login (em um projeto real, use um banco de dados)
users = {
    'admin@example.com': generate_password_hash('adminpassword')
}

@app.route('/')
def index():
    if 'user' in session:
        return render_template('index.html')
    return redirect(url_for('login'))

@app.route('/add_client', methods=['POST'])
def add_client():
    if 'user' not in session:
        flash('Você precisa estar logado para adicionar clientes!', 'error')
        return redirect(url_for('login'))

    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    if not name or not email or not password:
        flash('Por favor, preencha todos os campos!', 'error')
        return redirect(url_for('index'))

    hashed_password = generate_password_hash(password)

    if not os.path.isfile('submissions.csv'):
        with open('submissions.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Email', 'Password'])

    with open('submissions.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, email, hashed_password])

    flash('Cliente adicionado com sucesso!', 'success')
    return redirect(url_for('thankyou'))

@app.route('/edit_client', methods=['GET'])
def edit_client():
    if 'user' not in session:
        flash('Você precisa estar logado para acessar esta página!', 'error')
        return redirect(url_for('login'))

    email = request.args.get('email')
    client = None

    if os.path.isfile('submissions.csv'):
        with open('submissions.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Email'] == email:
                    client = row
                    break

    if client:
        return render_template('edit_client.html', client=client)
    
    flash('Cliente não encontrado!', 'error')
    return redirect(url_for('index'))

@app.route('/update_client', methods=['POST'])
def update_client():
    if 'user' not in session:
        flash('Você precisa estar logado para atualizar dados!', 'error')
        return redirect(url_for('login'))

    old_email = request.form.get('old_email')
    name = request.form.get('name')
    new_email = request.form.get('email')
    password = request.form.get('password')
    hashed_password = generate_password_hash(password)

    updated_rows = []
    if os.path.isfile('submissions.csv'):
        with open('submissions.csv', mode='r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            for row in reader:
                if row[1] == old_email:
                    updated_rows.append([name, new_email, hashed_password])
                else:
                    updated_rows.append(row)

    with open('submissions.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(updated_rows)

    flash('Cliente atualizado com sucesso!', 'success')
    return redirect(url_for('thankyou'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if email in users and check_password_hash(users[email], password):
            session['user'] = email
            flash('Login bem-sucedido!', 'success')
            return redirect(url_for('index'))
        
        flash('Email ou senha incorretos!', 'error')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Você foi desconectado!', 'success')
    return redirect(url_for('login'))

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)
