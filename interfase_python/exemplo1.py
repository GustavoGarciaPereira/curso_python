from tkinter import Tk, Button
from tkinter import messagebox

# Função para exibir uma mensagem
def show_message():
    messagebox.showinfo("Mensagem", "Olá, bem-vindo ao Tkinter!")
    messagebox.showerror("dddd", "erro")

# Criação da janela principal
root = Tk()
root.title("Exemplo Tkinter")
root.geometry("500x500")

# # Criação de um botão
button = Button(root, text="Clique aqui", command=show_message)
button.pack(pady=120)


# # Iniciar o loop principal da aplicação
root.mainloop()
