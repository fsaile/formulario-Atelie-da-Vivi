from waitress import serve
from app import app  # Certifique-se de que 'app' é o nome do seu objeto Flask no arquivo app.py

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8000)

