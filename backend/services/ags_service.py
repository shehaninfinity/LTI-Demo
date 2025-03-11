# backend/services/ags_service.py

import requests
from config import Config

def create_line_item(access_token, lineitem_info):
    """
    Create a line item at the platform's endpoint. This typically means:
      POST /lineitems
    with a JSON body specifying the assignment details.
    """
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/vnd.ims.lis.v2.lineitem+json"
    }
    payload = {
        "scoreMaximum": lineitem_info.get("scoreMaximum", 100),
        "label": lineitem_info.get("label", "Assignment"),
        "tag": lineitem_info.get("tag", "example-tag"),
        "resourceId": lineitem_info.get("resourceId", "example-resource"),
        "startDateTime": "2020-01-01T00:00:00Z",
        "endDateTime": "2030-01-01T00:00:00Z"
    }
    response = requests.post(Config.AGS_LINEITEMS_URL, headers=headers, json=payload)
    return response.json()

def get_line_items(access_token):
    """
    Retrieve existing line items from the platform. Typically:
      GET /lineitems
    """
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/vnd.ims.lis.v2.lineitemcontainer+json"
    }
    response = requests.get(Config.AGS_LINEITEMS_URL, headers=headers)
    return response.json()

def post_score(access_token, lineitem_url, user_id, score):
    """
    Post a score for a user to a specific lineitem:
      POST /lineitems/{id}/scores
    """
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/vnd.ims.lis.v1.score+json"
    }
    payload = {
        "userId": user_id,
        "scoreGiven": score,
        "scoreMaximum": 100,
        "comment": "Submitted",
        "timestamp": "2025-01-01T00:00:00Z",
        "activityProgress": "Completed",
        "gradingProgress": "FullyGraded"
    }
    response = requests.post(lineitem_url, headers=headers, json=payload)
    return response.json()
