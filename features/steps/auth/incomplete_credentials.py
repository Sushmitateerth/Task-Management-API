import requests
from behave import *
from util.logger import log_response
from http import HTTPStatus

user_info = {
    'username': 'test user',
    'password': ''
}


@given('user exists')
def step_impl(context):
    context.execute_steps('given we create user with credentials')


@when('we signin with only username')
def step_impl(context):
    context.response = requests.post(f"{context.base_url}/auth/signin", json=user_info)


@then('bad request error is thrown')
def step_impl(context):
    assert context.response.status_code == HTTPStatus.BAD_REQUEST
    assert 'password should not be empty' in context.response.json()['errors']
