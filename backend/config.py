# backend/config.py

class Config:
    """
    All necessary configuration for the LTI 1.3 flow:
    - SECRET_KEY used for session management (demo).
    - LTI_* variables store the integration details with your future Turnitin or other LTI Platform.
    - For Turnitin, you'll get actual values (Issuer, JWKS URL, etc.).
    """

    # Replace "some-secret-key" with a secure random key or environment variable
    SECRET_KEY = "some-secret-key"

    # LTI / OIDC configuration
    LTI_CLIENT_ID = "your_client_id"
    LTI_ISSUER = "https://turnitin.example.com"  # or your custom domain
    LTI_KEY_SET_URL = "https://turnitin.example.com/.well-known/jwks.json"
    LTI_AUTH_URL = "https://turnitin.example.com/auth"  # OIDC Auth Endpoint
    DEPLOYMENT_ID = "your_deployment_id"

    # Example for AGS & NRPS
    # Typically, these come from an LMS or Turnitin's documentation (endpoints).
    # You may not need them if Turnitin does not provide direct AGS/NRPS endpoints,
    # but this shows how you would do it for a typical LTI Advantage integration.
    AGS_LINEITEMS_URL = "https://turnitin.example.com/lineitems"
    NRPS_MEMBERSHIPS_URL = "https://turnitin.example.com/memberships"

    # For Access Token URL and optional Platform Authorization Provider:
    ACCESS_TOKEN_URL = "https://turnitin.example.com/token"
    PLATFORM_AUTHORIZATION_PROVIDER = "https://turnitin.example.com/authorization"
