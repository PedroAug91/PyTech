CREATE DATABASE if not exists PyTech DEFAULT CHARACTER SET utf8;
USE PyTech;

create table Fornecedor (
    id_fornecedor int not null AUTO_INCREMENT primary key,
    razao_social varchar(45) not null,
    email varchar(255) not null,
    cnpj varchar(45) not null,
    senha varchar(45) not null,
    inscricao_estadual varchar(45) not null,
    descricao varchar(500) not null default '',
    constraint email_unico unique (email),
    constraint cnpj_unico unique (cnpj)
);

create table Produto (
    id_produto int not null AUTO_INCREMENT primary key,
    nome_produto varchar(500) not null,
    preco varchar(45) not null,
    id_fornecedor int not null,
    descricao varchar(1000) not null default '',
    constraint nome_unico unique (nome_produto),
    foreign key(id_fornecedor) references Fornecedor(id_fornecedor)
);

create table Cliente (
    id_cliente int not null AUTO_INCREMENT primary key,
    nome varchar(100) not null,
    sobrenome varchar(100) not null,
    cpf varchar(45) not null,
    email varchar(45) not null,
    senha varchar(45) not null,
    constraint email_unico unique (email),
    constraint cpf_unico unique (cpf)
);

create table Telefone (
    id_telefone int not null AUTO_INCREMENT primary key,
    id_cliente int null,
    id_fornecedor int null,
    telefone varchar(15) not null,
    foreign key(id_cliente) references Cliente(id_cliente),
    foreign key(id_fornecedor) references Fornecedor(id_fornecedor)
);

create table Endereco (
    id_endereco int not null AUTO_INCREMENT primary key,
    cidade varchar(45) not null,
    bairro varchar(45) not null,
    estado varchar(45) not null,
    rua varchar(45) not null,
    numero_casa int not null,
    id_cliente int null,
    id_fornecedor int null,
    foreign key(id_cliente) references Cliente(id_cliente),
    foreign key(id_fornecedor) references Fornecedor(id_fornecedor)
);

create table Carrinho (
    id_carrinho int not null AUTO_INCREMENT primary key,
    id_cliente int not null,
    foreign key(id_cliente) references Cliente(id_cliente)
);

create table Carrinho_has_Produto (
    id_carrinho_has_produto int not null primary key,
    id_carrinho int not null,
    id_produto int not null,
    quantidade int not null,
    valor_total varchar(45) not null,
    foreign key(id_carrinho) references Carrinho(id_carrinho),
    foreign key(id_produto) references Produto(id_produto)
);

create table Venda (
    id_venda int not null AUTO_INCREMENT primary key,
    data_compra varchar(45) not null,
    id_carrinho_has_produto int not null,
    foreign key(id_carrinho_has_produto) references Carrinho_has_Produto(id_carrinho_has_produto)
);

create table Imagem_Produto (
    id_imagem_produto int not null AUTO_INCREMENT primary key,
    caminho varchar(500) not null,
    id_produto int not null,
    foreign key(id_produto) references Produto(id_produto)
);

create table Imagem_Fornecedor (
    id_imagem_fornecedor int not null AUTO_INCREMENT primary key,
    caminho varchar(500) not null,
    id_fornecedor int not null,
    foreign key(id_fornecedor) references Fornecedor(id_fornecedor)
);

create table Estoque (
    id_estoque int not null AUTO_INCREMENT primary key,
    quantidade int not null,
    id_fornecedor int not null,
    id_produto int not null,
    foreign key(id_fornecedor) references Fornecedor(id_fornecedor),
    foreign key(id_produto) references Produto(id_produto)
);

create table Categoria (
    id_categoria int not null AUTO_INCREMENT primary key,
    nome varchar(45) not null,
    descricao varchar(45) not null
);

create table Categoria_Produto (
    id_categoria_produto int not null AUTO_INCREMENT primary key,
    id_produto int not null,
    id_categoria int not null,
    foreign key(id_produto) references Produto(id_produto),
    foreign key(id_categoria) references Categoria(id_categoria)
)
