import requests
from behave import *
from http import HTTPStatus

from util.logger import log_response


@when('we fetch boards list with search parameter')
def step_impl(context):
    context.title = 'eight'
    context.response = requests.get(f"{context.base_url}/boards?search={context.title}", headers=context.headers)
    log_response(context.response, context)


@then('relevant boards are returned')
def step_impl(context):
    json = context.response.json()
    assert context.response.status_code == HTTPStatus.OK
    assert json[0]['title'] == context.title
