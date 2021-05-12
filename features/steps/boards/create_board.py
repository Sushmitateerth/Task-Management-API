import requests

from behave import *
from http import HTTPStatus
from util.time import to_epoch
from util.logger import log_response

created_at_buffer = 1
payload = {'title': 'test board'}


@given('we create board with correct payload')
def step_impl(context):
    """
    attempts to create a new board
    uses payload and headers from context set in before_tag
    """
    context.response = requests.post(f"{context.base_url}/boards", json=payload, headers=context.headers)


@then('board creation "{is_created}"')
def step_impl(context, is_created):
    """
    verifies the created board
    """
    context.json = context.response.json()
    log_response(context.response, context)

    if is_created == "succeeds":
        assert context.response.status_code == HTTPStatus.CREATED
        assert context.json['id'] > 0
        assert context.json['description'] is None
        assert context.json['title'] == payload['title']
        assert to_epoch(context.json['createdAt']) - to_epoch(context.json['updatedAt']) <= created_at_buffer

    elif is_created == "fails":
        assert context.response.status_code == HTTPStatus.BAD_REQUEST
        assert 'title should not be empty' in context.response.json()['errors']


@then('board can be fetched by ID')
def step_impl(context):
    context.search = requests.get(f"{context.base_url}/boards/{context.json['id']}", headers=context.headers)
    assert context.search.json()['id'] == context.json['id']
    assert context.search.status_code == HTTPStatus.OK
