import mysql.connector

class Banco():
    def __init__(self, localhost, name, password, database = None):
        self.localhost = localhost
        self.name = name
        self.password = password
        self.database = database

        if database == None:
            self.database_con = mysql.connector.connect(
                host=self.localhost,
                user=self.name,
                password=self.password
            )

        else:
            self.database_con = mysql.connector.connect(
                host=self.localhost,
                user=self.name,
                password=self.password,
                database=self.database
            )

        self.cursor = self.database_con.cursor()

    def create_database(self, nome_banco):
        self.criar = f"CREATE DATABASE IF NOT EXISTS {nome_banco};"
        self.cursor.execute(self.criar)

    def use_database(self, nome_banco):
        self.cursor.execute(f"USE {nome_banco};")

    def insert_into_database(self, tabela, lista_dados):
        string_a_ser_montada = f"INSERT INTO '{tabela}' VALUES ("
        for i in lista_dados:
            if type(i) == int or type(i) == float:
                string_a_ser_montada += f"{i},"
            else:
                string_a_ser_montada += f"'{i}',"

        string_a_ser_montada = string_a_ser_montada.rstrip(string_a_ser_montada[-1])
        string_a_ser_montada += ");"

        self.cursor.execute(string_a_ser_montada)
        self.database_con.commit()

    def create_table(self, nome_tabela, lista_campos, lista_tamanhos = None):
        index_lista_tamanhos = 0
        string_a_ser_montada = f"CREATE TABLE IF NOT EXISTS `{nome_tabela}` ("
        for i in lista_campos:
            if i[-1] == "K":
                string_a_ser_montada += f"{i} INT PRIMARY KEY AUTO_INCREMENT,"
            elif i[-1] == "N":
                string_a_ser_montada += f"{i} INT,"
            elif i[-1] == "V":
                string_a_ser_montada += f"{i} VARCHAR({lista_tamanhos[index_lista_tamanhos]}),"
                index_lista_tamanhos += 1
            elif i[-1] == "F":
                string_a_ser_montada += f"{i} DECIMAL({lista_tamanhos[index_lista_tamanhos]}, {lista_tamanhos[index_lista_tamanhos + 1]}),"
                index_lista_tamanhos += 2
            elif i[-1] == "D":
                string_a_ser_montada += f"{i} DATETIME,"

        string_a_ser_montada = string_a_ser_montada.rstrip(string_a_ser_montada[-1])
        string_a_ser_montada += ");"
        self.cursor.execute(string_a_ser_montada)

