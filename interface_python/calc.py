import tkinter as tk

def add_to_expression(value):
    current = expression_label["text"]
    expression_label.config(text=current + str(value))

def calculate():
    try:
        result = eval(expression_label["text"])
        expression_label.config(text=str(result))
    except Exception:
        expression_label.config(text="Error")

def clear():
    expression_label.config(text="")

root = tk.Tk()
root.title("Calculadora")

# Label para exibir a expressão
expression_label = tk.Label(root, text="", font=("Arial", 20), anchor="e")
expression_label.grid(row=0, column=0, columnspan=4)

# Botões numéricos
for i in range(1, 10):
    button = tk.Button(root, text=str(i), font=("Arial", 15), width=5,
                       command=lambda i=i: add_to_expression(i))
    button.grid(row=(i-1)//3 + 1, column=(i-1)%3)

# Botão zero
tk.Button(root, text="0", font=("Arial", 15), width=5,
          command=lambda: add_to_expression(0)).grid(row=4, column=1)

# Botões de operações
operations = ["+", "-", "*", "/"]
for idx, op in enumerate(operations):
    tk.Button(root, text=op, font=("Arial", 15), width=5,
              command=lambda op=op: add_to_expression(op)).grid(row=idx+1, column=3)

# Botão de igual
tk.Button(root, text="=", font=("Arial", 15), width=5,
          command=calculate).grid(row=4, column=3)

# Botão de limpar
tk.Button(root, text="C", font=("Arial", 15), width=5,
          command=clear).grid(row=4, column=0)

root.mainloop()
