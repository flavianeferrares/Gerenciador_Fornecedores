import mysql.connector

from mysql.connector import errorcode

class Banco_Dados():
    def __init__(self, database = "trabalho_gestor_fornecedores"):
        self.host = input('Digite o nome do host: ')
        self.user = input('Digite o nome do usuario: ')
        self. password = input('Digite a senha: ')
        self.database = database

    def conecta(self):
        try:
            self.conexao_bd = mysql.connector.connect(host= self.host, user= self.user, password= self.password,
                                                 database= self.database)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('Nome de usuário ou senha incorretos!')
            elif err.errno == errorcode.ER_BAD_ERROR:
                print('Banco de dados não existe!')
            else:
                print(err)

        self.cur = self.conexao_bd.cursor()

    def desconecta(self):
        self.cur.close()
        self.conexao_bd.close()

    def pesquisa(self, sql):
        try:
            self.conecta()
            self.cur.execute(sql)
            resultado = self.cur.fetchall()
            self.desconecta()
            return resultado
            self.desconecta()
            print("Pesquisa realizada com sucesso!!")
        except mysql.connector.Error as erro:
            print("Falha ao pesquisar: {}".format(erro))

    def deletar(self, sql):
        try:
            self.conecta()
            self.cur.execute(sql)
            self.conexao_bd.commit()
            self.desconecta()
            print("Remoção realizada com sucesso!!")
        except mysql.connector.Error as erro:
            print("Falha ao remover: {}".format(erro))

    def alterar(self, sql):
        try:
            self.conecta()
            self.cur.execute(sql)
            self.conexao_bd.commit()
            self.desconecta()
            print("Alteração realizada com sucesso!!")
        except mysql.connector.Error as erro:
            print("Falha ao alterar: {}".format(erro))

    def inserir(self,sql, value):
        try:
            self.conecta()
            self.cur.execute(sql,value)
            self.conexao_bd.commit()
            self.desconecta()
            print("Inserido com sucesso!!")
        except mysql.connector.Error as erro:
            print("Falha ao inserir: {}".format(erro))
