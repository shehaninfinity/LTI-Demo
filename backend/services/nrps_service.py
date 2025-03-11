# backend/services/nrps_service.py
import requests

def get_roster(nrps_url, access_token):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/vnd.ims.lti-nrps.v2.membershipcontainer+json"
    }
    response = requests.get(nrps_url, headers=headers)
    return response.json()
