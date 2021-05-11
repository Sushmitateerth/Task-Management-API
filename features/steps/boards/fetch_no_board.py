import requests
from behave import *
from http import HTTPStatus
from util.logger import log_response

id = 1


@given('we fetch non existent board by id')
def step_impl(context):
    context.response = requests.get(f"{context.base_url}/boards/{id}", headers=context.headers)

@then('board not found error is thrown')
def step_impl(context):
    assert context.response.status_code == HTTPStatus.NOT_FOUND
    assert 'board with id {} not found'.format(id) in context.response.json()['errors']
