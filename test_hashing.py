from werkzeug.security import generate_password_hash, check_password_hash

# Senha para teste
password = 'MinhaSenhaSegura'
hashed_password = generate_password_hash(password)  # Usando método padrão

print(f'Hash da senha: {hashed_password}')

# Verifica se a senha corresponde ao hash
print(f'Senha correta: {check_password_hash(hashed_password, password)}')  # Deve ser True
print(f'Senha incorreta: {check_password_hash(hashed_password, "SenhaErrada")}')  # Deve ser False
