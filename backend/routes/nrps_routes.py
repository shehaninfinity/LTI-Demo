# backend/routes/nrps_routes.py

from flask import Blueprint, request, jsonify
from services.nrps_service import get_memberships

nrps_bp = Blueprint('nrps', __name__)

@nrps_bp.route('/members', methods=['GET'])
def get_members():
    """
    Retrieve membership from the LMS (NRPS).
    Needs the membership endpoint from the platform + valid OAuth token.
    """
    access_token = request.args.get('access_token')
    result = get_memberships(access_token)
    return jsonify(result), 200
