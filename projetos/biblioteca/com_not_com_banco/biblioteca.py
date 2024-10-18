from datetime import date, timedelta
from tinydb import TinyDB, Query

class Livro:
    def __init__(self, id_livro, titulo, autor, ano_publicacao, disponivel=True):
        self.id_livro = id_livro
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = disponivel

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"ID: {self.id_livro}, Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano_publicacao}, Status: {status}"

    def to_dict(self):
        return vars(self)

class Usuario:
    def __init__(self, id_usuario, nome, email, livros_emprestados=None):
        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email
        self.livros_emprestados = livros_emprestados or []

    def __str__(self):
        return f"ID: {self.id_usuario}, Nome: {self.nome}, Email: {self.email}"

    def to_dict(self):
        return vars(self)

class Emprestimo:
    MAX_LIVROS = 3
    PRAZO_DEVOLUCAO = 14

    def __init__(self, livro, usuario):
        self.livro = livro
        self.usuario = usuario
        self.data_emprestimo = date.today()
        self.data_devolucao = self.data_emprestimo + timedelta(days=self.PRAZO_DEVOLUCAO)

    def __str__(self):
        return (f"Livro: {self.livro.titulo}, Usuário: {self.usuario.nome}, "
                f"Emprestado em: {self.data_emprestimo}, Devolver até: {self.data_devolucao}")

    def to_dict(self):
        return {
            "livro": self.livro.to_dict(),
            "usuario": self.usuario.to_dict(),
            "data_emprestimo": str(self.data_emprestimo),
            "data_devolucao": str(self.data_devolucao),
        }

class Biblioteca:
    def __init__(self, notificador):
        self.db = TinyDB('biblioteca.json')
        self.notificador = notificador

    def adicionar_livro(self, livro):
        if self.db.table('livros').contains(Query().id_livro == livro.id_livro):
            print(f"Livro com ID {livro.id_livro} já existe.")
        else:
            self.db.table('livros').insert(livro.to_dict())
            print(f"Livro '{livro.titulo}' adicionado com sucesso.")

    def remover_livro(self, id_livro):
        if self.db.table('livros').remove(Query().id_livro == id_livro):
            print(f"Livro ID {id_livro} removido com sucesso.")
        else:
            print(f"Livro com ID {id_livro} não encontrado.")

    def listar_livros(self):
        livros = self.db.table('livros').all()
        if not livros:
            print("Nenhum livro na biblioteca.")
        else:
            for livro in livros:
                print(Livro(**livro))

    def adicionar_usuario(self, usuario):
        if self.db.table('usuarios').contains(Query().id_usuario == usuario.id_usuario):
            print(f"Usuário com ID {usuario.id_usuario} já existe.")
        else:
            self.db.table('usuarios').insert(usuario.to_dict())
            print(f"Usuário '{usuario.nome}' adicionado com sucesso.")

    def listar_usuarios(self):
        usuarios = self.db.table('usuarios').all()
        if not usuarios:
            print("Nenhum usuário registrado.")
        else:
            for usuario in usuarios:
                print(Usuario(**usuario))

    def emprestar_livro(self, id_livro, id_usuario):
        livro_data = self.db.table('livros').get(Query().id_livro == id_livro)
        usuario_data = self.db.table('usuarios').get(Query().id_usuario == id_usuario)

        if not livro_data or not usuario_data:
            print("Livro ou usuário não encontrado.")
            return

        livro = Livro(**livro_data)
        usuario = Usuario(**usuario_data)

        if not livro.disponivel:
            print(f"Livro '{livro.titulo}' não está disponível para empréstimo.")
            return
        if len(usuario.livros_emprestados) >= Emprestimo.MAX_LIVROS:
            print(f"Usuário '{usuario.nome}' atingiu o limite de empréstimos.")
            return

        emprestimo = Emprestimo(livro, usuario)
        self.db.table('emprestimos').insert(emprestimo.to_dict())

        # Atualizar estado do livro
        livro.disponivel = False
        self.db.table('livros').upsert(livro.to_dict(), Query().id_livro == id_livro)

        print(f"Livro '{livro.titulo}' emprestado para '{usuario.nome}'. Devolução até {emprestimo.data_devolucao}.")

        # Notificação
        assunto = "Confirmação de Empréstimo de Livro"
        mensagem = (f"Olá {usuario.nome},\n\n"
                    f"Você pegou emprestado o livro '{livro.titulo}' em {emprestimo.data_emprestimo}.\n"
                    f"Por favor, devolva o livro até {emprestimo.data_devolucao}.\n\n"
                    "Obrigado por usar a nossa biblioteca!")
        self.notificador.enviar_email(usuario.email, assunto, mensagem)

    def listar_emprestimos(self):
        emprestimos = self.db.table('emprestimos').all()
        if not emprestimos:
            print("Nenhum empréstimo ativo.")
        else:
            for emp in emprestimos:
                emprestimo = Emprestimo(
                    Livro(**emp['livro']),
                    Usuario(**emp['usuario'])
                )
                print(emprestimo)

    def devolver_livro(self, id_livro, id_usuario):
        UsuarioQuery = Query()
        LivroQuery = Query()
        EmprestimoQuery = Query()

        # Verifica se o usuário existe no banco de dados
        usuario_data = self.db.table('usuarios').get(UsuarioQuery.id_usuario == id_usuario)
        if not usuario_data:
            print(f"Usuário com ID {id_usuario} não encontrado.")
            return

        # Verifica se o livro existe no banco de dados
        livro_data = self.db.table('livros').get(LivroQuery.id_livro == id_livro)
        if not livro_data:
            print(f"Livro com ID {id_livro} não encontrado.")
            return

        # Busca o empréstimo do livro pelo usuário
        emprestimo_data = self.db.table('emprestimos').get(
            (EmprestimoQuery['livro']['id_livro'] == id_livro) & 
            (EmprestimoQuery['usuario']['id_usuario'] == id_usuario)
        )

        if not emprestimo_data:
            print(f"O usuário '{usuario_data['nome']}' não tem o livro com ID {id_livro} emprestado.")
            return

        # Remover o empréstimo do banco
        self.db.table('emprestimos').remove(doc_ids=[emprestimo_data.doc_id])

        # Atualizar o estado do livro para disponível
        self.db.table('livros').update({'disponivel': True}, LivroQuery.id_livro == id_livro)

        # Exibir mensagem de devolução bem-sucedida
        print(f"Livro '{livro_data['titulo']}' devolvido por '{usuario_data['nome']}'.")

        # Enviar notificação da devolução (opcional)
        assunto = "Confirmação de Devolução de Livro"
        mensagem = (f"Olá {usuario_data['nome']},\n\n"
                    f"O livro '{livro_data['titulo']}' foi devolvido com sucesso.\n"
                    "Agradecemos por utilizar nossa biblioteca!\n\n"
                    "Atenciosamente, \nEquipe da Biblioteca")
        self.notificador.enviar_email(usuario_data['email'], assunto, mensagem)
