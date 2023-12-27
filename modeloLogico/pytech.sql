CREATE DATABASE PyTech DEFAULT CHARACTER SET utf8;
USE PyTech;

create table 'Produto' (
    'Id_Produto' int not null AUTO_INCREMENT primary key,
    'Nome_Produto' varchar(500) not null,
    'Preco' varchar(45) not null,
    'Descricao' varchar(1000) not null default ''
);

create table 'Fornecedor' (
    'Id_Fornecedor' int not null AUTO_INCREMENT primary key,
    'Razao_Social' varchar(45) not null,
    'Email' varchar(255) not null,
    'CNPJ' varchar(45) not null,
    'Inscricao_Estadual' varchar(45) not null
);

create table 'Cliente' (
    'Id_Cliente' int not null AUTO_INCREMENT primary key,
    'CPF' varchar(45) not null,
    'Email' varchar(45) not null,
    'Senha' varchar(45) not null
);

create table 'Telefone' (
    'Id_Telefone' int not null AUTO_INCREMENT primary key,
    'Id_Cliente' int null,
    'Id_Fornecedor' int null,
    foreign key(Id_Cliente) references Cliente(ID_Cliente),
    foreign key(Id_Fornecedor) references Fornecedor(Id_Fornecedor),
);

create table 'Endereco' (
    'Id_Endereco' int not null AUTO_INCREMENT primary key,
    'Cidade' varchar(45) not null,
    'Bairro' varchar(45) not null,
    'Estado' varchar(45) not null,
    'Rua' varchar(45) not null,
    'Numero_Casa' int not null,
    'Id_Cliente' int null,
    'Id_Fornecedor' int null,
    foreign key(Id_Cliente) references Cliente(Id_Cliente),
    foreign key(Id_Fornecedor) references Fornecedor(Id_Fornecedor)
)

create table 'Carrinho' (
    'Id_Carrinho' int not null AUTO_INCREMENT primary key,
    'Id_Cliente' int not null,
    foreign key(Id_Cliente) references Cliente(Id_Cliente)
)