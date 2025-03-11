# backend/services/lti_service.py
import jwt
from config import Config

def validate_lti_launch(id_token):
    """
    Validates the LTI 1.3 id_token using PyJWT.
    In production, you would fetch the public keys from the LTI keyset URL and verify the token accordingly.
    """
    try:
        # For demo, we use the secret key. In production, validate using the proper RSA public keys.
        decoded = jwt.decode(id_token, Config.SECRET_KEY, algorithms=["HS256"], audience=Config.LTI_CLIENT_ID)
    except jwt.ExpiredSignatureError:
        raise Exception("Token has expired")
    except jwt.InvalidAudienceError:
        raise Exception("Invalid audience")
    except Exception as e:
        raise Exception(f"Token validation error: {str(e)}")
    
    # Check for required LTI claims
    required_claims = [
        "iss", 
        "sub", 
        "https://purl.imsglobal.org/spec/lti/claim/message_type"
    ]
    for claim in required_claims:
        if claim not in decoded:
            raise Exception(f"Missing required claim: {claim}")

    return decoded
