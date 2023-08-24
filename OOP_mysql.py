import mysql.connector
import psutil

class Banco():
    def __init__(self, localhost, name, password, database = None):
        self.localhost = localhost
        self.name = name
        self.password = password
        self.database = database

        if database == None:
            self.database = mysql.connector.connect(
                host=self.localhost,
                user=self.name,
                password=self.password
            )

        else:
            self.database = mysql.connector.connect(
                host=self.localhost,
                user=self.name,
                password=self.password,
                database=self.database
            )

        self.cursor = self.database.cursor()

    def criar_banco(self, nome_banco):
        self.sql = "CREATE DATABASE %s"%nome_banco
        self.cursor.execute(self.sql)

    def use_banco(self, nome_banco):
        self.database = nome_banco

        self.database = mysql.connector.connect(
            host=self.localhost,
            user=self.name,
            password=self.password,
            database=self.database
        )

banco = Banco("localhost", "xxxxx", "xxxxx")

banco.use_banco("teste")