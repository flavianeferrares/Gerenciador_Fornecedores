from Compra import Compra
from Estoque import Estoque
from Fornecedor import Fornecedor
from Produto import Produto
from Endereco import Endereco
from BD import Banco_Dados

print("Digite os campos para se conectar ao Banco de Dados:")
dados = Banco_Dados()

a = 22

def MSG_Principal():
    print('=' * 4 + 'MENU PRINCIPAL' + '=' * 4)
    print('''[ 1 ] Fornecedor
[ 2 ] Produto
[ 3 ] Estoque
[ 4 ] Compra
[ 5 ] Endereço
[ 6 ] Sair''')
    print('=' * a)

def MSG_Fornecedor():
    print('=' * 3 + 'MENU FORNECEDOR' + '=' * 3)
    print('''[ 1 ] Cadastrar
[ 2 ] Alterar
[ 3 ] Excluir
[ 4 ] Visualizar tudo
[ 5 ] Visualizar um fornecedor
[ 6 ] Voltar''')
    print('=' * a)

def MSG_Produto():
    print('=' * 3 + 'MENU PRODUTO' + '=' * 3)
    print('''[ 1 ] Cadastrar
[ 2 ] Alterar
[ 3 ] Excluir
[ 4 ] Visualizar tudo
[ 5 ] Visualizar um produto
[ 6 ] Voltar''')
    print('=' * a)

def MSG_Estoque():
    print('=' * 3 + 'MENU ESTOQUE' + '=' * 3)
    print('''[ 1 ] Incluir
[ 2 ] Alterar
[ 3 ] Excluir
[ 4 ] Visualizar tudo
[ 5 ] Visualizar o estoque
[ 6 ] Voltar''')
    print('=' * a)

def MSG_Compra():
    print('=' * 3 + 'MENU COMPRA' + '=' * 3)
    print('''[ 1 ] Comprar
[ 2 ] Alterar
[ 3 ] Excluir
[ 4 ] Visualizar tudo
[ 5 ] Visualizar uma compra
[ 6 ] Voltar''')
    print('=' * a)

def MSG_Endereco():
    print('=' * 3 + 'MENU ENDERECO' + '=' * 3)
    print('''[ 1 ] Cadastrar
[ 2 ] Alterar
[ 3 ] Excluir
[ 4 ] Visualizar tudo
[ 5 ] Visualizar um endereço
[ 6 ] Voltar''')
    print('=' * a)

def Menu_Fornecedor():
    opcao = 0
    while opcao != 6:
        MSG_Fornecedor()
        opcao = int(input('Digite uma opção válida: '))
        if opcao == 1:
            #CADASTRA
            print('Cadastro do fornecedor:')
            forn = Fornecedor()
            sql = "INSERT INTO trabalho_gestor_fornecedores.fornecedor (cnpj, nome, email, telefone, codigo_produto) VALUES (%s,%s,%s,%s,%s)"
            values = (forn.cnpj, forn.nome, forn.email, forn.telefone, forn.codigoProduto)
            dados.inserir(sql, values)

        elif opcao == 2:
            #ALTERAR
            print('Alterando fornecedor:')
            forn = Fornecedor()
            sql = """UPDATE trabalho_gestor_fornecedores.fornecedor SET nome = '"""+forn.nome+"""',email = '"""+forn.email+"""', telefone = '"""+forn.telefone+"""', codigo_produto ="""+str(forn.codigoProduto)+""" WHERE cnpj = '"""+forn.cnpj+"""'"""
            dados.alterar(sql)

        elif opcao == 3:
            # DELETE
            num = input('Digite o CNPJ que deseja excluir: ')
            sql = """DELETE FROM trabalho_gestor_fornecedores.fornecedor WHERE cnpj ='""" + num + """'"""
            dados.deletar(sql)

        elif opcao == 4:
            # VISUALIZAR TODOS
            print('Todos os fornecedores cadastrados:')
            sql = "SELECT * FROM trabalho_gestor_fornecedores.fornecedor"
            resultado = dados.pesquisa(sql)
            for (cnpj, nome, email, telefone, codigo_produto) in resultado:
                print("CNPJ: {}, Nome Fornecedor: {}, Código produto vendido: {}, Email: {}, Telefone: {}".format(cnpj,nome, codigo_produto,email, telefone))

        elif opcao == 5:
            # VISUALIZAR UM
            num = input('Digite o CNPJ do fornecedor que deseja visualizar: ')
            sql = "SELECT * FROM trabalho_gestor_fornecedores.fornecedor WHERE (cnpj = %s)"%(num)
            resultado = dados.pesquisa(sql)
            for (cnpj, nome, email, telefone, codigo_produto) in resultado:
                print("CNPJ: {}, Nome Fornecedor: {}, Código produto vendido: {}, Email: {}, Telefone: {}".format(cnpj,nome, codigo_produto,email, telefone))

        elif opcao == 6:
            print('Voltando para o Menu Principal!')

        else:
            print('Opção inválida!!')

