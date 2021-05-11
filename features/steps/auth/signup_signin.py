import time

import jwt
import requests

from behave import *
from http import HTTPStatus
from util.time import num_seconds
from util.logger import log_response

jwt_buffer = 1

@given('we create user with credentials')
def step_impl(context):
    """
    attempts to create a new user
    uses user dict from context set in before_all
    """
    context.response = requests.post(f"{context.base_url}/auth/signup", json=context.user)


@then('user creation "{is_created}"')
def step_impl(context, is_created):
    """
    verifies success and failure cases defined as two different scenarios in auth.feature
    """
    json = context.response.json()
    log_response(context.response, "user is created")

    if is_created == "succeeds":
        assert context.response.status_code == HTTPStatus.CREATED
        assert json['id'] > 0
        assert json['username'] == context.user['username']

        context.response = json

    elif is_created == "fails":
        assert context.response.status_code == HTTPStatus.CONFLICT
        assert json['statusCode'] == HTTPStatus.CONFLICT
        assert f"username {context.user['username']} already exists" in json['errors']


@then('user can signin')
def step_impl(context):
    """
    attempts to sign in with previously created user
    verifies JWT
    """
    response = requests.post(f"{context.base_url}/auth/signin", json=context.user)
    json = response.json()
    log_response(response, "user can signin")

    assert response.status_code == HTTPStatus.OK

    jwt_payload = jwt.decode(json['token'], options={'verify_signature': False})
    assert jwt_payload['id'] == context.response['id']
    assert jwt_payload['username'] == context.response['username']

    current_time = int(time.time())
    assert current_time >= jwt_payload['iat'] >= current_time - jwt_buffer

    expected_exp = jwt_payload['iat'] + num_seconds()
    assert jwt_payload['exp'] == expected_exp


