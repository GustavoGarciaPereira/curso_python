from tkinter import Entry, Tk, Label, Button
from tkinter import messagebox

def  button_click():
    texto_entrada = entrada.get()
    messagebox.showerror(
        title="informacao",
        message=f"Olá {texto_entrada}"
    )




root  = Tk()
root.title("Minha janelinha")
root.geometry("500x500")


label = Label(root,text="Informe seu nome:")
label.pack(pady=5)

entrada = Entry(root)
entrada.pack(pady=12)


button = Button(root, text="botão", command=button_click)
button.pack(pady=12)
root.mainloop()
