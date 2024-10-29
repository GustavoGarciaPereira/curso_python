import tkinter as tk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Função para exibir o gráfico
def show_plot():
    # Cria uma nova figura de matplotlib
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)

    # Dados para o gráfico
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 2, 5, 3]

    # Cria um gráfico de linha
    ax.plot(x, y, marker="o")
    ax.set_title("Exemplo de Gráfico de Linha")
    ax.set_xlabel("Eixo X")
    ax.set_ylabel("Eixo Y")

    # Renderiza o gráfico no widget Tkinter
    canvas = FigureCanvasTkAgg(fig, master=root)  
    canvas.draw()
    canvas.get_tk_widget().pack(pady=20)

# Criação da janela principal
root = tk.Tk()
root.title("Exemplo Tkinter com Matplotlib")
root.geometry("600x400")

# Rótulo de instrução
label = tk.Label(root, text="Clique no botão para exibir o gráfico:")
label.pack(pady=10)

# Botão para mostrar o gráfico
button = tk.Button(root, text="Mostrar Gráfico", command=show_plot)
button.pack(pady=10)

# Inicia o loop principal da aplicação
root.mainloop()
