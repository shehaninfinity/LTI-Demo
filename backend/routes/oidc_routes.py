# backend/routes/oidc_routes.py

from flask import Blueprint, request, redirect, session
import uuid
from config import Config

oidc_bp = Blueprint('oidc', __name__)

@oidc_bp.route('/login_initiation', methods=['GET'])
def oidc_login_initiation():
    """
    Step 1 of LTI 1.3 flow:
    The Platform (or your custom LMS) will call this endpoint with:
      - client_id
      - login_hint
      - lti_message_hint
      - target_link_uri
    We'll generate state & nonce, store them, and redirect to the OIDC Auth URL.
    """
    client_id = request.args.get('client_id')
    login_hint = request.args.get('login_hint')
    lti_message_hint = request.args.get('lti_message_hint')
    target_link_uri = request.args.get('target_link_uri')

    # Generate random state & nonce
    state = str(uuid.uuid4())
    nonce = str(uuid.uuid4())

    # Store them in session (or database) for later validation
    session['state'] = state
    session['nonce'] = nonce

    # Construct the redirect URL to the LTI/Platform's OIDC auth endpoint
    authorization_url = (
        f"{Config.LTI_AUTH_URL}?"
        f"scope=openid&"
        f"response_type=id_token&"
        f"client_id={client_id}&"
        f"redirect_uri={target_link_uri}&"
        f"login_hint={login_hint}&"
        f"lti_message_hint={lti_message_hint}&"
        f"state={state}&"
        f"nonce={nonce}&"
        f"prompt=none"
    )

    return redirect(authorization_url)
