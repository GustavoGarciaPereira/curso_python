from biblioteca import Biblioteca, Livro, Usuario
from notificacoes import Notificador

def menu():
    print("\n----- Sistema de Biblioteca -----")
    print("1. Adicionar Livro")
    print("2. Listar Livros")
    print("3. Adicionar Usuário")
    print("4. Listar Usuários")
    print("5. Emprestar Livro")
    print("6. Devolver Livro")
    print("7. Listar Empréstimos")
    print("8. Sair")
    return input("Escolha uma opção: ")

def main():
    servidor_smtp = "smtp.gmail.com"
    porta = 587
    email_remetente = "gusgurtavo@gmail.com"
    senha = "sua_senha"

    notificador = Notificador(servidor_smtp, porta, email_remetente, senha)
    biblioteca = Biblioteca(notificador)

    while True:
        escolha = menu()

        if escolha == '1':
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = int(input("Ano de Publicação: "))
            livro = Livro(None, titulo, autor, ano)
            biblioteca.adicionar_livro(livro)

        elif escolha == '2':
            biblioteca.listar_livros()

        elif escolha == '3':
            nome = input("Nome: ")
            email = input("Email: ")
            usuario = Usuario(None, nome, email)
            biblioteca.adicionar_usuario(usuario)

        elif escolha == '4':
            biblioteca.listar_usuarios()

        elif escolha == '5':
            id_livro = int(input("ID do Livro: "))
            id_usuario = int(input("ID do Usuário: "))
            biblioteca.emprestar_livro(id_livro, id_usuario)

        elif escolha == '6':
            id_livro = int(input("ID do Livro: "))
            biblioteca.devolver_livro(id_livro)

        elif escolha == '7':
            biblioteca.listar_emprestimos()

        elif escolha == '8':
            print("Saindo...")
            break

if __name__ == "__main__":
    main()
