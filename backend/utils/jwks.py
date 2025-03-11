# backend/utils/jwks.py

from jwt import PyJWKClient
from config import Config

def verify_token(token):
    """
    1. Fetch JWK Set from the LTI Key Set URL.
    2. Find the correct public key for the token's 'kid'.
    3. Return that key for verifying signature.
    """
    jwks_client = PyJWKClient(Config.LTI_KEY_SET_URL)
    signing_key = jwks_client.get_signing_key_from_jwt(token)
    return signing_key.key
