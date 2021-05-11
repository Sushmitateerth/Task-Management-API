import jwt
import requests

from constants import base_url
from http import HTTPStatus


def before_all(context):
    """
    creates payload for a new user
    adds base_url to context
    """
    context.user = {
        'username': 'test user',
        'password': 'Password123!',
    }
    context.base_url = base_url


def before_tag(context, tag):
    """
    creates a new user (will not throw error if user already exists)
    signs in as that user
    adds JWT token to context
    apply @signin tag to scenario for signing in
    """
    if tag != 'signin':
        pass

    requests.post(f"{context.base_url}/auth/signup", json=context.user)

    response = requests.post(f"{context.base_url}/auth/signin", json=context.user)
    assert response.status_code == HTTPStatus.OK

    token = response.json()['token']
    context.headers = {"Authorization": f"Bearer {token}"}
    jwt_payload = jwt.decode(token, options={'verify_signature': False})
    context.user_id = jwt_payload['id']
