# backend/routes/ags_routes.py

from flask import Blueprint, request, jsonify
from services.ags_service import create_line_item, get_line_items, post_score

ags_bp = Blueprint('ags', __name__)

@ags_bp.route('/lineitems', methods=['POST'])
def create_lineitem_route():
    """
    Create a new line item in the LMS gradebook.
    Usually called after an LTI assignment is created.
    """
    data = request.json
    access_token = data.get('access_token')  # Typically an OAuth token from the platform
    lineitem_info = {
        "scoreMaximum": data.get('scoreMaximum', 100),
        "label": data.get('label', "New Assignment"),
        "tag": data.get('tag', ""),
        "resourceId": data.get('resourceId', "pdf_123"),
    }

    result = create_line_item(access_token, lineitem_info)
    return jsonify(result), 200

@ags_bp.route('/lineitems', methods=['GET'])
def get_lineitems_route():
    """
    Retrieve line items from the LMS.
    """
    access_token = request.args.get('access_token')
    items = get_line_items(access_token)
    return jsonify(items), 200

@ags_bp.route('/score', methods=['POST'])
def post_score_route():
    """
    Post a score for a user (submission).
    """
    data = request.json
    access_token = data.get('access_token')
    lineitem_url = data.get('lineitem_url')  # e.g. a specific lineitem endpoint
    user_id = data.get('user_id')
    score_given = data.get('score_given', 50)

    result = post_score(access_token, lineitem_url, user_id, score_given)
    return jsonify(result), 200
