
import requests
from behave import *
from features.steps.boards.data import params
from http import HTTPStatus


@given('a set of boards')
def step_impl(context):
    context.list = []
    for board in params.boards:
        response = requests.post(f"{context.base_url}/boards", json=board, headers=context.headers)
        json = response.json()
        context.list.append(json)


@when('we fetch boards list')
def step_impl(context):
    context.response = requests.get(f"{context.base_url}/boards", headers=context.headers)


@then('boards are returned')
def step_impl(context):
    assert context.response.status_code == HTTPStatus.OK
    json = context.response.json()

    assert len(params.boards) == len(json)
    for expected, actual in zip(params.boards, json):
        assert expected['title'] == actual['title']
        assert expected['description'] == actual['description']
        assert actual['id'] > 0


