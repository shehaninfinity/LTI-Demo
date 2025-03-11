# backend/utils/jwks.py
import requests
from jwt import PyJWKClient

def get_jwk_client():
    jwks_url = "https://platform.example.com/.well-known/jwks.json"
    return PyJWKClient(jwks_url)

def verify_token(token):
    jwks_client = get_jwk_client()
    signing_key = jwks_client.get_signing_key_from_jwt(token)
    return signing_key.key
