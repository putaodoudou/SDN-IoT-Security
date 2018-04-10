import requests
import time
from datetime import datetime

class Cymon(object):
    def __init__(self, username, password, endpoint='https://api.cymon.io/v2'):
        self.endpoint = endpoint
        self.creds = {'username': username, 'password': password}
        self.token = None
        self.token_expiry = None

    def login(self):
        h = {'Content-Type': 'application/json'}
        r = requests.post(self.endpoint + '/auth/login', json=self.creds, headers=h)
        r.raise_for_status()
        self.token = r.json().get('jwt')
        #self.token_expiry = datetime.fromtimestamp(r.json().get('expires')) does not work
        return self.token

    def get(self, path):
        #self.check_token() didn't work
        h = {'Authorization': 'Bearer {}'.format(self.token)}
        r = requests.get(self.endpoint + path, headers=h)
        r.raise_for_status()
        return r

    def post(self, path, params):
        self.check_token()
        h = {
            'Authorization': 'Bearer {}'.format(self.token),
            'Content-Type': 'application/json'
        }
        r = requests.post(self.endpoint + path, json=params, headers=h)
        r.raise_for_status()
        return r

    ''' is not needed because it is not working
    def check_token(self):
        if self.token is None or self.token_expiry is None:
            self.login()
        if datetime.utcnow() > self.token_expiry:
            self.login()
    '''