def Menu_Produto():
    opcao = 0
    while opcao != 6:
        MSG_Produto()
        opcao = int(input('Digite uma opção válida: '))
        if opcao == 1:
            #CADASTRA
            print('Cadastro do produto:')
            prod = Produto()
            sql = "INSERT INTO `trabalho_gestor_fornecedores`.`produto` (`codigo`, `tipo_produto`, `nome`, `quantidade`) VALUES (%s,%s,%s,%s)"
            values = (prod.codigo, prod.tipo_produto, prod.nome, prod.quantidade)
            dados.inserir(sql,values)

        elif opcao == 2:
            #ALTERAR
            print('Alterando produto:')
            prod = Produto()
            sql = """UPDATE trabalho_gestor_fornecedores.produto SET tipo_produto ='""" +prod.tipo_produto+"""', nome = '"""+prod.nome+"""', quantidade ="""+str(prod.quantidade)+""" WHERE codigo = """+str(prod.codigo)
            dados.alterar(sql)

        elif opcao == 3:
            #DELETE
            num = input('Digite o código produto que deseja excluir: ')
            sql = """DELETE FROM trabalho_gestor_fornecedores.produto WHERE codigo ='"""+num+"""'"""
            dados.deletar(sql)

        elif opcao == 4:
            #VISUALIZAR TODOS
           print('Todos os produtos cadastrados:')
           sql = "SELECT * FROM trabalho_gestor_fornecedores.produto"
           resultado = dados.pesquisa(sql)
           for (codigo, tipo_produto, nome, quantidade) in resultado:
               print("Nome: {}, Codigo: {}, Tipo Produto: {}, Quantidade: {}".format(nome,codigo,tipo_produto,quantidade))

        elif opcao == 5:
            #VISUALIZAR UM
            num = input('Digite o código produto que deseja visualizar: ')
            sql = "SELECT * FROM trabalho_gestor_fornecedores.produto WHERE (codigo = %s)"%(num)
            resultado = dados.pesquisa(sql)
            for (codigo, tipo_produto, nome, quantidade) in resultado:
                print("Nome: {}, Codigo: {}, Tipo Produto: {}, Quantidade: {}".format(nome, codigo, tipo_produto,quantidade))

        elif opcao == 6:
            print('Voltando para o Menu Principal!')
        else:
            print('Opção inválida!!')

