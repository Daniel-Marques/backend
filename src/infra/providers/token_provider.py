from datetime import datetime, timedelta
from jose import jwt

# import requests
# import json

# CONFIG Auth0
url = ""
headers = {'content-type': "application/json"}
CLIENT_ID = ""
CLIENT_SECRET = ""
AUDIENCE = ""
GRANT_TYPE = 'client_credentials'

# CONFIG JWT
SECRET_KEY = 'a3bf1113af136ad54847a795b2175108'
ALGORITHM = 'HS256'
EXPIRES_IN_MIN = 24 * 60 * 60 * 1000


def create_access_token(data: dict):
    data = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MIN)

    data.update({'exp': expire})
    token_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return token_jwt


def verify_access_token(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload.get('sub')
