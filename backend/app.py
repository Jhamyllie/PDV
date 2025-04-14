import sys
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

# Ajustando o caminho para importar db_connection
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'db')))
from db_connection import create_connection

app = Flask(__name__)
CORS(app)  # Habilita CORS para aceitar requisições do frontend

@app.route('/produtos', methods=['POST'])
def cadastrar_produto():
    try:
        data = request.get_json()
        nome = data.get('nome')
        preco = data.get('preco')
        estoque = data.get('estoque')

        connection = create_connection()
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO produtos (nome, preco, estoque)
            VALUES (%s, %s, %s);
        """, (nome, preco, estoque))

        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({"message": "Produto cadastrado com sucesso!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/produtos', methods=['GET'])
def listar_produtos():
    try:
        connection = create_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()

        # Transformar os produtos em dicionários com tipo adequado
        produtos_formatados = []
        for produto in produtos:
            id, nome, preco, estoque = produto
            produtos_formatados.append({
                "id": id,
                "nome": nome,
                "preco": float(preco),     # <-- Transforma para float
                "estoque": estoque
            })

        cursor.close()
        connection.close()

        return jsonify(produtos_formatados), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/produtos/<int:id>', methods=['PUT'])
def atualizar_produto(id):
    try:
        data = request.get_json()
        nome = data.get('nome')
        preco = data.get('preco')
        estoque = data.get('estoque')

        connection = create_connection()
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE produtos
            SET nome = %s, preco = %s, estoque = %s
            WHERE id = %s;
        """, (nome, preco, estoque, id))

        if cursor.rowcount == 0:
            return jsonify({"error": "Produto não encontrado"}), 404

        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({"message": "Produto atualizado com sucesso!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/produtos/<int:id>', methods=['DELETE'])
def excluir_produto(id):
    try:
        connection = create_connection()
        cursor = connection.cursor()

        cursor.execute("DELETE FROM produtos WHERE id = %s;", (id,))

        if cursor.rowcount == 0:
            return jsonify({"error": "Produto não encontrado"}), 404

        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({"message": "Produto excluído com sucesso!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
