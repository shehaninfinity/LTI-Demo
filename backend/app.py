# backend/app.py
from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register blueprints
    from routes.lti_routes import lti_bp
    from routes.pdf_routes import pdf_bp

    app.register_blueprint(lti_bp, url_prefix='/lti')
    app.register_blueprint(pdf_bp, url_prefix='/pdfs')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
