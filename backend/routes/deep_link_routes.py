# backend/routes/deep_link_routes.py

from flask import Blueprint, request, jsonify
from services.lti_service import validate_lti_launch
from services.deep_link_service import build_deep_link_jwt

dl_bp = Blueprint('deep_link', __name__)

@dl_bp.route('/handle', methods=['POST'])
def handle_deep_link():
    """
    Step: Deep Linking.
    - The platform sends an LtiDeepLinkingRequest (id_token) to your /deep_link/handle.
    - You let user pick or create content (like your PDF assignment).
    - Then respond with a 'Deep Linking Response' (JWT) that the platform consumes
      to create a new link in the LMS.
    """
    data = request.form.to_dict()
    id_token = data.get('id_token', None)
    if not id_token:
        return jsonify({"error": "Missing id_token"}), 400

    try:
        decoded = validate_lti_launch(id_token)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    # Here you'd show UI for content selection, or just generate a dummy resource link.
    # We'll assume the user selected "pdf_id=123".
    deep_link_jwt = build_deep_link_jwt(decoded, resource_link_id="pdf_123")
    # This JWT must be posted back to the deep_link_return_url from the LMS.

    return jsonify({"deep_link_jwt": deep_link_jwt})
