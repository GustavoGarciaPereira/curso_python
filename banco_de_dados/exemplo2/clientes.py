from mysql.connector import Error

def criar_cliente(conexao, nome, telefone, email, cidade, estado):
    try:
        cursor = conexao.cursor()
        sql = "INSERT INTO clientes (nome, telefone, email, cidade, estado) VALUES (%s, %s, %s, %s, %s)"
        valores = (nome, telefone, email, cidade, estado)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Cliente criado com sucesso!")
    except Error as e:
        print(f"Erro ao criar cliente: {e}")

def ler_clientes(conexao):
    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM clientes")
        resultados = cursor.fetchall()
        for cliente in resultados:
            print(cliente)
    except Error as e:
        print(f"Erro ao ler clientes: {e}")

def atualizar_cliente(conexao, cliente_id, nome=None, telefone=None, email=None, cidade=None, estado=None):
    try:
        cursor = conexao.cursor()
        campos = []
        valores = []
        if nome:
            campos.append("nome = %s")
            valores.append(nome)
        if telefone:
            campos.append("telefone = %s")
            valores.append(telefone)
        if email:
            campos.append("email = %s")
            valores.append(email)
        if cidade:
            campos.append("cidade = %s")
            valores.append(cidade)
        if estado:
            campos.append("estado = %s")
            valores.append(estado)
        valores.append(cliente_id)
        sql = f"UPDATE clientes SET {', '.join(campos)} WHERE cliente_id = %s"
        cursor.execute(sql, tuple(valores))
        conexao.commit()
        print("Cliente atualizado com sucesso!")
    except Error as e:
        print(f"Erro ao atualizar cliente: {e}")

def deletar_cliente(conexao, cliente_id):
    try:
        cursor = conexao.cursor()
        sql = "DELETE FROM clientes WHERE cliente_id = %s"
        cursor.execute(sql, (cliente_id,))
        conexao.commit()
        print("Cliente deletado com sucesso!")
    except Error as e:
        print(f"Erro ao deletar cliente: {e}")