def Menu_Estoque():
    opcao = 0
    while opcao != 6:
        MSG_Estoque()
        opcao = int (input('Digite uma opção válida: '))
        if opcao == 1:
            # CADASTRA
            print('Cadastro do estoque:')
            est = Estoque()
            sql = "INSERT INTO trabalho_gestor_fornecedores.estoque (codigo, quantidade, data_entrada, validade) VALUES (%s,%s,%s,%s)"
            values = (est.codigo, est.quantidade, est.data_entrada, est.validade)
            dados.inserir(sql, values)

        elif opcao == 2:
            # ALTERAR
            print('Alterando estoque:')
            est = Estoque()
            sql = """UPDATE trabalho_gestor_fornecedores.estoque SET quantidade = """+str(est.quantidade)+""" WHERE codigo = """+str(est.codigo)+""""""
            dados.alterar(sql)

        elif opcao == 3:
            #DELETE
            num = input('Digite o código do produto que deseja excluir do estoque: ')
            sql = """DELETE FROM trabalho_gestor_fornecedores.estoque WHERE codigo ='"""+num+"""'"""
            dados.deletar(sql)

        elif opcao == 4:
            # VISUALIZAR TODOS
            print('Todo o estoque cadastrado:')
            sql = "SELECT P.nome, P.tipo_produto, Q.codigo, Q.quantidade, Q.data_entrada, Q.validade FROM produto P, estoque Q WHERE P.codigo = Q.codigo"
            resultado = dados.pesquisa(sql)
            for (nome, tipo_produto,codigo, quantidade, data_entrada, validade) in resultado:
                print("Nome: {},Tipo Produto: {},Codigo: {}, Quantidade: {}, data_entrada: {}, validade: {}".format(nome, tipo_produto,codigo, quantidade, data_entrada.strftime('%d/%m/%y'), validade.strftime('%d/%m/%y')))

        elif opcao == 5:
            #VISUALIZAR UM
            num = int(input('Digite o código do produto em estoque que deseja visualizar: '))
            sql = "SELECT P.nome, P.tipo_produto, Q.codigo, Q.quantidade, Q.data_entrada, Q.validade FROM produto P, estoque Q WHERE Q.codigo = """+str(num)+""" AND P.codigo = """+str(num)+""""""
            resultado = dados.pesquisa(sql)
            for (nome, tipo_produto, codigo, quantidade, data_entrada, validade) in resultado:
                print(
                    "Nome: {},Tipo Produto: {},Codigo: {}, Quantidade: {}, data_entrada: {}, validade: {}".format(nome,tipo_produto,codigo,quantidade,data_entrada.strftime('%d/%m/%y'), validade.strftime('%d/%m/%y')))

        elif opcao == 6:
            print('Voltando para o Menu Principal!')
        else:
            print('Opção inválida!!')

def Menu_Compra():
    opcao = 0
    while opcao != 6:
        MSG_Compra()
        opcao = int(input('Digite uma opção válida: '))
        if opcao == 1:
            # CADASTRA
            print('Cadastro da compra:')
            compra = Compra()
            sql = "INSERT INTO trabalho_gestor_fornecedores.compra (codigo, codigo_fornecedor, tipo_pagamento, valor, descricao, quantidade, valor_unitario, data_compra) VALUES (%s,%s,%s,%s, %s, %s, %s,%s)"
            values = (compra.codigo, compra.CNPJ, compra.tipo_pag, compra.valor, compra.descricao, compra.qtd, compra.valor_unit, compra.data_compra)
            dados.inserir(sql, values)

        elif opcao == 2:
            #ALTERAR
            print('Alterando compra:')
            cod = input('Digite o código da compra a ser alterada: ')
            qnt = (input('Digite a nova quantidade: '))
            sql = """UPDATE trabalho_gestor_fornecedores.compra SET quantidade = """+str(qnt)+""" WHERE codigo = """+str(cod)+""""""
            dados.alterar(sql)

        elif opcao == 3:
            #DELETE
            num = input('Digite o código da compra que deseja excluir: ')
            sql = """DELETE FROM trabalho_gestor_fornecedores.compra WHERE codigo ='"""+num+"""'"""
            dados.deletar(sql)

        elif opcao == 4:
            # VISUALIZAR TODOS
            print('Todos as compras cadastradas:')
            sql = "SELECT * FROM trabalho_gestor_fornecedores.compra"
            resultado = dados.pesquisa(sql)
            for (codigo, codigo_fornecedor, tipo_pagamento,valor, descricao, quantidade, valor_unitario, data_compra) in resultado:
                print("Codigo Compra: {},CNPJ Fornecedor: {},Forma de pagamento: {}, Valor: {}, Descrição: {}, Quantidade: {}, Valor Unitário: {},Data da Compra: {}".format(codigo,codigo_fornecedor,tipo_pagamento, valor, descricao, quantidade, valor_unitario, data_compra.strftime('%d/%m/%y')))

        elif opcao == 5:
            # VISUALIZAR UM
            num = input('Digite o código produto que deseja visualizar: ')
            sql = "SELECT * FROM trabalho_gestor_fornecedores.compra WHERE (codigo = %s)" % (num)
            resultado = dados.pesquisa(sql)
            for (codigo, codigo_fornecedor, tipo_pagamento,valor, descricao, quantidade, valor_unitario, data_compra) in resultado:
                print("Codigo Compra: {},CNPJ Fornecedor: {},Forma de pagamento: {}, Valor: {}, Descrição: {}, Quantidade: {}, Valor Unitário: {},Data da Compra: {}".format(codigo,codigo_fornecedor,tipo_pagamento, valor, descricao, quantidade, valor_unitario, data_compra.strftime('%d/%m/%y')))

        elif opcao == 6:
            print('Voltando para o Menu Principal!')
        else:
            print('Opção inválida!!')

