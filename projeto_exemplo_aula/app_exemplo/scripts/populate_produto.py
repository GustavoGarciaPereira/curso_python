# import os
# import django

# Configurar o ambiente do Django
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nome_do_seu_projeto.settings')
# django.setup()

from produto.models import Produto  # Substitua 'app' pelo nome do seu aplicativo
def run():
    # Dados fictícios para popular a tabela Produto
    produtos = [
        {
            "nome": "Smartphone Galaxy S23",
            "preco": 5999.99,
            "estoque": 15,
            "descricao": "Um smartphone de última geração com excelente desempenho."
        },
        {
            "nome": "Notebook Dell Inspiron",
            "preco": 4500.00,
            "estoque": 10,
            "descricao": "Notebook potente, ideal para trabalho e estudo."
        },
        {
            "nome": "Smart TV 4K Samsung",
            "preco": 3200.00,
            "estoque": 5,
            "descricao": "Televisão 4K com qualidade de imagem superior."
        },
        {
            "nome": "Fone de Ouvido Bluetooth JBL",
            "preco": 299.99,
            "estoque": 30,
            "descricao": "Fone de ouvido sem fio com alta qualidade de som."
        },
        {
            "nome": "Teclado Mecânico Logitech",
            "preco": 799.99,
            "estoque": 25,
            "descricao": "Teclado mecânico para gamers e profissionais."
        },
        {
            "nome": "Câmera DSLR Canon EOS",
            "preco": 2500.00,
            "estoque": 8,
            "descricao": "Câmera de alta performance para fotografia profissional."
        },
        {
            "nome": "Monitor LG Ultrawide",
            "preco": 1299.99,
            "estoque": 12,
            "descricao": "Monitor ultrawide para maior produtividade."
        },
        {
            "nome": "Mouse Gamer Razer",
            "preco": 499.99,
            "estoque": 20,
            "descricao": "Mouse com sensor de alta precisão e design ergonômico."
        },
        {
            "nome": "Console PlayStation 5",
            "preco": 4999.99,
            "estoque": 3,
            "descricao": "Console de última geração com gráficos incríveis."
        },
        {
            "nome": "Drone DJI Mini 3 Pro",
            "preco": 4200.00,
            "estoque": 7,
            "descricao": "Drone compacto com câmera 4K e recursos avançados."
        }
    ]

    # Inserir os dados no banco de dados
    for produto in produtos:
        Produto.objects.create(**produto)

    print("Banco de dados populado com sucesso!")
