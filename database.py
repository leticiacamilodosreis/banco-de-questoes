import psycopg2

class Database:
    def __init__(self):
        self.conexao = psycopg2.connect(
            host = "localhost",
            dbname = "banco_questoes",
            user= "postgres",
            password="senha",
        )
        self.cursor = self.conexao.cursor()

    def buscar_questao(self):
        self.cursor.execute("SELECT id, pergunta, resposta_correta FROM questoes")
        return self.cursor.fetchall()

    def fechar_conexao(self):
        self.conexao.close()
