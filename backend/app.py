# backend/app.py

from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.secret_key = Config.SECRET_KEY  # For session usage (state, nonce, etc.)

    # Import and register blueprints
    from routes.oidc_routes import oidc_bp
    from routes.lti_routes import lti_bp
    from routes.deep_link_routes import dl_bp
    from routes.ags_routes import ags_bp
    from routes.nrps_routes import nrps_bp
    from routes.pdf_routes import pdf_bp

    app.register_blueprint(oidc_bp, url_prefix="/oidc")
    app.register_blueprint(lti_bp, url_prefix="/lti")
    app.register_blueprint(dl_bp, url_prefix="/deep_link")
    app.register_blueprint(ags_bp, url_prefix="/ags")
    app.register_blueprint(nrps_bp, url_prefix="/nrps")
    app.register_blueprint(pdf_bp, url_prefix="/pdfs")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
