"""
Original auther:
Github: juliuspleunes4
"""

import google.oauth2.service_account
import google.auth.transport.requests


"""
Path to service account key (the .json file)
NOTE: If you use \ instead of / make sure to put r in front of the " !
Example: r"Path\To\Key.json" ✅
Example: "Path/To/Key.json" ✅
"""
SERVICE_ACCOUNT_FILE = "PATH TO JSON FILE"

"""
OAuth 2.0 scope for FCM
"""
SCOPES = ["https://www.googleapis.com/auth/cloud-platform"]

"""
Generates the token
"""
credentials = google.oauth2.service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)

request = google.auth.transport.requests.Request()
credentials.refresh(request)

print("Access Token:", credentials.token)
