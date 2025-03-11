# backend/services/nrps_service.py

import requests
from config import Config

def get_memberships(access_token):
    """
    GET /memberships
    Requires the platform's membership URL + OAuth2 token.
    """
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/vnd.ims.lti-nrps.v2.membershipcontainer+json"
    }
    # Could also be a dynamic membership URL from the LTI launch claims
    url = Config.NRPS_MEMBERSHIPS_URL

    response = requests.get(url, headers=headers)
    return response.json()
