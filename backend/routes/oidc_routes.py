# backend/routes/oidc_routes.py
from flask import Blueprint, request, redirect, session
import uuid
from config import Config

oidc_bp = Blueprint('oidc', __name__)

@oidc_bp.route('/login_initiation', methods=['GET'])
def oidc_login_initiation():
    client_id = request.args.get('client_id')
    login_hint = request.args.get('login_hint')
    lti_message_hint = request.args.get('lti_message_hint')
    target_link_uri = request.args.get('target_link_uri')

    # Generate random state and nonce for security
    state = str(uuid.uuid4())
    nonce = str(uuid.uuid4())

    # Store them temporarily (in session or a database)
    session['state'] = state
    session['nonce'] = nonce

    # Construct LMS authorization URL (example URL, update as needed)
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
