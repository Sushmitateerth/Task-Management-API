import requests
from behave import *
from http import HTTPStatus
from util.logger import log_response

user_cred = {
    'username': 'user',
    'password': 'Pa!2'
}


@given('we create new user with < 8 character password')
def step_impl(context):
    context.response = requests.post(f"{context.base_url}/auth/signup", json=user_cred)


@then('bad request error is thrown with message')
def step_impl(context):
    assert context.response.status_code == HTTPStatus.BAD_REQUEST
    assert 'password must be longer than or equal to 8 characters' in context.response.json()['errors']


@then('user cannot signin')
def step_impl(context):
    response = requests.post(f"{context.base_url}/auth/signin", json=user_cred)
    log_response(response, context)
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert 'Unauthorized' in response.json()['errors']
