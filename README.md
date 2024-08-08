# 📦 ItemManager

Bem-vindo ao **ItemManager**! 🎉 Este é um projeto de gerenciamento de itens que utiliza **FastAPI** para criar uma API robusta e **Flask** para fornecer uma interface web interativa. Com este projeto, você pode facilmente criar, ler, atualizar e excluir itens em um banco de dados SQLite. 🛠️

## 🚀 Funcionalidades

- **CRUD Completo**: Crie, leia, atualize e exclua itens facilmente.
- **Interface Web**: Gerencie itens de forma intuitiva através de uma interface web desenvolvida com Flask.
- **API Rápida e Eficiente**: Utilize uma API desenvolvida com FastAPI para operações rápidas e seguras.
- **Persistência de Dados**: Armazene dados de itens em um banco de dados SQLite.

## 🛠️ Tecnologias Utilizadas

- **[FastAPI](https://fastapi.tiangolo.com/)**: Framework moderno para construir APIs rápidas e eficientes.
- **[Flask](https://flask.palletsprojects.com/)**: Micro framework para criar uma interface web interativa.
- **[SQLAlchemy](https://www.sqlalchemy.org/)**: ORM para interagir com o banco de dados SQLite.
- **[SQLite](https://www.sqlite.org/index.html)**: Banco de dados leve e embutido.

## 🌐 Como Executar

### 1. Clone o Repositório

```bash
git clone https://github.com/thaleson/FlaskAPIItems
cd itemmanager
```

### 2. Crie um Ambiente Virtual

```bash
python -m venv venv
source venv/bin/activate  # Para Windows use `venv\Scripts\activate`
```

### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

### 4. Inicie a API FastAPI

```bash
uvicorn app.main:app --reload
```

### 5. Inicie a Aplicação Flask

```bash
flask run
```

## 📄 Endpoints da API

- `POST /items/` - Cria um novo item.
- `GET /items/{item_id}` - Obtém um item pelo ID.
- `GET /items/` - Obtém todos os itens.
- `PUT /items/{item_id}/` - Atualiza um item pelo ID.
- `DELETE /items/{item_id}/` - Exclui um item pelo ID.

## 🌟 Tela da Aplicação Web

A interface web permite que você visualize e gerencie os itens de maneira intuitiva. Veja a página [Itens](http://127.0.0.1:5000/items) para interagir com a aplicação.

