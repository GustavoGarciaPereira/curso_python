import tkinter as tk

# Função de callback para quando uma opção é selecionada
def option_selected(value):
    print(f"Opção selecionada: {value.get()}")

# Configuração principal da janela
root = tk.Tk()
root.title("Exemplo de OptionMenu")
root.geometry("300x200")

# Variável que guarda o valor selecionado
selected_option = tk.StringVar(root)
selected_option.set("Opção 1")  # Valor inicial

# Criação do OptionMenu
options = ["Opção 1", "Opção 2", "Opção 3", "Opção 4"]
option_menu = tk.OptionMenu(root, selected_option, *options, command=lambda _: option_selected(selected_option))
option_menu.pack(pady=50)

# Inicia o loop da aplicação
root.mainloop()
