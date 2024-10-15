
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


class Emprestimo:
    MAX_LIVROS = 3  # Limite de livros por usuário
    PRAZO_DEVOLUCAO = 14  # Prazo de devolução em dias

    def __init__(self, livro, usuario):
        self.livro = livro
        self.usuario = usuario
        self.data_emprestimo = date.today()
        self.data_devolucao = self.data_emprestimo + timedelta(days=self.PRAZO_DEVOLUCAO)

    def __str__(self):
        return (f"Livro: {self.livro.titulo}, Usuário: {self.usuario.nome}, "
                f"Emprestado em: {self.data_emprestimo}, Devolver até: {self.data_devolucao}")


class Biblioteca:

    def __init__(self):
        self.livros = {}       # Dicionário de livros com id_livro como chave
        self.usuarios = {}     # Dicionário de usuários com id_usuario como chave
        self.emprestimos = []  # Lista de empréstimos ativos


    # Métodos para gerenciar livros
    def adicionar_livro(self, livro):
        if livro.id_livro in self.livros:
            print(f"Livro com ID {livro.id_livro} já existe.")
        else:
            self.livros[livro.id_livro] = livro
            print(f"Livro '{livro.titulo}' adicionado com sucesso.")

    def remover_livro(self, id_livro):
        livro = self.livros.get(id_livro)
        if livro:
            if livro.disponivel:
                del self.livros[id_livro]
                print(f"Livro ID {id_livro} removido com sucesso.")
            else:
                print("Não é possível remover um livro que está emprestado.")
        else:
            print(f"Livro com ID {id_livro} não encontrado.")

    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro na biblioteca.")
        else:
            print(f"self.livros = {self.livros}")
            for livro in self.livros.values():
                print(livro)

    # Métodos para gerenciar usuários
    def adicionar_usuario(self, usuario):
        if usuario.id_usuario in self.usuarios:
            print(f"Usuário com ID {usuario.id_usuario} já existe.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            print(f"Usuário '{usuario.nome}' adicionado com sucesso.")

    def listar_usuarios(self):
        if not self.usuarios:
            print("Nenhum usuário registrado.")
        else:
            for usuario in self.usuarios.values():
                print(usuario)

    # Métodos para gerenciar empréstimos
    def emprestar_livro(self, id_livro, id_usuario):
        livro = self.livros.get(id_livro)
        usuario = self.usuarios.get(id_usuario)

        if not livro:
            print(f"Livro com ID {id_livro} não encontrado.")
            return
        if not usuario:
            print(f"Usuário com ID {id_usuario} não encontrado.")
            return
        if not livro.disponivel:
            print(f"Livro '{livro.titulo}' não está disponível para empréstimo.")
            return
        if len(usuario.livros_emprestados) >= Emprestimo.MAX_LIVROS:
            print(f"Usuário '{usuario.nome}' atingiu o limite de empréstimos.")
            return

        emprestimo = Emprestimo(livro, usuario)
        self.emprestimos.append(emprestimo)
        usuario.livros_emprestados.append(emprestimo)
        livro.disponivel = False
        print(f"Livro '{livro.titulo}' emprestado para '{usuario.nome}'. Devolução até {emprestimo.data_devolucao}.")

    def devolver_livro(self, id_livro, id_usuario):
        usuario = self.usuarios.get(id_usuario)
        if not usuario:
            print(f"Usuário com ID {id_usuario} não encontrado.")
            return

        emprestimo_encontrado = None
        for emprestimo in usuario.livros_emprestados:
            if emprestimo.livro.id_livro == id_livro:
                emprestimo_encontrado = emprestimo
                break

        if emprestimo_encontrado:
            usuario.livros_emprestados.remove(emprestimo_encontrado)
            self.emprestimos.remove(emprestimo_encontrado)
            emprestimo_encontrado.livro.disponivel = True
            print(f"Livro '{emprestimo_encontrado.livro.titulo}' devolvido por '{usuario.nome}'.")

    def listar_emprestimos(self):
        if not self.emprestimos:
            print("Nenhum empréstimo ativo.")
        else:
            for emprestimo in self.emprestimos:
                print(emprestimo)
