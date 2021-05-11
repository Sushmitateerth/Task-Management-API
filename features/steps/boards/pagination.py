import requests
from behave import *
from http import HTTPStatus
from util.logger import log_response

from features.steps.boards.data import params

skip = 4
limit = 3


@when(u'we fetch boards with pagination parameters')
def step_impl(context):
    context.search_response = requests.get(f"{context.base_url}/boards/?skip={skip}&limit={limit}",
                                           headers=context.headers)
    log_response(context.search_response)
    context.json_response = context.search_response.json()


@then(u'verify relevant boards are returned')
def step_impl(context):
    assert context.search_response.status_code == HTTPStatus.OK
    expected_list = params.boards[skip: skip + limit:]
    for actual, expected in zip(expected_list, context.json_response):
        assert actual['title'] == expected['title']
        assert actual['description'] == expected['description']
