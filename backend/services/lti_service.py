# backend/services/lti_service.py
import jwt
from utils.jwks import verify_token
from config import Config

def validate_lti_launch(id_token):
    try:
        key = verify_token(id_token)
        decoded = jwt.decode(
            id_token,
            key=key,
            algorithms=["RS256"],
            audience=Config.LTI_CLIENT_ID,
            options={"verify_exp": True}
        )
    except jwt.PyJWTError as e:
        raise Exception(f"Invalid JWT: {str(e)}")

    return decoded
