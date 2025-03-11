# Exemplo 1: Manipulação de datas com datetime
from datetime import datetime, timedelta

# Data atual
hoje = datetime.now()
# Data futura (7 dias depois)
proxima_semana = hoje + timedelta(days=7)
print(f"Hoje: {hoje.strftime('%d/%m/%Y')}")
print(f"Próxima semana: {proxima_semana.strftime('%d/%m/%Y')}")

# Exemplo 2: Trabalhando com JSON
import json

dados = {
    "nome": "Maria",
    "idade": 30,
    "hobbies": ["leitura", "música", "viagem"]
}

# Convertendo para JSON
json_string = json.dumps(dados, indent=4)
print("\nJSON formatado:")
print(json_string)

# Exemplo 3: Manipulação de arquivos e diretórios
import os
from pathlib import Path

# Criar diretório
Path("exemplo_dir").mkdir(exist_ok=True)

# Listar arquivos do diretório atual
print("\nArquivos no diretório atual:")
for arquivo in os.listdir("."):
    print(f"- {arquivo}")

# Exemplo 4: Gerando números aleatórios
import random

# Lista de nomes
nomes = ["Ana", "João", "Pedro", "Maria", "Carlos"]
print("\nSorteio aleatório:")
print(f"Nome sorteado: {random.choice(nomes)}")
print(f"Número aleatório entre 1 e 100: {random.randint(1, 100)}")

# Exemplo 5: Trabalhando com URLs
from urllib.parse import urlparse

url = "https://www.exemplo.com/pagina?param=valor"
parsed_url = urlparse(url)
print("\nAnálise de URL:")
print(f"Protocolo: {parsed_url.scheme}")
print(f"Domínio: {parsed_url.netloc}")
print(f"Caminho: {parsed_url.path}")




---------------------------


# Exemplo 1: Collections - Counter e defaultdict
from collections import Counter, defaultdict

# Counter para contar ocorrências
texto = "python é uma linguagem python muito python legal"
contagem = Counter(texto.split())
print("Counter exemplo:")
print(contagem)  # Conta palavras

# defaultdict para dicionário com valor padrão
dict_padrao = defaultdict(list)
dict_padrao['frutas'].append('maçã')
dict_padrao['frutas'].append('banana')
print("\nDefaultdict exemplo:")
print(dict_padrao)

# Exemplo 2: CSV
import csv

# Criar arquivo CSV
dados = [
    ['Nome', 'Idade', 'Cidade'],
    ['João', '25', 'São Paulo'],
    ['Maria', '30', 'Rio de Janeiro']
]

with open('pessoas.csv', 'w', newline='') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerows(dados)

# Ler arquivo CSV
with open('pessoas.csv', 'r') as arquivo:
    reader = csv.reader(arquivo)
    print("\nLendo CSV:")
    for linha in reader:
        print(linha)

# Exemplo 3: SQLite3
import sqlite3

# Criar banco e tabela
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        idade INTEGER
    )
''')

# Inserir dados
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", ("Ana", 25))
conn.commit()
conn.close()

# Exemplo 4: Logging
import logging

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Iniciando o programa")
logging.warning("Este é um aviso")
logging.error("Este é um erro")

# Exemplo 5: Argparse
import argparse

parser = argparse.ArgumentParser(description='Um exemplo de CLI')
parser.add_argument('--nome', type=str, help='Nome do usuário')
parser.add_argument('--idade', type=int, help='Idade do usuário')

# Para testar, execute o script com argumentos:
# python script.py --nome João --idade 25
args = parser.parse_args()

# Exemplo 6: Expressões Regulares (RE)
import re

texto = "Meu email é exemplo@email.com e telefone é 123-456-789"

# Encontrar email
email = re.search(r'\S+@\S+\.\S+', texto)
print("\nEmail encontrado:", email.group())

# Encontrar telefone
telefone = re.search(r'\d{3}-\d{3}-\d{3}', texto)
print("Telefone encontrado:", telefone.group())

# Exemplo 7: Unittest
import unittest

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('python'.upper(), 'PYTHON')

    def test_isupper(self):
        self.assertTrue('PYTHON'.isupper())
        self.assertFalse('Python'.isupper())

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

# Created/Modified files during execution:
print("Arquivos criados/modificados:")
print("- pessoas.csv")
print("- exemplo.db")
