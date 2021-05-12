import json

import requests
from behave import *

from features.steps.boards.data import params
from util.logger import log_response
from http import HTTPStatus


@when(u'we fetch boards list with sort parameter')
def step_impl(context):
    sort_input = [
        {
            "description": "asc"
        }
    ]
    context.sort_response = requests.get(f"{context.base_url}/boards/?sort={json.dumps(sort_input)}",
                                         headers=context.headers)
    log_response(context.sort_response, context)
    context.actual_result = context.sort_response.json()


@then(u'boards are returned right order')
def step_impl(context):
    assert context.sort_response.status_code == HTTPStatus.OK
    for actual, expected in zip(context.actual_result, params.sort_by_description):
        assert actual['description'] == expected['description']
