class Endereco():

    def __init__(self):
        self.cnpj = input('Informe CNPJ do fornecedor: ')
        self.rua = input('Rua: ')
        self.numero = int(input('Número: '))
        self.bairro = input('Bairro: ')
        self.cidade = input('Cidade: ')
        self.estado = input('Estado: ')
        self.cep = input('CEP: ')