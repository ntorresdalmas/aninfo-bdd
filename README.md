# aninfo-bdd

Command line:

$ mvn features


//TODO
.feature
Feature: gaming




  Scenario: a computer upgrade
    Given I have more computer memory available
    When I spend 5 minutes placing my new computer memory
    Then I will have an upgrade in my computer



.py
@given('{number:d} pesos')
def step_impl(context, number):
    pass

@when('I spend {number:d} pesos in computer components')
def step_impl(context, number):
    assert number >= 100000
    context.tests_count = number

@then('I will have my new computer components')
def step_impl(context):
    assert context.failed is False
    assert context.tests_count >= 0