from behave import *


@given('we create user with duplicate credentials')
def step_impl(context):
    """
    assumes that test user is already created and attempts to create the same user again
    """
    context.execute_steps('given we create user with credentials')
