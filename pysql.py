import mysql.connector
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='senacrs',
    database='bar',
    use_pure=True
)


cursor = conexao.cursor()

cursor.execute("select * from  clientes;")
dados = cursor.fetchall()
print(type(dados[0]))


for i in dados:
    print(f"id = {i[0]} nome:{i[1]}")
