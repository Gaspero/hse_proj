# -*- coding: utf-8 -*-

from behave import given, when, then


@given('APP is setup')
def flask_setup(context):
    assert context.client and context.db


@when('i call root page')
def root(context):
    context.page = context.client.get('/', follow_redirects=True)
    assert context.page


@then('i should see the alert "{message}"')
def logged_in(context, message):
    assert message in str(context.page.data)


# @given('i login with "{username}" and "{password}"')
# @when('i login with "{username}" and "{password}"')
# def login(context, username, password):
#     context.page = context.client.post('/login', data=dict(
#         username=username,
#         password=password
#     ), follow_redirects=True)
#     assert context.page
#
#
# @when('i logout')
# def logout(context):
#     context.page = context.client.get('/logout', follow_redirects=True)
#     assert context.page
#
#
# @then('i should see the alert "{message}"')
# def logged_in(context, message):
#     assert message in context.page.data
