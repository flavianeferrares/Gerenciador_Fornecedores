USE trabalho_gestor_fornecedores;

INSERT INTO produto(codigo, tipo_produto, nome, quantidade) VALUES (1, "Doce",  "Paçoca", 100);
INSERT INTO produto(codigo, tipo_produto, nome, quantidade) VALUES (2, "Doce",  "Goiabada", 300);
INSERT INTO produto(codigo, tipo_produto, nome, quantidade) VALUES (3, "Chocolate", "Garoto", 150);
INSERT INTO produto(codigo, tipo_produto, nome, quantidade) VALUES (4, "Bala",  "Haribo Banana", 50);
INSERT INTO produto(codigo, tipo_produto, nome, quantidade) VALUES (5, "Bala",  "Haribo Dentinhos", 100);
SELECT * FROM produto;

INSERT INTO fornecedor(cnpj, nome, email, telefone, codigo_produto) VALUE ("11111111111", "Leo", "leo@gmail.com", "38551111", 1); 
INSERT INTO fornecedor(cnpj, nome, email, telefone, codigo_produto) VALUE ("55555555555", "Jose", "jose@gmail.com", "38552222", 5);
INSERT INTO fornecedor(cnpj, nome, email, telefone, codigo_produto) VALUE ("22222222222", "Marcela", "marcela@gmail.com", "38553333", 2);
INSERT INTO fornecedor(cnpj, nome, email, telefone, codigo_produto) VALUE ("33333333333", "Maria", "maria@gmail.com", "38554444", 3);
INSERT INTO fornecedor(cnpj, nome, email, telefone, codigo_produto) VALUE ("44444444444", "Luna", "luna@gmail.com", "385555", 4);
SELECT * FROM fornecedor;

INSERT INTO estoque(codigo, quantidade, data_entrada, validade) VALUE (1, 100, "2021-03-20", "2024-03-24");
INSERT INTO estoque(codigo, quantidade, data_entrada, validade) VALUE (2, 300, "2021-03-20", "2023-03-24");
INSERT INTO estoque(codigo, quantidade, data_entrada, validade) VALUE (3, 150, "2021-03-20", "2024-05-24");
INSERT INTO estoque(codigo, quantidade, data_entrada, validade) VALUE (4, 50, "2021-03-20", "2021-12-24");
INSERT INTO estoque(codigo, quantidade, data_entrada, validade) VALUE (5, 100, "2021-03-20", "2024-03-24");
SELECT * FROM estoque;

INSERT INTO endereco(cnpj, rua, numero, bairro, cidade, estado, cep) VALUE ("11111111111", "A", 10, "Centro", "Alvinópolis", "MG", "35950000");
INSERT INTO endereco(cnpj, rua, numero, bairro, cidade, estado, cep) VALUE ("22222222222", "B", 20, "Centro", "Alvinópolis", "MG", "35950000");
INSERT INTO endereco(cnpj, rua, numero, bairro, cidade, estado, cep) VALUE ("33333333333", "C", 30, "Centro", "Alvinópolis", "MG", "35950000");
INSERT INTO endereco(cnpj, rua, numero, bairro, cidade, estado, cep) VALUE ("44444444444", "D", 40, "Centro", "Alvinópolis", "MG", "35950000");
INSERT INTO endereco(cnpj, rua, numero, bairro, cidade, estado, cep) VALUE ("55555555555", "C", 30, "Centro", "Alvinópolis", "MG", "35950000");
SELECT * FROM endereco;


INSERT INTO compra(codigo, codigo_fornecedor, tipo_pagamento, valor, descricao, quantidade, valor_unitario, data_compra) VALUE (1, "11111111111", "Debito", 100.0, "compra de paçocas", 100, 1, "2021-03-28");
INSERT INTO compra(codigo, codigo_fornecedor, tipo_pagamento, valor,  descricao, quantidade, valor_unitario, data_compra) VALUE (2, "22222222222", "Credito", 300.0, "compra de goiabada", 300, 15, "2021-03-28");
INSERT INTO compra(codigo, codigo_fornecedor, tipo_pagamento, valor,  descricao, quantidade, valor_unitario, data_compra) VALUE (3, "33333333333", "Dinheiro", 150.0, "compra de chocolate marca garoto", 150, 12, "2021-03-28");
INSERT INTO compra(codigo, codigo_fornecedor, tipo_pagamento, valor,  descricao, quantidade, valor_unitario, data_compra) VALUE (4, "44444444444", "Debito", 50.0, "compra de balas Haribo", 50, 11, "2021-03-28");
INSERT INTO compra(codigo, codigo_fornecedor, tipo_pagamento, valor,  descricao, quantidade, valor_unitario, data_compra) VALUE (5, "55555555555", "Debito", 100.0,  "compra de balas Haribo", 100,  25, "2021-03-28");
SELECT * FROM compra;
