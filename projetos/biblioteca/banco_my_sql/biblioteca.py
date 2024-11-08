import mysql.connector
from datetime import date, timedelta



class Livro:
    def __init__(self, id_livro, titulo, autor, ano_publicacao):
        self.id_livro = id_livro
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"ID: {self.id_livro}, Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano_publicacao}, Status: {status}"


class Usuario:
    def __init__(self, id_usuario, nome, email):
        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email
        self.livros_emprestados = []  # Lista de empréstimos do usuário

    def __str__(self):
        return f"ID: {self.id_usuario}, Nome: {self.nome}, Email: {self.email}"



class Biblioteca:
    def __init__(self, notificador):
        self.notificador = notificador
        self.conexao = mysql.connector.connect(
            host='localhost',
            user='gustavo',
            password='senha_gustavo',
            database='teste_db'
        )
        self.cursor = self.conexao.cursor()

    # Adicionar Livro ao banco de dados
    def adicionar_livro(self, livro):
        sql = "INSERT INTO livros (titulo, autor, ano_publicacao) VALUES (%s, %s, %s)"
        valores = (livro.titulo, livro.autor, livro.ano_publicacao)
        self.cursor.execute(sql, valores)
        self.conexao.commit()
        print(f"Livro '{livro.titulo}' adicionado com sucesso.")

    def listar_livros(self):
        self.cursor.execute("SELECT * FROM livros")
        livros = self.cursor.fetchall()
        for livro in livros:
            status = "Disponível" if livro[4] else "Emprestado"
            print(f"ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Ano: {livro[3]}, Status: {status}")

    def adicionar_usuario(self, usuario):
        sql = "INSERT INTO usuarios (nome, email) VALUES (%s, %s)"
        valores = (usuario.nome, usuario.email)
        self.cursor.execute(sql, valores)
        self.conexao.commit()
        print(f"Usuário '{usuario.nome}' adicionado com sucesso.")

    def listar_usuarios(self):
        self.cursor.execute("SELECT * FROM usuarios")
        usuarios = self.cursor.fetchall()
        for usuario in usuarios:
            print(f"ID: {usuario[0]}, Nome: {usuario[1]}, Email: {usuario[2]}")

    def emprestar_livro(self, id_livro, id_usuario):
        self.cursor.execute("SELECT disponivel FROM livros WHERE id = %s", (id_livro,))
        disponivel = self.cursor.fetchone()
        if not disponivel or not disponivel[0]:
            print("Livro não disponível para empréstimo.")
            return

        data_emprestimo = date.today()
        data_devolucao = data_emprestimo + timedelta(days=14)
        sql = "INSERT INTO emprestimos (id_livro, id_usuario, data_emprestimo, data_devolucao) VALUES (%s, %s, %s, %s)"
        valores = (id_livro, id_usuario, data_emprestimo, data_devolucao)
        self.cursor.execute(sql, valores)

        self.cursor.execute("UPDATE livros SET disponivel = FALSE WHERE id = %s", (id_livro,))
        self.conexao.commit()
        print(f"Livro {id_livro} emprestado com sucesso!")

    def devolver_livro(self, id_livro):
        self.cursor.execute("DELETE FROM emprestimos WHERE id_livro = %s", (id_livro,))
        self.cursor.execute("UPDATE livros SET disponivel = TRUE WHERE id = %s", (id_livro,))
        self.conexao.commit()
        print(f"Livro {id_livro} devolvido com sucesso.")

    def listar_emprestimos(self):
        self.cursor.execute("SELECT * FROM emprestimos")
        emprestimos = self.cursor.fetchall()
        for emprestimo in emprestimos:
            print(f"ID Livro: {emprestimo[1]}, ID Usuário: {emprestimo[2]}, Data Empréstimo: {emprestimo[3]}, Data Devolução: {emprestimo[4]}")




