from tkinter import WORD, Entry, Text, Tk, Label, Button, END, Toplevel
from tkinter import messagebox
from tkinter import filedialog
import markdown
from tkhtmlview import HTMLLabel




class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Minha janelinha")
        self.geometry("500x500")
        self.interface()

    def  button_click(self, t):
        print(t)
        texto_entrada = self.entrada.get()
        response = messagebox.askquestion("Confirmação", "Você deseja continuar?")
        if response == "yes":
            messagebox.showerror(
                title="informacao",
                message=f"simm Olá {texto_entrada}"
            )
        else:
            messagebox.showerror(
                title="informacao",
                message=f"não Olá {texto_entrada}"
            )

    def on_button_click(self):
        self.button_click("gugu")

    def open_file_dialog(self):
        file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            self.selected_file_label.config(text=f"Selected File: {file_path}")
            self.process_file(file_path)

    def read_markdown(self):
        file_path = filedialog.askopenfilename(title="Select a Markdown File", filetypes=[("Markdown files", "*.md"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                markdown_content = file.read()
                self.render_markdown(markdown_content)

    def render_markdown(self, markdown_content):
        # Convert markdown content to HTML
        html_content = markdown.markdown(markdown_content)

        # Create a new window for displaying markdown
        markdown_window = Toplevel(self)
        markdown_window.title("Markdown Viewer")
        markdown_window.geometry("500x500")
        
        # Add a Text widget to display the HTML content
        text_widget = Text(markdown_window, wrap=WORD, height=25, width=60)
        text_widget.pack(padx=20, pady=20)

        # Insert the converted HTML content
        text_widget.insert(END, html_content)
        text_widget.config(state='disabled')  # Make it read-only

        # Cria o botão que renderiza o Markdown em HTML
        render_button = Button(markdown_window, text="Mostrar Markdown Renderizado", command=lambda: self.show_rendered_markdown(markdown_window, html_content))
        render_button.pack(pady=10)
        
    def show_rendered_markdown(self, window, html_content):
        # Remove qualquer widget anterior da janela e exibe o HTML renderizado
        for widget in window.winfo_children():
            widget.pack_forget()

        # Adiciona um HTMLLabel para exibir o conteúdo renderizado
        html_label = HTMLLabel(window, html=html_content)
        html_label.pack(fill="both", expand=True, padx=10, pady=10)

    def process_file(self,file_path):
        # Implement your file processing logic here
        # For demonstration, let's just display the contents of the selected file
        try:
            with open(file_path, 'r') as file:
                file_contents = file.read()
                self.file_text.delete('1.0', END)
                self.file_text.insert(END, file_contents)
        except Exception as e:
            self.selected_file_label.config(text=f"Error: {str(e)}")



    def interface(self):
        label = Label(self,text="Informe seu nome:")
        label.pack(pady=5)

        self.entrada = Entry(self)
        self.entrada.pack(pady=12)


        button = Button(self, text="botão", command=lambda:self.button_click("guggg"))
        button.pack(pady=12)
        
        # open_button = Button(self, text="Open File", command=self.open_file_dialog)
        # open_button.pack(padx=20, pady=20)
        
        
        # self.selected_file_label = Label(self, text="Selected File:")
        # self.selected_file_label.pack()

        # self.file_text = Text(self, wrap=WORD, height=100, width=400)
        # self.file_text.pack(padx=20, pady=20)

        markdown_button = Button(self, text="Ler Markdown", command=self.read_markdown)
        markdown_button.pack(pady=10)

app = App()
app.mainloop()