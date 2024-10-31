import tkinter as tk

# Configuração principal da janela
root = tk.Tk()
root.title("Exemplo de Menubutton")
root.geometry("400x300")

# Criação do Menubutton
menubutton = tk.Menubutton(root, text="Opções", relief="raised")
menubutton.grid(row=0, column=0, padx=20, pady=20)

# Criação do Menu associado ao Menubutton
menu = tk.Menu(menubutton, tearoff=0)
menubutton.config(menu=menu)

# Adicionando itens ao Menu
menu.add_command(label="Opção 1", command=lambda: print("Opção 1 selecionada"))
menu.add_command(label="Opção 2", command=lambda: print("Opção 2 selecionada"))
menu.add_separator()
menu.add_command(label="Sair", command=root.quit)

# Inicia o loop da aplicação
root.mainloop()
