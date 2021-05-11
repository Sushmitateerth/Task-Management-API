import requests
from behave import *
from http import HTTPStatus
from util.logger import log_response

user = {
    'username': 'test user',
    'password': 'Pa!2'
}



@given('we create new user with < 8 character password')
def step_impl(context):
    context.response = requests.post(f"{context.base_url}/auth/signup", json=user)


@then('bad request error is thrown with message')
def step_impl(context):
    assert context.response.status_code == HTTPStatus.BAD_REQUEST
    assert 'password must be longer than or equal to 8 characters' in context.response.json()['errors']


@then('user cannot signin')
def step_impl(context):
    context.response = requests.post(f"{context.base_url}/auth/signin", json=context.user)
    log_response(context.response)
    assert context.response.status_code == HTTPStatus.UNAUTHORIZED
    assert 'Unauthorized' in context.response.json()['errors']
