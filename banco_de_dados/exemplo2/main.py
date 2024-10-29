from clientes import atualizar_cliente, criar_cliente, deletar_cliente, ler_clientes
from comandas import atualizar_comanda, criar_comanda, deletar_comanda, ler_comandas
from pedidos import atualizar_pedido, criar_pedido, deletar_pedido, ler_pedidos
import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root_password',
            database='bar'
        )
        if conexao.is_connected():
            print("Conectado ao banco de dados")
            return conexao
    except Error as e:
        print(f"Erro ao conectar: {e}")
        return None




def menu():
    print("\n--- CRUD Bar ---")
    print("1. Criar Cliente")
    print("2. Ler Clientes")
    print("3. Atualizar Cliente")
    print("4. Deletar Cliente")
    print("5. Criar Comanda")
    print("6. Ler Comandas")
    print("7. Atualizar Comanda")
    print("8. Deletar Comanda")
    print("9. Criar Pedido")
    print("10. Ler Pedidos")
    print("11. Atualizar Pedido")
    print("12. Deletar Pedido")
    print("0. Sair")

def executar_opcao(opcao, conexao):
    if opcao == '1':
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        criar_cliente(conexao, nome, telefone, email, cidade, estado)
    elif opcao == '2':
        ler_clientes(conexao)
    elif opcao == '3':
        cliente_id = int(input("ID do Cliente: "))
        print("Deixe em branco para não alterar o campo.")
        nome = input("Novo Nome: ") or None
        telefone = input("Novo Telefone: ") or None
        email = input("Novo Email: ") or None
        cidade = input("Nova Cidade: ") or None
        estado = input("Novo Estado: ") or None
        atualizar_cliente(conexao, cliente_id, nome, telefone, email, cidade, estado)
    elif opcao == '4':
        cliente_id = int(input("ID do Cliente: "))
        deletar_cliente(conexao, cliente_id)
    elif opcao == '5':
        cliente_id = int(input("ID do Cliente: "))
        data_comanda = input("Data da Comanda (YYYY-MM-DD): ")
        status = input("Status: ")
        criar_comanda(conexao, cliente_id, data_comanda, status)
    elif opcao == '6':
        ler_comandas(conexao)
    elif opcao == '7':
        comanda_id = int(input("ID da Comanda: "))
        print("Deixe em branco para não alterar o campo.")
        cliente_id = input("Novo ID do Cliente: ")
        cliente_id = int(cliente_id) if cliente_id else None
        data_comanda = input("Nova Data da Comanda (YYYY-MM-DD): ") or None
        status = input("Novo Status: ") or None
        atualizar_comanda(conexao, comanda_id, cliente_id, data_comanda, status)
    elif opcao == '8':
        comanda_id = int(input("ID da Comanda: "))
        deletar_comanda(conexao, comanda_id)
    elif opcao == '9':
        comanda_id = int(input("ID da Comanda: "))
        item = input("Item: ")
        quantidade = int(input("Quantidade: "))
        preco_unitario = float(input("Preço Unitário: "))
        criar_pedido(conexao, comanda_id, item, quantidade, preco_unitario)
    elif opcao == '10':
        ler_pedidos(conexao)
    elif opcao == '11':
        pedido_id = int(input("ID do Pedido: "))
        print("Deixe em branco para não alterar o campo.")
        comanda_id = input("Novo ID da Comanda: ")
        comanda_id = int(comanda_id) if comanda_id else None
        item = input("Novo Item: ") or None
        quantidade = input("Nova Quantidade: ")
        quantidade = int(quantidade) if quantidade else None
        preco_unitario = input("Novo Preço Unitário: ")
        preco_unitario = float(preco_unitario) if preco_unitario else None
        atualizar_pedido(conexao, pedido_id, comanda_id, item, quantidade, preco_unitario)
    elif opcao == '12':
        pedido_id = int(input("ID do Pedido: "))
        deletar_pedido(conexao, pedido_id)
    elif opcao == '0':
        print("Saindo...")
    else:
        print("Opção inválida!")

def main():
    conexao = conectar()
    if conexao:
        while True:
            menu()
            opcao = input("Escolha uma opção: ")
            if opcao == '0':
                executar_opcao(opcao, conexao)
                break
            executar_opcao(opcao, conexao)
        conexao.close()
        print("Conexão encerrada.")

if __name__ == "__main__":
    main()
