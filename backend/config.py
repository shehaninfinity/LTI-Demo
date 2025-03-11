# backend/config.py
import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "your_secret_key_here"
    LTI_ISSUER = "https://your.lti.issuer"
    LTI_CLIENT_ID = "your_client_id"
    LTI_DEPLOYMENT_ID = "your_deployment_id"
    LTI_KEY_SET_URL = "https://your.lti.keyset.url"  # For production use
    # Add any additional configuration parameters as needed.
    