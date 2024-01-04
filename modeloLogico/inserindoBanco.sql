use pytech;

-- Inserindo fornecedores na tabela Fornecedor
INSERT INTO Fornecedor (razao_social, email, cnpj, senha, inscricao_estadual, descricao) VALUES ('Fornecedor 1', 'fornecedor1@email.com', '12345678901234', 'senha1', '1234567890', 'Descrição do Fornecedor 1');
INSERT INTO Fornecedor (razao_social, email, cnpj, senha, inscricao_estadual, descricao) VALUES ('Fornecedor 2', 'fornecedor2@email.com', '23456789012345', 'senha2', '2345678901', 'Descrição do Fornecedor 2');
INSERT INTO Fornecedor (razao_social, email, cnpj, senha, inscricao_estadual, descricao) VALUES ('Fornecedor 3', 'fornecedor3@email.com', '34567890123456', 'senha3', '3456789012', 'Descrição do Fornecedor 3');

-- Inserindo clientes na tabela Cliente
INSERT INTO Cliente (nome, sobrenome, cpf, email, senha) VALUES ('Cliente', '1', '12345678901', 'cliente1@email.com', 'senha1');
INSERT INTO Cliente (nome, sobrenome, cpf, email, senha) VALUES ('Cliente', '2', '23456789012', 'cliente2@email.com', 'senha2');
INSERT INTO Cliente (nome, sobrenome, cpf, email, senha) VALUES ('Cliente', '3', '34567890123', 'cliente3@email.com', 'senha3');

-- Inserindo produtos na tabela Produto
INSERT INTO Produto (nome_produto, preco, id_fornecedor, descricao) VALUES ('Produto 1', '100', 1, 'Descrição do Produto 1');
INSERT INTO Produto (nome_produto, preco, id_fornecedor, descricao) VALUES ('Produto 2', '200', 2, 'Descrição do Produto 2');
INSERT INTO Produto (nome_produto, preco, id_fornecedor, descricao) VALUES ('Produto 3', '300', 3, 'Descrição do Produto 3');

-- Inserindo carrinhos na tabela Carrinho
INSERT INTO Carrinho (id_cliente) VALUES (1);
INSERT INTO Carrinho (id_cliente) VALUES (2);
INSERT INTO Carrinho (id_cliente) VALUES (3);

-- Inserindo produtos no carrinho na tabela Carrinho_has_Produto
INSERT INTO Carrinho_has_Produto (id_carrinho, id_produto, quantidade, valor_total) VALUES (1, 1, 2, '200');
INSERT INTO Carrinho_has_Produto (id_carrinho, id_produto, quantidade, valor_total) VALUES (2, 2, 3, '600');
INSERT INTO Carrinho_has_Produto (id_carrinho, id_produto, quantidade, valor_total) VALUES (3, 3, 1, '300');
