# 🌐 Flask Web Framework Boilerplate

Este projeto é um **boilerplate** para aplicações web complexas utilizando o **Flask**, um microframework web em Python. Ele inclui funcionalidades comuns para a construção de **aplicações web seguras**, como **autenticação de usuários**, **painéis administrativos**, e **APIs RESTful** com **autenticação JWT**.

## 🚀 Funcionalidades

- 🔐 **Autenticação de Usuários**: Implementação de login e logout com **Flask-Login**.
- 🖥️ **Painel Administrativo**: Dashboard protegido para administração.
- 📱 **API RESTful**: Criação de endpoints para comunicação com o frontend via **JWT** (JSON Web Tokens).
- 🗄️ **Banco de Dados**: Utilização do **SQLAlchemy** para persistência de dados (**SQLite** por padrão).
- 📝 **Validação de Formulários**: Utilização do **Flask-WTF** para formulários protegidos contra **CSRF**.

## 🗂️ Estrutura do Projeto
A estrutura do projeto **my_flask_app** é organizada de forma modular, utilizando **Blueprints** para separar funcionalidades como autenticação, administração e API. Veja como o projeto está organizado:

### Descrição dos Arquivos

- **app/__init__.py**: Contém a configuração da aplicação Flask e a inicialização dos **Blueprints** (`auth`, `admin`, `api`).
- **app/models.py**: Define os modelos de banco de dados, como o modelo `User` para autenticação.
- **app/auth/routes.py**: Define as rotas para login e logout, além da autenticação de usuários.
- **app/admin/routes.py**: Define as rotas do painel administrativo.
- **app/api/routes.py**: Define os endpoints da API, incluindo a geração e validação de tokens JWT.
- **app/templates/**: Contém os templates HTML para as páginas (login, dashboard, etc.).

### Arquivos Importantes

- **config.py**: Arquivo com configurações globais como `SECRET_KEY` e URI do banco de dados.
- **run.py**: Script para rodar a aplicação Flask.
- **requirements.txt**: Contém as dependências do projeto para fácil instalação via `pip`.

Essa estrutura permite que você adicione facilmente novos módulos à medida que a aplicação cresce. Cada funcionalidade é isolada em seu próprio **Blueprint**, facilitando a manutenção e escalabilidade do projeto.

## 📦 Dependências
### As dependências do projeto estão listadas em requirements.txt:

Flask: Framework principal para a construção da aplicação.

Flask-SQLAlchemy: Para integração com o banco de dados (SQLAlchemy).

Flask-WTF: Para formulários protegidos contra CSRF.

Flask-Login: Para autenticação de usuários.

Flask-JWT-Extended: Para autenticação de API via JWT.

### Para instalar as dependências, execute:

pip install -r requirements.txt
