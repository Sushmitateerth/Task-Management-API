import json

import requests
from behave import *

from features.steps.boards.data import params
from http import HTTPStatus


@when('we fetch boards list with filter parameter')
def step_impl(context):
    context.board_index = int(len(context.list) / 2)
    middle_board = context.list[context.board_index]
    context.created_at = middle_board['createdAt']


@then('related boards are returned')
def step_impl(context):
    api_filter = {
        "createdAt": {
            "gt": context.created_at
        }
    }

    # json.dumps converts dictionary to json
    response = requests.get(f"{context.base_url}/boards/?filter={json.dumps(api_filter)}", headers=context.headers)
    json_response = response.json()
    assert response.status_code == HTTPStatus.OK

    # list slicing so that parmas.board will be obtained from middle index for comparision
    expected_board = params.boards[context.board_index + 1:len(params.boards):]
    for actual, expected in zip(json_response, expected_board):
        assert actual['title'] == expected['title']
        assert actual['description'] == expected['description']
