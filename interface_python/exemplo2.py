import tkinter as tk
from tkinter import messagebox

# Função para exibir uma mensagem personalizada
def show_greeting():
    name = entry_name.get()  # Obtém o texto inserido no campo de entrada
    if name:
        messagebox.showinfo("Saudação", f"Olá, {name}! Bem-vindo ao Tkinter!")
    else:
        messagebox.showwarning("Atenção", "Por favor, insira um nome.")

# Criação da janela principal
root = tk.Tk()
root.title("Exemplo Tkinter - Saudação")
root.geometry("300x200")

# Rótulo para instruir o usuário
label = tk.Label(root, text="Digite seu nome:")
label.pack(pady=10)

# Campo de entrada para o nome do usuário
entry_name = tk.Entry(root)
entry_name.pack(pady=5)

# Botão para mostrar a saudação
button = tk.Button(root, text="Saudar", command=show_greeting)
button.pack(pady=20)

# Iniciar o loop principal da aplicação
root.mainloop()
