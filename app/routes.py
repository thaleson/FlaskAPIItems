from flask import Blueprint, render_template, request, redirect, url_for
import requests

# Criação de um Blueprint para o módulo principal da aplicação Flask
bp = Blueprint('main', __name__)

# URL da API FastAPI que será consumida pelo Flask
API_URL = 'http://127.0.0.1:8000/items/'

@bp.route('/')
def index():
    """
    Rota para a página inicial.

    Renderiza a página `index.html`, que pode servir como ponto de entrada para a aplicação.
    """
    return render_template('index.html')

@bp.route('/items', methods=['GET'])
def items():
    """
    Rota para exibir a lista de itens.

    Faz uma requisição GET para a API FastAPI para obter todos os itens.
    Se a requisição for bem-sucedida, renderiza a página `items.html` com a lista de itens.
    Caso contrário, exibe uma mensagem de erro.

    Returns:
        Renderiza o template `items.html` com a lista de itens.
    """
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        items = response.json()
        
        # Imprime o tipo e o conteúdo da resposta para depuração
        print("Tipo de dados recebidos:", type(items))
        print("Dados recebidos:", items)
        
        # Verifica a estrutura dos itens
        for item in items:
            if not isinstance(item, dict) or 'id' not in item:
                return "Erro: Dados inválidos retornados pela API", 500
        
        return render_template('items.html', items=items)
    except requests.exceptions.RequestException as e:
        return f"Erro ao obter dados: {e}", 500

@bp.route('/add-item', methods=['POST'])
def add_item():
    """
    Rota para adicionar um novo item.

    Faz uma requisição POST para a API FastAPI para adicionar um novo item com base nos dados fornecidos no formulário.
    Redireciona para a lista de itens após a adição.

    Returns:
        Redireciona para a rota de exibição de itens.
    """
    data = {
        'name': request.form['name'],
        'description': request.form['description']
    }
    requests.post(API_URL, json=data)
    return redirect(url_for('main.items'))

@bp.route('/delete-item/<int:item_id>', methods=['POST'])
def delete_item(item_id):
    """
    Rota para deletar um item existente.

    Faz uma requisição DELETE para a API FastAPI para remover o item com o ID especificado.
    Redireciona para a lista de itens após a exclusão.

    Args:
        item_id (int): O ID do item a ser excluído.

    Returns:
        Redireciona para a rota de exibição de itens.
    """
    requests.delete(f'{API_URL}{item_id}/')
    return redirect(url_for('main.items'))

@bp.route('/update-item/<int:item_id>', methods=['POST'])
def update_item(item_id):
    """
    Rota para atualizar um item existente.

    Faz uma requisição PUT para a API FastAPI para atualizar o item com o ID especificado com base nos dados fornecidos no formulário.
    Redireciona para a lista de itens após a atualização.

    Args:
        item_id (int): O ID do item a ser atualizado.

    Returns:
        Redireciona para a rota de exibição de itens.
    """
    data = {
        'name': request.form['name'],
        'description': request.form['description']
    }
    requests.put(f'{API_URL}{item_id}/', json=data)
    return redirect(url_for('main.items'))
