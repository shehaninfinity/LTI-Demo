# backend/routes/lti_routes.py
from flask import Blueprint, request, jsonify
from services.lti_service import validate_lti_launch

lti_bp = Blueprint('lti', __name__)

@lti_bp.route('/launch', methods=['POST'])
def lti_launch():
    # Expecting an LTI launch POST request (form-encoded)
    data = request.form.to_dict()
    id_token = data.get('id_token')
    if not id_token:
        return jsonify({'error': 'Missing id_token'}), 400

    # Validate the LTI launch token
    try:
        launch_data = validate_lti_launch(id_token)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

    # For demo, return the launch data
    return jsonify({'message': 'LTI launch successful', 'launch_data': launch_data}), 200

@lti_bp.route('/deep_link', methods=['POST'])
def lti_deep_link():
    # Handle deep linking requests
    data = request.form.to_dict()
    id_token = data.get('id_token')
    if not id_token:
        return jsonify({'error': 'Missing id_token'}), 400

    try:
        deep_link_data = validate_lti_launch(id_token)  # Reuse validation function
    except Exception as e:
        return jsonify({'error': str(e)}), 400

    # Process deep linking logic. Here we return a dummy resource link.
    resource_link = "https://your.domain.com/resource/123"
    response = {
        "deep_link_return_url": data.get("deep_link_return_url", ""),
        "resource_link": resource_link
    }
    return jsonify(response), 200
