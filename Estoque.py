from datetime import date, datetime

class Estoque():

    def __init__(self):
        self.codigo = int(input('Codigo do produto a ser estocado: '))
        self.quantidade = int(input('Quantidade: '))
        self.data_entrada = datetime.now()
        data = date.today()
        self.validade = date.fromordinal(data.toordinal() + 90)  # hoje mais 90 dias