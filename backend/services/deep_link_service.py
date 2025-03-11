# backend/services/deep_link_service.py

import jwt
import time
from config import Config

def build_deep_link_jwt(decoded_launch, resource_link_id="pdf_123"):
    """
    Build a Deep Linking Response JWT that the LMS will consume.
    Usually posted to 'deep_link_return_url' from decoded_launch.
    """

    # The LMS often includes a claim for deep linking settings:
    # "https://purl.imsglobal.org/spec/lti-dl/claim/deep_linking_settings"
    dl_settings = decoded_launch.get("https://purl.imsglobal.org/spec/lti-dl/claim/deep_linking_settings", {})
    deep_link_return_url = dl_settings.get("deep_link_return_url", "")

    now = int(time.time())

    # A typical deep link response includes context about the content item.
    # This is a minimal example. The LMS expects a "https://purl.imsglobal.org/spec/lti-dl/claim/content_items"
    # array describing the resource.
    deep_link_payload = {
        "iss": Config.LTI_CLIENT_ID,
        "aud": decoded_launch["iss"],
        "iat": now,
        "exp": now + 300,
        "nonce": decoded_launch["nonce"],

        "https://purl.imsglobal.org/spec/lti/claim/message_type": "LtiDeepLinkingResponse",
        "https://purl.imsglobal.org/spec/lti/claim/version": "1.3.0",

        # The content items you want to pass back:
        "https://purl.imsglobal.org/spec/lti-dl/claim/content_items": [
            {
                "type": "ltiResourceLink",
                "title": "My PDF Assignment",
                "url": f"https://your.tool.com/lti/launch?resource_link_id={resource_link_id}",
                "presentation": {
                    "documentTarget": "iframe"
                }
            }
        ],

        # Deep linking settings claim
        "https://purl.imsglobal.org/spec/lti-dl/claim/data": dl_settings.get("data", "")
    }

    deep_link_jwt = jwt.encode(deep_link_payload, Config.SECRET_KEY, algorithm="HS256")
    return deep_link_jwt
