# backend/services/ags_service.py
import requests

def post_grade(lineitem_url, score, access_token, user_id):
    grade_payload = {
        "userId": user_id,
        "scoreGiven": score,
        "scoreMaximum": 100,
        "activityProgress": "Completed",
        "gradingProgress": "FullyGraded"
    }

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/vnd.ims.lis.v1.score+json"
    }

    response = requests.post(lineitem_url, json=grade_payload, headers=headers)
    return response.json()
