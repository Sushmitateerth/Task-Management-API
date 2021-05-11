import requests
from behave import *
from http import HTTPStatus

user = {
    'username': 'test user',
    'password': 'abc'
}


@given('user already exists')
def step_impl(context):
    context.execute_steps('given user exists')


@when('we signin with incorrect password')
def step_impl(context):
    context.response = requests.post(f"{context.base_url}/auth/signin", json=user)


@then('unauthorized error is thrown with message')
def step_impl(context):
    assert context.response.status_code == HTTPStatus.UNAUTHORIZED
    assert 'Unauthorized' in context.response.json()['errors']
