from biblioteca import Biblioteca, Livro, Usuario


def menu():
    print("\n----- Sistema de Biblioteca -----")
    print("1. Adicionar Livro")
    print("2. Remover Livro")
    print("3. Listar Livros")
    print("4. Adicionar Usuário")
    print("5. Listar Usuários")
    print("6. Emprestar Livro")
    print("7. Devolver Livro")
    print("8. Listar Empréstimos")
    print("9. Sair")
    escolha = input("Escolha uma opção: ")

    return escolha


def main():
    biblioteca = Biblioteca()

    while True:
        escolha = menu()

        if escolha == '1':
            id_livro = input("ID do Livro: ")
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = input("Ano de Publicação: ")
            livro = Livro(id_livro, titulo, autor, ano)
            biblioteca.adicionar_livro(livro)

        elif escolha == '2':
            id_livro = input("ID do Livro a remover: ")
            biblioteca.remover_livro(id_livro)

        elif escolha == '3':
            biblioteca.listar_livros()

        elif escolha == '4':
            id_usuario = input("ID do Usuário: ")
            nome = input("Nome: ")
            email = input("Email: ")
            usuario = Usuario(id_usuario, nome, email)
            biblioteca.adicionar_usuario(usuario)

        elif escolha == '5':
            biblioteca.listar_usuarios()

        elif escolha == '6':
            id_livro = input("ID do Livro para empréstimo: ")
            id_usuario = input("ID do Usuário: ")
            biblioteca.emprestar_livro(id_livro, id_usuario)

        elif escolha == '7':
            id_livro = input("ID do Livro para devolução: ")
            id_usuario = input("ID do Usuário: ")
            biblioteca.devolver_livro(id_livro, id_usuario)

        elif escolha == '8':
            biblioteca.listar_emprestimos()

        elif escolha == '9':
            print("Saindo do sistema. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
