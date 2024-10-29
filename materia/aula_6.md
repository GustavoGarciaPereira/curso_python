### 1. **Configuração Básica e Janela Principal**

- **`tk.Tk()`**: Cria a janela principal da aplicação.
- **`title("Texto")`**: Define o título da janela principal.
- **`geometry("LARGURAxALTURA")`**: Define o tamanho da janela (ex: `"300x200"` para 300 pixels de largura por 200 de altura).
- **`mainloop()`**: Inicia o loop principal da aplicação, mantendo a janela aberta até que seja fechada.

---

### 2. **Widgets Básicos**

#### Rótulos (Labels)
- **`Label(root, text="Texto")`**: Cria um rótulo de texto.
- **`label.pack(pady=10)`**: Posiciona o rótulo na janela com um espaçamento vertical (`pady`).

#### Botões
- **`Button(root, text="Texto do Botão", command=função)`**: Cria um botão que, ao ser clicado, chama a função definida em `command`.
- **`button.pack(pady=10)`**: Posiciona o botão na janela com um espaçamento vertical (`pady`).

#### Campos de Entrada (Entry)
- **`Entry(root)`**: Cria um campo de entrada onde o usuário pode digitar texto.
- **`entry.get()`**: Recupera o texto digitado no campo de entrada.
- **`entry.pack(pady=5)`**: Posiciona o campo de entrada na janela com um espaçamento vertical.

#### Combobox (Lista de Opções)
- **`ttk.Combobox(root, values=[...])`**: Cria uma combobox, ou lista de opções, para o usuário escolher entre várias opções.
- **`combobox.set("Texto")`**: Define o valor padrão da combobox.
- **`combobox.get()`**: Recupera o valor selecionado.

---

### 3. **Mensagens e Alertas**

- **`messagebox.showinfo("Título", "Mensagem")`**: Exibe uma caixa de mensagem de informação.
- **`messagebox.showwarning("Título", "Mensagem")`**: Exibe uma caixa de mensagem de aviso.
- **`messagebox.showerror("Título", "Mensagem")`**: Exibe uma caixa de mensagem de erro.

---

### 4. **Widgets do `matplotlib` com Tkinter**

- **`Figure(figsize=(L, A), dpi=N)`**: Cria uma figura `matplotlib` onde L é a largura, A é a altura e dpi é a resolução da figura.
- **`add_subplot(111)`**: Adiciona um conjunto de eixos (gráfico) à figura.
- **`ax.plot(x, y)`**: Desenha um gráfico de linha com listas de dados `x` e `y`.
- **`ax.bar(x, y)`**: Desenha um gráfico de barras com listas de dados `x` e `y`.
- **`ax.set_title("Título")`**: Define o título do gráfico.
- **`ax.set_xlabel("Nome do Eixo X")` e `ax.set_ylabel("Nome do Eixo Y")`**: Define os rótulos dos eixos X e Y.
- **`FigureCanvasTkAgg(fig, master=root)`**: Cria um canvas para integrar a figura do `matplotlib` ao `tkinter`.
- **`canvas.draw()`**: Renderiza a figura dentro do canvas.
- **`canvas.get_tk_widget().pack()`**: Posiciona o widget canvas na janela principal.

---

### 5. **Gerenciamento de Layouts e Posicionamento**

- **`pack(pady=N)`**: Posiciona o widget com um espaçamento vertical (`pady`).
- **`pack_forget()`**: Remove o widget da janela, útil para atualizar ou excluir elementos.
