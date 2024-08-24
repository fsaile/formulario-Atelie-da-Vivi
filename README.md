[text](README.md)
# Formulário HTML

## Descrição

Este projeto contém um formulário HTML básico. O objetivo é criar um formulário simples para coletar informações dos usuários.

## Estrutura do Projeto

- `index.html`: O arquivo principal HTML.
- `css/`: Pasta para arquivos de estilo CSS.
- `js/`: Pasta para arquivos de script JavaScript.
- `images/`: Pasta para imagens e recursos gráficos.

## Instruções de Uso

1. Abra o arquivo `index.html` em um navegador da web para visualizar o formulário.
2. Adicione estilos na pasta `css/` e scripts na pasta `js/` conforme necessário.

## Contribuindo

Se você deseja contribuir com o projeto, por favor, siga estas etapas:
1. Faça um fork do repositório.
2. Crie uma nova branch (`git checkout -b feature/nova-funcionalidade`).
3. Faça suas alterações e commit (`git commit -am 'Adiciona nova funcionalidade'`).
4. Faça push para a branch (`git push origin feature/nova-funcionalidade`).
5. Abra um pull request.

## Segurança e Armazenamento de Senhas

Neste projeto, as senhas dos usuários são armazenadas de forma segura usando hashing. Ao enviar um formulário, a senha é criptografada antes de ser salva no arquivo CSV.

### Criptografia de Senhas

A criptografia é realizada utilizando a biblioteca `werkzeug`. As senhas são transformadas em hashes antes de serem armazenadas, garantindo que mesmo que o arquivo CSV seja acessado, as senhas não estejam visíveis em texto claro.

### Como Funciona

- **Hashing da Senha:** Quando um usuário envia um formulário, a senha é criptografada usando o método `generate_password_hash` da biblioteca `werkzeug.security`.
- **Armazenamento:** O hash da senha é armazenado no arquivo `submissions.csv` em vez da senha em texto claro.
- **Verificação:** Ao verificar uma senha, o hash armazenado é comparado com o hash da senha fornecida pelo usuário usando `check_password_hash`.


## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
