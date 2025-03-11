# backend/services/lti_service.py

import jwt
from config import Config
from utils.jwks import verify_token

def validate_lti_launch(id_token):
    """
    Validate the LTI 1.3 id_token using the Turnitin (or other platform) public key (JWKS).
    Check claims: issuer, audience, etc.
    """
    key = verify_token(id_token)  # fetch public key from JWKs

    try:
        decoded = jwt.decode(
            id_token,
            key=key,
            algorithms=["RS256"],
            audience=Config.LTI_CLIENT_ID,
            issuer=Config.LTI_ISSUER
        )
    except jwt.PyJWTError as e:
        raise Exception(f"Invalid or expired JWT: {e}")

    # Basic required claims for an LTI Launch
    required_claims = [
        "iss",
        "aud",
        "nonce",
        "https://purl.imsglobal.org/spec/lti/claim/message_type",
        "https://purl.imsglobal.org/spec/lti/claim/version"
    ]
    for rc in required_claims:
        if rc not in decoded:
            raise Exception(f"Missing required claim: {rc}")

    return decoded
