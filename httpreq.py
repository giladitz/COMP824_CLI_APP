import requests
from requests.auth import HTTPBasicAuth

CREATE_USER_URI = 'https://auth.tradies.live/tokens/'


def create_user(user, passw):
    response = requests.request(method='POST',
                                url=CREATE_USER_URI,
                                headers={"User-Agent": "Tradies/1.0"},
                                auth=HTTPBasicAuth(user, passw))
    if response.status_code != 200:
        return False, "Create user request failed: {}".format(response.json().get('error', ''))

    return True, response.json()
