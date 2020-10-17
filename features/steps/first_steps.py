# -- FILE: features/steps/example_steps.py
from behave import given, when, then


@given('A charger')
def step_impl(context):
    pass

@when('I plug my phone for {number:d} minutes')
def step_impl(context, number):
    assert number >= 60
    context.tests_count = number

@then('I will have at least {number:d}% in my phone battery')
def step_impl(context, number):
    assert number >= 50
    assert context.failed is False
    assert context.tests_count >= 0

@given('{number:d} pesos')
def step_impl(context, number):
    pass

@when('I spend {text} pesos in computer components')
def step_impl(context, text):
    try:
        text = int(text)
    except ValueError:
        text = 100000 if text == 'all' else 0
    assert text >= 100000
    text = 100000
    context.tests_count = text

@then('I will have my new computer components')
def step_impl(context):
    assert context.failed is False
    assert context.tests_count >= 0

"""
@given({number:d} computer components)
def step_impl(context, number):
    pass

@when('I spend {number:d} minutes matching computer components')
def step_impl(context, text):
    assert number >= 180
    context.tests_count = text

@then('I will have my new computer')
def step_impl(context):
    assert context.failed is False
    assert context.tests_count >= 0
"""