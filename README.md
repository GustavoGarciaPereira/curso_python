# curso_python
links úteis

[www.plantuml.com (ferramenta de diagrama uml)](https://www.plantuml.com/plantuml/uml/XLExJWCn4EplAwoh4hWKj2UA28cEbjhQ-5Pe9JyYFwu0yK5y1p-6xsmdTYAID55cPsTcTvszys1zKB8J4fnZRpHRmxuw5ZyxHXEN2p0ovst6FFaW6mI2DxO1jE77S90aG42aalQvCf4x6aqpof4TZ94h_CWu9qsUyqqn7BBDaCI72ydjgI-QnhPjSl_kyXJlBe2bPewGe3gcDWhhtwY0P0siKHn7TRJeF4p6ZH5p_ZfraHzMqI59tKlvcdH9dOEcRQShPAW4BqELJO87ZYU5SG6mhaqu6na4rAKgSrvpLhyNzONYwer70MrK5yL9-3Pg2vupjjk3o26ZmQQBfq0bXqLbPYobkD-ckgYKFhVPNWdc79lytRRbQjLOxdjfDrJlfd3NhSvuczhOLVD7nxZHz1VhdthslDkn_g6l7yB8XD7-zqTrwTmtY1P1qYTqrMqMhidSP3Eo3xIe1VtBopwtcQrxGzwZdeAIVm00)





[aula_1_operadores lógicos, variáveis e operadores aritméticos](/materia/aula_1.md)

[aula_2_tipos estruturados](/materia/aula_2.md)

[aula_3_Exceções e Tratamento de Erros](/materia/aula_3.md)

[aula_4_Resumo: Estruturas de Dados Avançadas](/materia/aula_4.md)

[aula_5_Controle de Fluxo em Python](/materia/aula_5.md)

[aula_6_Interface grafica](/materia/aula_6.md)


## Matérial Python

[PensePython2e](https://penseallen.github.io/PensePython2e/)

[python_tutorial](https://docs.python.org/pt-br/3.10/tutorial/)


## Material django
https://docs.djangoproject.com/en/5.1/topics/install/


## Matéria banco de dados
[Programação Dinâmica](https://www.youtube.com/watch?v=BRPUA0EgS4I&list=PL5TJqBvpXQv5n1N15kcK1m9oKJm_cv-m6)

[Base de dados](https://basedosdados.org/dataset/fb38dbe8-03ce-46b4-a6b7-638ade03999c?table=b6df9e1c-cbcb-4dbd-893b-8645a51773e6)

## Matério de Flask
[python-flask-immutablemultidict](https://www.geeksforgeeks.org/python-flask-immutablemultidict/)

[Welcome to Flask’s documentation](https://flask.palletsprojects.com/en/stable/)

[Flask Installation](https://flask.palletsprojects.com/en/stable/installation/)

[Flask quickstart](https://flask.palletsprojects.com/en/stable/quickstart/)

[Jinja Template: Part 1](https://medium.com/@aneesha161994/jinja-template-part-1-94944a2fdaad)

[Jinja Template Part 2 :How to use Jinja template in docxtpl and flask ?](https://medium.com/@aneesha161994/jinja-template-part-2-how-to-use-jinja-template-44e5dcc8516f)

[jinja2](https://jinja.palletsprojects.com/en/stable/templates/)


## comandos git:
| Comando           | Descrição                                                                                     |
|-------------------|-----------------------------------------------------------------------------------------------|
| `git init`        | Inicializa um novo repositório Git no diretório atual.                                        |
| `git add`         | Adiciona arquivos ou alterações ao staging area (área de preparação) para o próximo commit.   |
| `git commit`      | Salva as mudanças no repositório local com uma mensagem descritiva.                           |
| `git push`        | Envia os commits locais para um repositório remoto.                                           |
| `git pull`        | Puxa e integra as atualizações de um repositório remoto para o repositório local.             |
| `git clone`       | Cria uma cópia de um repositório remoto no diretório local.                                   |
| `git branch`      | Cria, lista ou exclui branches no repositório.                                                |
| `git checkout`    | Alterna entre branches ou restaura arquivos em um commit específico.                          |
| `git remote add`  | Adiciona um repositório remoto ao projeto local, associado a um nome específico.              |
| `git remote remove` | Remove um repositório remoto previamente adicionado.                                        |
| `git fetch`       | Baixa as atualizações de um repositório remoto sem integrá-las ao repositório local.          |


## HTML e CSS

[getbootstrap](https://getbootstrap.com/)


## comandos virtualenv

pip install virtualenv

python -m virtualenv venv

source venv/Scripts/activate

pip freeze > requirements.txt

deactivate


## Tabela comandos django
| **Comando**                  | **Usado com**  | **Descrição**                                                                                     |
|------------------------------|----------------|-------------------------------------------------------------------------------------------------|
| `startproject <nome>`        | `django-admin` | Cria um novo projeto Django na pasta especificada.                                              |
| `startapp <nome>`            | `manage.py`    | Cria uma nova aplicação Django dentro do projeto.                                               |
| `runserver [porta]`          | `manage.py`    | Inicia o servidor de desenvolvimento na porta padrão (8000) ou na especificada.                 |
| `migrate`                    | `manage.py`    | Aplica as migrações ao banco de dados.                                                          |
| `makemigrations [app]`       | `manage.py`    | Cria novas migrações baseadas nas alterações feitas nos modelos do app especificado.            |
| `check`                      | `manage.py`    | Verifica o projeto em busca de problemas.                                                       |
| `createsuperuser`            | `manage.py`    | Cria um superusuário para acessar o admin do Django.                                            |
| `shell`                      | `manage.py`    | Abre um shell interativo do Django com acesso ao contexto do projeto.                          |
| `dbshell`                    | `manage.py`    | Abre um shell interativo do banco de dados configurado no projeto.                              |
| `showmigrations`             | `manage.py`    | Lista todas as migrações disponíveis e seu estado (aplicada ou pendente).                       |
| `sqlmigrate <app> <migração>`| `manage.py`    | Mostra o SQL correspondente a uma migração específica.                                          |
| `flush`                      | `manage.py`    | Remove todos os dados do banco de dados, mantendo as tabelas.                                   |
| `inspectdb`                  | `manage.py`    | Gera modelos baseados no esquema do banco de dados atual (para engenharia reversa).             |
| `collectstatic`              | `manage.py`    | Coleta todos os arquivos estáticos das aplicações para o diretório configurado no projeto.       |
| `test [app]`                 | `manage.py`    | Executa os testes para o app especificado ou para todo o projeto.                               |
| `changepassword <username>`  | `manage.py`    | Altera a senha de um usuário específico.                                                        |
| `dumpdata [app]`             | `manage.py`    | Exporta os dados de um app ou do projeto inteiro em formato JSON.                               |
| `loaddata <arquivo>`         | `manage.py`    | Importa dados de um arquivo JSON ou fixture para o banco de dados.                              |
| `clearcache`                 | `manage.py`    | Limpa o cache do projeto (requer configuração).                                                 |
| `compilemessages`            | `manage.py`    | Compila arquivos de tradução (.po) em arquivos binários (.mo).                                  |
| `makemessages -l <lingua>`   | `manage.py`    | Gera arquivos de tradução para a linguagem especificada.                                         |




# Conteúdos para a vida!

- [Naruhodo #251 - O que é a síndrome do impostor?](https://www.youtube.com/watch?v=tV2jAdJNg4Y)
- [Naruhodo #259 - Por que as coisas parecem óbvias depois que passamos por elas? - Parte 1 de 2](https://www.youtube.com/watch?v=fsgAdq_iu-A)
- [Naruhodo #328 - Existem "gatilhos mentais"?](https://www.youtube.com/watch?v=fxBQJlin8Z4)
- [Naruhodo #366 - Por que temos ideias durante o banho?](https://www.youtube.com/watch?v=jYJUwNRZWHE&t=494s)
- [Naruhodo #367 - Estamos ficando mais esquecidos do que já fomos?](https://www.youtube.com/watch?v=ouilklEqKAU)
