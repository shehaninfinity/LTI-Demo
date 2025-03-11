# backend/routes/lti_routes.py

from flask import Blueprint, request, jsonify
from services.lti_service import validate_lti_launch

lti_bp = Blueprint('lti', __name__)

@lti_bp.route('/launch', methods=['POST'])
def lti_launch():
    """
    Step 2 of LTI 1.3 core:
    The platform sends an id_token (JWT) via form POST after successful OIDC login.
    We'll decode & validate the JWT, then respond with success or error.
    """
    data = request.form.to_dict()
    id_token = data.get('id_token', None)
    if not id_token:
        return jsonify({"error": "Missing id_token"}), 400

    try:
        launch_data = validate_lti_launch(id_token)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    return jsonify({"message": "LTI launch successful", "launch_data": launch_data}), 200
