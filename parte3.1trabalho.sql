CREATE DATABASE trabalho_gestor_fornecedores;

USE trabalho_gestor_fornecedores;

CREATE TABLE produto 
(
    codigo INT UNIQUE NOT NULL,
    tipo_produto VARCHAR(15) NOT NULL,
    nome VARCHAR(40) NOT NULL,
    quantidade INT NOT NULL CHECK (quantidade > 0),
    CONSTRAINT pkproduto PRIMARY KEY (codigo)
);

CREATE TABLE fornecedor (
    cnpj CHAR(14) UNIQUE NOT NULL,
    nome VARCHAR(40) NOT NULL,
    email VARCHAR(40) UNIQUE,
    telefone CHAR(11) UNIQUE,
    codigo_produto INT NOT NULL,
    CONSTRAINT pkfornecedor PRIMARY KEY (cnpj),
    CONSTRAINT fkcod_prod FOREIGN KEY (codigo_produto)
        REFERENCES Produto (codigo)
        ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE estoque 
(
    codigo INT NOT NULL,
    quantidade INT NOT NULL,
    data_entrada DATE,
    validade DATE,
    CONSTRAINT pkestoque PRIMARY KEY (codigo),
    CONSTRAINT fkestoque FOREIGN KEY (codigo)
        REFERENCES produto (codigo)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    CHECK (validade > data_entrada)
);

CREATE TABLE endereco 
(
    cnpj CHAR(14) UNIQUE NOT NULL,
    rua VARCHAR(30) NOT NULL,
    numero INT NOT NULL,
    bairro VARCHAR(20) NOT NULL,
    cidade VARCHAR(20) NOT NULL,
    estado VARCHAR(20) NOT NULL,
    cep VARCHAR(10) NOT NULL,
    CONSTRAINT pkendereco PRIMARY KEY (cnpj),
    CONSTRAINT fkendereco FOREIGN KEY (cnpj)
        REFERENCES fornecedor(cnpj)
        ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE compra
(
	codigo INT UNIQUE NOT NULL,
    codigo_fornecedor CHAR(14) UNIQUE NOT NULL,
    tipo_pagamento VARCHAR(15) NOT NULL,
    valor FLOAT NOT NULL,
    descricao VARCHAR(50),
    quantidade INT NOT NULL,
	valor_unitario FLOAT NOT NULL,
    data_compra DATE NOT NULL,
    CONSTRAINT pkcompra PRIMARY KEY (codigo),
    CONSTRAINT fkcompra FOREIGN KEY (codigo_fornecedor)
		REFERENCES fornecedor(cnpj)
        ON DELETE RESTRICT ON UPDATE CASCADE
    
);