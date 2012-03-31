import requests, json
from django.conf import settings

WHATCD_URL = 'https://ssl.what.cd'

login_data = {'username': settings.WHATCD_USER, 'password': settings.WHATCD_PASS}

class WhatAPI():
    def __init__(self):
        self.cookies = None
        self.login()

    def logged_in(self):
        try:
            r = requests.get('%s/ajax.php?action=index' % WHATCD_URL, cookies=self.cookies)
            return r.headers['content-type'].startswith('application/json')
        except requests.ConnectionError:
            return False

    def login(self):
        r = requests.post('%s/login.php' % WHATCD_URL, data=login_data)
        self.cookies = r.cookies
        r = requests.get('%s/ajax.php?action=index' % WHATCD_URL, cookies=self.cookies)
        res = json.loads(r.text)
        self.authkey = res['response']['authkey']

    def send_pm(self, user_id, subject, body):
        url ='%s/inbox.php?action=compose&to=%s' % (WHATCD_URL, user_id)
        data = {
            'action': 'takecompose',
            'toid': user_id,
            'auth': self.authkey,
            'subject': subject,
            'body': body,
        }
        r = requests.post(url, data=data, cookies=self.cookies)

    def get_stats(self):
        # TODO write this sheeeeeet
        pass
