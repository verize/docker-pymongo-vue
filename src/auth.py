"""
    Auth-BCrypt
    ~~~~~~~~~~~

    Securing an Eve-powered API with Basic Authentication (RFC2617).

    You will need to install py-bcrypt: ``pip install py-bcrypt``

    This snippet by Nicola Iarocci can be used freely for anything you like.
    Consider it public domain.
"""

import bcrypt
from eve.auth import BasicAuth
from flask import current_app as app


class BCryptAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        # use Eve's own db driver; no additional connections/resources are used
        accounts = app.data.driver.db['users']
        account = accounts.find_one({'email': username})
        return account and \
               bcrypt.hashpw(password, account['password']) == account['password']
