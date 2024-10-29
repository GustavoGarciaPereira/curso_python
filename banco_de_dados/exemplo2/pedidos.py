from mysql.connector import Error
def criar_pedido(conexao, comanda_id, item, quantidade, preco_unitario):
    try:
        cursor = conexao.cursor()
        sql = "INSERT INTO pedidos (comanda_id, item, quantidade, preco_unitario) VALUES (%s, %s, %s, %s)"
        valores = (comanda_id, item, quantidade, preco_unitario)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Pedido criado com sucesso!")
    except Error as e:
        print(f"Erro ao criar pedido: {e}")

def ler_pedidos(conexao):
    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM pedidos")
        resultados = cursor.fetchall()
        for pedido in resultados:
            print(pedido)
    except Error as e:
        print(f"Erro ao ler pedidos: {e}")

def atualizar_pedido(conexao, pedido_id, comanda_id=None, item=None, quantidade=None, preco_unitario=None):
    try:
        cursor = conexao.cursor()
        campos = []
        valores = []
        if comanda_id:
            campos.append("comanda_id = %s")
            valores.append(comanda_id)
        if item:
            campos.append("item = %s")
            valores.append(item)
        if quantidade:
            campos.append("quantidade = %s")
            valores.append(quantidade)
        if preco_unitario:
            campos.append("preco_unitario = %s")
            valores.append(preco_unitario)
        valores.append(pedido_id)
        sql = f"UPDATE pedidos SET {', '.join(campos)} WHERE pedido_id = %s"
        cursor.execute(sql, tuple(valores))
        conexao.commit()
        print("Pedido atualizado com sucesso!")
    except Error as e:
        print(f"Erro ao atualizar pedido: {e}")

def deletar_pedido(conexao, pedido_id):
    try:
        cursor = conexao.cursor()
        sql = "DELETE FROM pedidos WHERE pedido_id = %s"
        cursor.execute(sql, (pedido_id,))
        conexao.commit()
        print("Pedido deletado com sucesso!")
    except Error as e:
        print(f"Erro ao deletar pedido: {e}")

