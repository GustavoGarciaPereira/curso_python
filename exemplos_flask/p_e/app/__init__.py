from flask import Flask
from .routes import register_routes
from .config import Config

def create_app():
    app = Flask(
        __name__,
        template_folder='../templates',
        static_folder='../static',
        static_url_path='/static'
    )
    
    app.config.from_object(Config)
    
    # Registra as rotas
    register_routes(app)

    return app
