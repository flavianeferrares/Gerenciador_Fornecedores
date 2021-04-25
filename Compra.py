from datetime import datetime

class Compra():

    def __init__(self):
        self.codigo = int (input('Informe o codigo da compra: '))
        self.CNPJ = int(input('Informe o CNPJ do fornecedor: '))
        self.tipo_pag = input('Informe a forma de pagamento:')
        self.valor = float(input('Valor Total: '))
        self.descricao = input('Descrição: ')
        self.qtd = int(input('Quantidade comprada: '))
        v = self.valor/self.qtd
        self.valor_unit = v
        self.data_compra = datetime.now()