from tkinter import *
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Classe principal da aplicação
class PlotApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplicação com Tkinter e Matplotlib")
        self.geometry("700x500")

        # Configuração do layout e widgets
        self.create_widgets()

    def create_widgets(self):
        # Rótulo e combobox para seleção do tipo de gráfico
        label  = Label(self, text="Selecione o tipo de gráfico:")
        label.pack(pady=10)

        self.plot_type = ttk.Combobox(self, values=["Linha", "Barras"])
        self.plot_type.set("Linha")  # Define o valor inicial
        self.plot_type.pack(pady=5)

        # Botão para gerar o gráfico
        plot_button  = Button(self, text="Gerar Gráfico", command=self.plot_graph)
        plot_button.pack(pady=20)

        # Área para o gráfico
        self.canvas = None  # Inicia o canvas como None para ser usado depois

    def plot_graph(self):
        # Remove o canvas antigo, se existir
        if self.canvas:
            self.canvas.get_tk_widget().pack_forget()
        
        # Cria uma nova figura de matplotlib
        fig = Figure(figsize=(6, 4), dpi=100)
        ax = fig.add_subplot(111)

        # Dados para o gráfico
        x = [1, 2, 3, 4, 5]
        y = [10, 20, 15, 25, 18]

        # Verifica o tipo de gráfico selecionado e gera o gráfico correspondente
        plot_type = self.plot_type.get()
        if plot_type == "Linha":
            ax.plot(x, y, marker="o")
            ax.set_title("Gráfico de Linha")
        elif plot_type == "Barras":
            ax.bar(x, y)
            ax.set_title("Gráfico de Barras")

        ax.set_xlabel("Eixo X")
        ax.set_ylabel("Eixo Y")

        # Renderiza o gráfico no widget Tkinter
        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(pady=10)

# Instancia e executa a aplicação
if __name__ == "__main__":
    app = PlotApp()
    app.mainloop()
