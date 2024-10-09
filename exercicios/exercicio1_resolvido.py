import os

class FileManager:
    def __init__(self, directory):
        self.directory = directory
        # Verifica se o diretório existe, caso contrário cria
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

    def list_files(self):
        """Retorna uma lista de todos os arquivos no diretório"""
        try:
            return os.listdir(self.directory)
        except FileNotFoundError:
            return []

    def create_file(self, file_name, content):
        """Cria um arquivo com o nome e conteúdo especificados"""
        file_path = os.path.join(self.directory, file_name)
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"Arquivo '{file_name}' criado com sucesso!")

    def delete_file(self, file_name):
        """Exclui o arquivo especificado no diretório"""
        file_path = os.path.join(self.directory, file_name)
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Arquivo '{file_name}' excluído com sucesso!")
        else:
            print(f"Arquivo '{file_name}' não encontrado.")

    def rename_file(self, old_name, new_name):
        """Renomeia um arquivo de old_name para new_name"""
        old_path = os.path.join(self.directory, old_name)
        new_path = os.path.join(self.directory, new_name)
        if os.path.exists(old_path):
            os.rename(old_path, new_path)
            print(f"Arquivo '{old_name}' renomeado para '{new_name}' com sucesso!")
        else:
            print(f"Arquivo '{old_name}' não encontrado.")

    def file_exists(self, file_name):
        """Retorna True se o arquivo existir no diretório, caso contrário False"""
        file_path = os.path.join(self.directory, file_name)
        return os.path.exists(file_path)

    def get_file_size(self, file_name):
        """Retorna o tamanho do arquivo em bytes"""
        file_path = os.path.join(self.directory, file_name)
        if os.path.exists(file_path):
            return os.path.getsize(file_path)
        else:
            print(f"Arquivo '{file_name}' não encontrado.")
            return None
