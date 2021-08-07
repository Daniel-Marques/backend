from datetime import datetime, timedelta
from jose import jwt

import requests
import json

# CONFIG Auth0
url = 'https://fastapi-newmission.us.auth0.com/oauth/token'
headers = {'content-type': "application/json"}
CLIENT_ID = "YkMchAYZLQ9O6kWLXV1E1mEg4shUedkn"
CLIENT_SECRET = "eDYudkDiKk3vRZ2j2ouU7zUFl9uYo9bndvfbeToQ_Syr-8Y8lN-AYMAwYrrfSYxi"
AUDIENCE = "https://fastapi-newmission.us.auth0.com/api/v2/"
GRANT_TYPE = 'client_credentials'

# CONFIG JWT
SECRET_KEY = 'a3bf1113af136ad54847a795b2175108'
ALGORITHM = 'HS256'
EXPIRES_IN_MIN = 24 * 60 * 60 * 1000


def create_access_token(data: dict):
    email = data['sub']
    # Created token Auth0
    payload = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "audience": AUDIENCE,
        "grant_type": GRANT_TYPE
    }

    r = requests.post(url, data=json.dumps(payload), headers=headers)
    response = r.json()
    token = response['access_token']

    # Created token jwt
    data = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MIN)

    data.update({'access_token': token, 'sub': email, 'exp': expire})
    token_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return token_jwt


def verify_access_token(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload.get('sub')
