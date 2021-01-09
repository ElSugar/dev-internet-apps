from behave import given, when, then
from bridge import *


@given(u'Bridge app is run')
def step_impl(context):
    print(u'STEP: Given Bridge app is run')
    pass


@when(u'I input "{inp}" candles to put on the cake')
def step_impl(context, inp):
    print(u'STEP: When I input "{}" to put on the cake'.format(inp))
    context.result = '{}'.format(Strawberry(Candle(), inp).display_description())


@then(u'I get result "{out}"')
def step_impl(context, out):
    print(u'STEP: Then I get result "{}"'.format(out))
    assert context.result == out, 'Expected {}, got {}'.format(out, context.result)
