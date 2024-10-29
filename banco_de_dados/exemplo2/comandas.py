from mysql.connector import Error


def criar_comanda(conexao, cliente_id, data_comanda, status):
    try:
        cursor = conexao.cursor()
        sql = "INSERT INTO comandas (cliente_id, data_comanda, status) VALUES (%s, %s, %s)"
        valores = (cliente_id, data_comanda, status)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Comanda criada com sucesso!")
    except Error as e:
        print(f"Erro ao criar comanda: {e}")

def ler_comandas(conexao):
    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM comandas")
        resultados = cursor.fetchall()
        for comanda in resultados:
            print(comanda)
    except Error as e:
        print(f"Erro ao ler comandas: {e}")

def atualizar_comanda(conexao, comanda_id, cliente_id=None, data_comanda=None, status=None):
    try:
        cursor = conexao.cursor()
        campos = []
        valores = []
        if cliente_id:
            campos.append("cliente_id = %s")
            valores.append(cliente_id)
        if data_comanda:
            campos.append("data_comanda = %s")
            valores.append(data_comanda)
        if status:
            campos.append("status = %s")
            valores.append(status)
        valores.append(comanda_id)
        sql = f"UPDATE comandas SET {', '.join(campos)} WHERE comanda_id = %s"
        cursor.execute(sql, tuple(valores))
        conexao.commit()
        print("Comanda atualizada com sucesso!")
    except Error as e:
        print(f"Erro ao atualizar comanda: {e}")

def deletar_comanda(conexao, comanda_id):
    try:
        cursor = conexao.cursor()
        sql = "DELETE FROM comandas WHERE comanda_id = %s"
        cursor.execute(sql, (comanda_id,))
        conexao.commit()
        print("Comanda deletada com sucesso!")
    except Error as e:
        print(f"Erro ao deletar comanda: {e}")

