import curses
from biblioteca import Biblioteca, Livro, Usuario

def exibir_menu(stdscr):
    # Configurações iniciais do curses
    curses.curs_set(0)  # Ocultar cursor
    curses.start_color()  # Ativar cores
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)  # Cor da opção selecionada

    opcoes = [
        "Adicionar Livro",
        "Remover Livro",
        "Listar Livros",
        "Adicionar Usuário",
        "Listar Usuários",
        "Emprestar Livro",
        "Devolver Livro",
        "Listar Empréstimos",
        "Sair"
    ]
    escolha = 0  # Começar na primeira opção
    biblioteca = Biblioteca()  # Instanciar a biblioteca

    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()  # Pegar tamanho da tela

        # Exibir todas as opções
        for i, opcao in enumerate(opcoes):
            x = w // 2 - len(opcao) // 2  # Centraliza horizontalmente
            y = h // 2 - len(opcoes) // 2 + i  # Distribui verticalmente

            if i == escolha:
                stdscr.attron(curses.color_pair(1))  # Ativar destaque
                stdscr.addstr(y, x, opcao)
                stdscr.attroff(curses.color_pair(1))  # Desativar destaque
            else:
                stdscr.addstr(y, x, opcao)

        stdscr.refresh()
        key = stdscr.getch()

        # Navegação pelas setas do teclado
        if key == curses.KEY_UP and escolha > 0:
            escolha -= 1
        elif key == curses.KEY_DOWN and escolha < len(opcoes) - 1:
            escolha += 1
        elif key in [10, 13]:  # Enter pressionado
            executar_acao(escolha, stdscr, biblioteca)
            if escolha == len(opcoes) - 1:  # Última opção é "Sair"
                break

def executar_acao(escolha, stdscr, biblioteca:Biblioteca):
    stdscr.clear()
    if escolha == 0:
        id_livro = input_texto(stdscr, "ID do Livro: ")
        titulo = input_texto(stdscr, "Título: ")
        autor = input_texto(stdscr, "Autor: ")
        ano = input_texto(stdscr, "Ano de Publicação: ")
        livro = Livro(id_livro, titulo, autor, ano)
        biblioteca.adicionar_livro(livro)

    elif escolha == 1:
        id_livro = input_texto(stdscr, "ID do Livro a remover: ")
        biblioteca.remover_livro(id_livro)

    elif escolha == 2:
        biblioteca.listar_livros(stdscr)
        stdscr.getch()

    elif escolha == 3:
        id_usuario = input_texto(stdscr, "ID do Usuário: ")
        nome = input_texto(stdscr, "Nome: ")
        email = input_texto(stdscr, "Email: ")
        usuario = Usuario(id_usuario, nome, email)
        biblioteca.adicionar_usuario(usuario)

    elif escolha == 4:
        biblioteca.listar_usuarios()
        stdscr.getch()

    elif escolha == 5:
        id_livro = input_texto(stdscr, "ID do Livro para empréstimo: ")
        id_usuario = input_texto(stdscr, "ID do Usuário: ")
        biblioteca.emprestar_livro(id_livro, id_usuario)

    elif escolha == 6:
        id_livro = input_texto(stdscr, "ID do Livro para devolução: ")
        id_usuario = input_texto(stdscr, "ID do Usuário: ")
        biblioteca.devolver_livro(id_livro, id_usuario)

    elif escolha == 7:
        biblioteca.listar_emprestimos()
        stdscr.getch()

    elif escolha == 8:
        stdscr.addstr(0, 0, "Saindo do sistema. Até logo!")
        stdscr.refresh()
        stdscr.getch()

def input_texto(stdscr, prompt):
    stdscr.clear()
    stdscr.addstr(0, 0, prompt)
    stdscr.refresh()
    curses.echo()  # Ativar entrada visível
    entrada = stdscr.getstr().decode("utf-8")
    curses.noecho()  # Desativar entrada visível
    return entrada

def main():
    curses.wrapper(exibir_menu)

if __name__ == "__main__":
    main()
