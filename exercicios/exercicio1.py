import os

class FileManager:
    def __init__(self, directory):
        pass


    def list_files(self):
        """Retorna uma lista de todos os arquivos no diretório"""
        pass


    def create_file(self, file_name, content):
        """Cria um arquivo com o nome e conteúdo especificados"""
        pass


    def delete_file(self, file_name):
        """Exclui o arquivo especificado no diretório"""
        pass


    def rename_file(self, old_name, new_name):
        """Renomeia um arquivo de old_name para new_name"""
        pass


    def file_exists(self, file_name):
        """Retorna True se o arquivo existir no diretório, caso contrário False"""
        pass


    def get_file_size(self, file_name):
        """Retorna o tamanho do arquivo em bytes"""
        pass


# Explicação dos métodos:
# __init__: O construtor da classe, que aceita um diretório e, se ele não existir, cria o diretório.
# list_files(): Lista todos os arquivos no diretório especificado.
# create_file(file_name, content): Cria um arquivo com o nome e conteúdo fornecidos.
# delete_file(file_name): Exclui o arquivo com o nome especificado.
# rename_file(old_name, new_name): Renomeia um arquivo de old_name para new_name.
# file_exists(file_name): Verifica se o arquivo existe no diretório.
# get_file_size(file_name): Retorna o tamanho do arquivo em bytes.
