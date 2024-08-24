from flask import Flask, request, redirect, render_template
import csv
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    # Adiciona os dados ao arquivo CSV
    if not os.path.isfile('submissions.csv'):
        with open('submissions.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Email', 'Password'])
    
    with open('submissions.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, email, password])

    return redirect('/thankyou')

@app.route('/thankyou')c
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)
