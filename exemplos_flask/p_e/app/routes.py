from .controllers import main, home, cadastro, listagem

def register_routes(app):
    app.add_url_rule('/<int:num1>/<int:num2>/<string:sinal>', view_func=main, methods=['GET'])
    app.add_url_rule('/', view_func=home)
    app.add_url_rule('/cadastro', view_func=cadastro)
    app.add_url_rule('/listagem', view_func=listagem)



# Atividade
# Local
# Carga horária
# Tipo de participante
# Atividade
# Data Inicial
# Data Final