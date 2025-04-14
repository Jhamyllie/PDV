# 🛒 Sistema de Ponto de Venda (PDV)

Este é um sistema simples de **PDV (Ponto de Venda)** desenvolvido com **Python (Flask + PostgreSQL)** no backend e **HTML/CSS/JavaScript** no frontend. Ele permite o gerenciamento completo de produtos com operações de **CRUD (Criar, Ler, Atualizar, Deletar)**.

---

## 🧱 Estrutura do Projeto

```
PDV/
├── backend/
│   ├── app.py
│   ├── db/
│   │   └── db_connection.py
│   ├── criar_tabelas.py
│   └── venv/ (não versionado)
│
├── frontend/
│   ├── index.html
│   ├── index.js
│   └── style.css
```

---

## 🚀 Funcionalidades

- ✅ Cadastrar produtos
- ✅ Listar todos os produtos
- ✅ Atualizar informações de um produto
- ✅ Excluir produtos
- 🔒 Integração com banco de dados PostgreSQL

---

## 🖥️ Tecnologias Utilizadas

### Backend
- Python 3
- Flask
- Flask-CORS
- PostgreSQL
- psycopg2

### Frontend
- HTML5
- CSS3
- JavaScript Vanilla

---

## ⚙️ Como rodar o projeto

### 🔧 Pré-requisitos

- Python 3 instalado
- PostgreSQL instalado e rodando

---

### 📥 Instalação do Backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

> Se ainda não existir um `requirements.txt`, crie com:
> ```bash
> pip freeze > requirements.txt
> ```

---

### 🧠 Configurar o Banco de Dados

Edite o arquivo `db/db_connection.py` com suas credenciais PostgreSQL:

```python
def create_connection():
    return psycopg2.connect(
        host="localhost",
        database="seu_banco",
        user="seu_usuario",
        password="sua_senha"
    )
```

Crie as tabelas executando:

```bash
python criar_tabelas.py
```

---

### ▶️ Rodar o Backend

```bash
python app.py
```

O servidor estará disponível em:

```
http://127.0.0.1:5000
```

---

### 💻 Rodar o Frontend

Abra o arquivo `index.html` na pasta `frontend` diretamente no navegador.

---

## ✍️ Autor

Desenvolvido por **Seu Nome**  
📧 Contato: milli.santana2017@gmail.com

---

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se à vontade para usar, modificar e compartilhar!