
from flask import Flask
from app.routes import odds_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(odds_bp)
    return app
