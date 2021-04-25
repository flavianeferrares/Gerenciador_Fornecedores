class Produto():

    def __init__(self):
        self.codigo = int(input('Informe codigo do produto: '))
        self.nome = input('Nome produto: ')
        self.tipo_produto = input('Tipo de produto: ')
        self.quantidade = int(input('Quantidade: '))
