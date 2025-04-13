from db_connection import create_connection

def criar_tabelas():
    try:
        connection = create_connection()
        cursor = connection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            preco NUMERIC(10, 2) NOT NULL,
            estoque INTEGER NOT NULL
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS vendas (
            id SERIAL PRIMARY KEY,
            data TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            total NUMERIC(10, 2) NOT NULL
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS itens_venda (
            id SERIAL PRIMARY KEY,
            venda_id INTEGER REFERENCES vendas(id),
            produto_id INTEGER REFERENCES produtos(id),
            quantidade INTEGER NOT NULL,
            preco_unitario NUMERIC(10, 2) NOT NULL
        );
        """)

        connection.commit()
        print("✅ Tabelas criadas com sucesso!")

    except Exception as e:
        print(f"❌ Erro ao criar tabelas: {e}")

if __name__ == "__main__":
    criar_tabelas()
