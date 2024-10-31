import tkinter as tk
from tkinter import messagebox

# Função para ações de menu
def new_file():
    messagebox.showinfo("Novo Arquivo", "Criando um novo arquivo...")

def open_file():
    messagebox.showinfo("Abrir Arquivo", "Abrindo o arquivo...")

def save_file():
    messagebox.showinfo("Salvar Arquivo", "Salvando o arquivo...")

def undo_action():
    messagebox.showinfo("Desfazer", "Ação de desfazer...")

def redo_action():
    messagebox.showinfo("Refazer", "Ação de refazer...")

# Configuração principal da janela
root = tk.Tk()
root.title("Exemplo de Menu com Tkinter")
root.geometry("400x300")

# Criação da barra de menu
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Menu "Arquivo"
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Novo", command=new_file)
file_menu.add_command(label="Abrir", command=open_file)
file_menu.add_command(label="Salvar", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Sair", command=root.quit)

menu_bar.add_cascade(label="Arquivo", menu=file_menu)

# Menu "Editar"
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Desfazer", command=undo_action)
edit_menu.add_command(label="Refazer", command=redo_action)

menu_bar.add_cascade(label="Editar", menu=edit_menu)

# Menu "Ajuda"
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Sobre", command=lambda: messagebox.showinfo("Sobre", "Exemplo de menu com Tkinter"))

menu_bar.add_cascade(label="Ajuda", menu=help_menu)

# Inicia o loop da aplicação
root.mainloop()
