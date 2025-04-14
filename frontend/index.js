document.addEventListener('DOMContentLoaded', () => {
    const formProduto = document.getElementById('form-produto');
    const formAtualizar = document.getElementById('form-atualizar');
    const formExcluir = document.getElementById('form-excluir');
    const btnListar = document.getElementById('btn-listar');
    const tabelaProdutos = document.getElementById('tabela-produtos');

    // Cadastrar Produto
    formProduto.addEventListener('submit', (event) => {
        event.preventDefault();

        const nome = document.getElementById('nome').value;
        const preco = document.getElementById('preco').value;
        const estoque = document.getElementById('estoque').value;

        const produto = { nome, preco, estoque };

        fetch('http://127.0.0.1:5000/produtos', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(produto),
        })
            .then((response) => response.json())
            .then((data) => {
                alert(data.message);
                formProduto.reset();
                listarProdutos(); // Atualiza a tabela automaticamente
            })
            .catch((error) => console.error('Erro ao cadastrar produto:', error));
    });

    // Listar Produtos
    function listarProdutos() {
        fetch('http://127.0.0.1:5000/produtos')
            .then((response) => response.json())
            .then((produtos) => {
                const tbody = tabelaProdutos.querySelector('tbody');
                tbody.innerHTML = '';

                produtos.forEach((produto) => {
                    const tr = document.createElement('tr');
                    tr.innerHTML = `
                        <td>${produto.id}</td>
                        <td>${produto.nome}</td>
                        <td>R$ ${parseFloat(produto.preco).toFixed(2)}</td>
                        <td>${produto.estoque}</td>
                        <td>
                            <button class="update" data-id="${produto.id}" data-nome="${produto.nome}" data-preco="${produto.preco}" data-estoque="${produto.estoque}">Atualizar</button>
                            <button class="delete" data-id="${produto.id}">Excluir</button>
                        </td>
                    `;
                    tbody.appendChild(tr);
                });

                // Adiciona os eventos depois de montar a tabela
                adicionarEventosBotoes();
            })
            .catch((error) => console.error('Erro ao listar produtos:', error));
    }

    // Botão para chamar a listagem
    btnListar.addEventListener('click', listarProdutos);

    // Atualizar Produto via formulário
    formAtualizar.addEventListener('submit', (event) => {
        event.preventDefault();

        const id = document.getElementById('id').value;
        const nome = document.getElementById('nome-atualizar').value;
        const preco = document.getElementById('preco-atualizar').value;
        const estoque = document.getElementById('estoque-atualizar').value;

        const produto = { nome, preco, estoque };

        fetch(`http://127.0.0.1:5000/produtos/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(produto),
        })
            .then((response) => response.json())
            .then((data) => {
                alert(data.message);
                formAtualizar.reset();
                listarProdutos(); // Atualiza a tabela automaticamente
            })
            .catch((error) => console.error('Erro ao atualizar produto:', error));
    });

    // Excluir Produto via formulário
    formExcluir.addEventListener('submit', (event) => {
        event.preventDefault();

        const id = document.getElementById('id-excluir').value;

        fetch(`http://127.0.0.1:5000/produtos/${id}`, {
            method: 'DELETE',
        })
            .then((response) => response.json())
            .then((data) => {
                alert(data.message);
                formExcluir.reset();
                listarProdutos(); // Atualiza a tabela automaticamente
            })
            .catch((error) => console.error('Erro ao excluir produto:', error));
    });

    // Eventos dos botões de ação na tabela
    function adicionarEventosBotoes() {
        const botoesAtualizar = document.querySelectorAll('.update');
        const botoesExcluir = document.querySelectorAll('.delete');

        botoesAtualizar.forEach((botao) => {
            botao.addEventListener('click', () => {
                const id = botao.getAttribute('data-id');
                const nome = botao.getAttribute('data-nome');
                const preco = botao.getAttribute('data-preco');
                const estoque = botao.getAttribute('data-estoque');

                // Preenche o formulário de atualização
                document.getElementById('id').value = id;
                document.getElementById('nome-atualizar').value = nome;
                document.getElementById('preco-atualizar').value = preco;
                document.getElementById('estoque-atualizar').value = estoque;
            });
        });

        botoesExcluir.forEach((botao) => {
            botao.addEventListener('click', () => {
                const id = botao.getAttribute('data-id');

                if (confirm('Tem certeza que deseja excluir este produto?')) {
                    fetch(`http://127.0.0.1:5000/produtos/${id}`, {
                        method: 'DELETE',
                    })
                        .then((response) => response.json())
                        .then((data) => {
                            alert(data.message);
                            listarProdutos(); // Atualiza a tabela
                        })
                        .catch((error) => console.error('Erro ao excluir produto:', error));
                }
            });
        });
    }
});
