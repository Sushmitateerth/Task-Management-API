import requests
from behave import *

board = {
  "title": "",
  "description": "None",
  "participants": [
    0
  ]
}

@given('we create board with incorrect payload')
def step_impl(context):
    context.response = requests.post(f"{context.base_url}/boards", json=board, headers=context.headers)