def Menu_Endereco():
    opcao = 0
    while opcao != 6:
        MSG_Endereco()
        opcao = int(input('Digite uma opção válida: '))
        if opcao == 1:
            # CADASTRA
            print('Cadastro de endereço:')
            endereco = Endereco()
            sql = "INSERT INTO trabalho_gestor_fornecedores.endereco (cnpj, rua, numero, bairro, cidade, estado, cep) VALUES (%s,%s,%s,%s, %s, %s, %s)"
            values = (endereco.cnpj, endereco.rua, endereco.numero, endereco.bairro, endereco.cidade, endereco.estado, endereco.cep)
            dados.inserir(sql, values)

        elif opcao == 2:
            #ALTERAR
            print('Alterando endereço:')
            endereco = Endereco()
            sql = """UPDATE trabalho_gestor_fornecedores.endereco SET rua= '"""+endereco.rua+"""', numero= """+str(endereco.numero)+""", bairro= '"""+endereco.bairro+"""', cidade = '"""+endereco.cidade+"""', estado = '"""+endereco.estado+"""', cep= '"""+endereco.cep+"""'WHERE cnpj = '"""+endereco.cnpj+"""'"""
            #sql = """UPDATE trabalho_gestor_fornecedores.compra SET rua'"""+endereco+"""'WHERE codigo = '"""+cnpj+"""'"""
            dados.alterar(sql)

        elif opcao == 3:
            #DELETE
            num = input('Digite o código da compra que deseja excluir: ')
            sql = """DELETE FROM trabalho_gestor_fornecedores.compra WHERE codigo ='"""+num+"""'"""
            dados.deletar(sql)

        elif opcao == 4:
            # VISUALIZAR TODOS
            print('Todos os endereços cadastrados:')
            sql = "SELECT * FROM trabalho_gestor_fornecedores.endereco"
            resultado = dados.pesquisa(sql)
            for (cnpj, rua, numero, bairro, cidade, estado, cep) in resultado:
                print("CNPJ: {}, Rua: {}, N°: {}, Bairro: {}, Cidade: {}, Estado: {}, CEP: {}".format(cnpj, rua, numero, bairro, cidade, estado, cep))

        elif opcao == 5:
            # VISUALIZAR UM
            num = input('Informe o CNPJ vinculado ao endereço: ')
            sql = "SELECT * FROM trabalho_gestor_fornecedores.endereco WHERE (cnpj = %s)" % (num)
            resultado = dados.pesquisa(sql)
            for (cnpj, rua, numero, bairro, cidade, estado, cep) in resultado:
                print("CNPJ: {}, Rua: {}, N°: {}, Bairro: {}, Cidade: {}, Estado: {}, CEP: {}".format(cnpj, rua, numero, bairro, cidade, estado, cep))

        elif opcao == 6:
            print('Voltando para o Menu Principal!')

        else:
            print('Opção inválida!!')




















def Menu_Principal():
    opcao = 0
    while opcao != 6:
        MSG_Principal()
        opcao = int (input('Digite uma opção válida: '))
        if opcao == 1:
            Menu_Fornecedor()
        elif opcao == 2:
            Menu_Produto()
        elif opcao == 3:
            Menu_Estoque()
        elif opcao == 4:
            Menu_Compra()
        elif opcao == 5:
            Menu_Endereco()
        elif opcao == 6:
            print('Saindo do programa!')
        else:
            print('Opção inválida!!')

Menu_Principal()