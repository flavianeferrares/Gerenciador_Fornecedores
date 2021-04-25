class Fornecedor():

    def __init__(self):
        self.cnpj = input('Informe o CNPJ: ')
        self.nome = input('Nome fornecedor: ')
        self.email = input('Email: ')
        self.telefone = input('Telefone: ')
        self.codigoProduto = int(input('Digite o codigo do produto fornecido: '))