import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'db')))

from db_connection import create_connection

# Função para criar produto
def inserir_produto(nome, preco, estoque):
    try:
        connection = create_connection()
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO produtos (nome, preco, estoque)
            VALUES (%s, %s, %s);
        """, (nome, preco, estoque))

        connection.commit()
        print("✅ Produto inserido com sucesso!")

    except Exception as e:
        print(f"❌ Erro ao inserir produto: {e}")

# Função para consultar produtos
def consultar_produtos():
    try:
        connection = create_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM produtos;")
        produtos = cursor.fetchall()

        if produtos:
            print("\nProdutos cadastrados:")
            for produto in produtos:
                print(f"ID: {produto[0]}, Nome: {produto[1]}, Preço: R${produto[2]:.2f}, Estoque: {produto[3]}")
        else:
            print("❌ Nenhum produto encontrado.")

        connection.close()

    except Exception as e:
        print(f"❌ Erro ao consultar produtos: {e}")

# Função para atualizar produto
def atualizar_produto(produto_id, novo_nome=None, novo_preco=None, novo_estoque=None):
    try:
        connection = create_connection()
        cursor = connection.cursor()

        # Verificar se o produto existe
        cursor.execute("SELECT * FROM produtos WHERE id = %s;", (produto_id,))
        produto = cursor.fetchone()

        if produto is None:
            print(f"❌ Produto com ID {produto_id} não encontrado!")
            connection.close()
            return

        # Se o produto existir, podemos proceder com a atualização
        if novo_nome:
            cursor.execute("UPDATE produtos SET nome = %s WHERE id = %s;", (novo_nome, produto_id))
        if novo_preco:
            cursor.execute("UPDATE produtos SET preco = %s WHERE id = %s;", (novo_preco, produto_id))
        if novo_estoque:
            cursor.execute("UPDATE produtos SET estoque = %s WHERE id = %s;", (novo_estoque, produto_id))

        connection.commit()

        print(f"✅ Produto de ID {produto_id} atualizado com sucesso!")
        connection.close()

    except Exception as e:
        print(f"❌ Erro ao atualizar produto: {e}")

# Função para deletar produto
def deletar_produto(produto_id):
    try:
        connection = create_connection()
        cursor = connection.cursor()

        cursor.execute("DELETE FROM produtos WHERE id = %s;", (produto_id,))

        connection.commit()

        if cursor.rowcount > 0:
            print(f"✅ Produto de ID {produto_id} deletado com sucesso!")
        else:
            print(f"❌ Produto com ID {produto_id} não encontrado.")
        
        connection.close()

    except Exception as e:
        print(f"❌ Erro ao deletar produto: {e}")

# Função de menu interativo
def menu():
    while True:
        print("\nEscolha uma opção:")
        print("1 - Criar produto")
        print("2 - Consultar produtos")
        print("3 - Atualizar produto")
        print("4 - Deletar produto")
        print("5 - Sair")

        opcao = input("Digite o número da opção: ")

        if opcao == "1":
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            estoque = int(input("Digite a quantidade em estoque: "))
            inserir_produto(nome, preco, estoque)

        elif opcao == "2":
            consultar_produtos()

        elif opcao == "3":
            produto_id = int(input("Digite o ID do produto a ser atualizado: "))
            novo_nome = input("Novo nome (ou pressione Enter para manter o nome atual): ")
            novo_preco = input("Novo preço (ou pressione Enter para manter o preço atual): ")
            novo_estoque = input("Novo estoque (ou pressione Enter para manter o estoque atual): ")

            if novo_preco:
                novo_preco = float(novo_preco)
            if novo_estoque:
                novo_estoque = int(novo_estoque)

            # Chama a função de atualização com a verificação de ID existente
            atualizar_produto(produto_id, novo_nome or None, novo_preco or None, novo_estoque or None)

        elif opcao == "4":
            produto_id = int(input("Digite o ID do produto a ser deletado: "))
            deletar_produto(produto_id)

        elif opcao == "5":
            print("Saindo...")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
