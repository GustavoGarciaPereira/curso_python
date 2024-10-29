import mysql.connector
from mysql.connector.errors import Error


# Configuração da conexão


config = {
    'host': 'localhost',
    'user': 'gustavo',
    'password': 'senha_gustavo',
    'database': 'teste_db'  # Atualizado para teste_db
}

def inicializar_tabelas():
    try:
        # Conectando ao MySQL
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        # Criando a tabela 'livros'
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS livros (
                id INT AUTO_INCREMENT PRIMARY KEY,
                titulo VARCHAR(255),
                autor VARCHAR(255),
                ano_publicacao INT,
                disponivel BOOLEAN DEFAULT TRUE
            );
        """)

        # Criando a tabela 'usuarios'
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255),
                email VARCHAR(255)
            );
        """)

        # Criando a tabela 'emprestimos'
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS emprestimos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                id_livro INT,
                id_usuario INT,
                data_emprestimo DATE,
                data_devolucao DATE,
                FOREIGN KEY (id_livro) REFERENCES livros(id),
                FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
            );
        """)

        print("Tabelas inicializadas com sucesso!")

    except mysql.connector.Error as err:
        print(f"Erro: {err}")
    finally:
        cursor.close()
        conn.close()

# Executando a função de inicialização
if __name__ == "__main__":
    inicializar_tabelas()