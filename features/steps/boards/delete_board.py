import requests
from behave import *
from http import HTTPStatus


@given('board exists')
def step_impl(context):
    context.execute_steps('given we create board with correct payload')


@when('board is deleted by ID')
def step_impl(context):
    context.created_boardID = context.response.json()['id']
    context.response = requests.delete(f"{context.base_url}/boards/{context.created_boardID}", headers=context.headers)


@then('board deletion succeeds')
def step_impl(context):
    context.response.status_code == HTTPStatus.OK


@then('board cannot be fetched by ID')
def step_impl(context):
    context.response = requests.get(f"{context.base_url}/boards/{context.created_boardID}", headers=context.headers)
    assert context.response.status_code == HTTPStatus.NOT_FOUND
    assert 'board with id {} not found'.format(context.created_boardID) in context.response.json()['errors']
