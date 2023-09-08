from behave import *


@given("I am on the login page")
def step_impl(context):
    context.login_page.navigate_to_login_page()


@when("I introduce an unregistered email in the email field")
def step_impl(context):
    context.login_page.set_email("kogtrdfgh989@yahoo.com")


@when("I introduce the password")
def step_impl(context):
    context.login_page.set_password()


@when("I click on the login button")
def step_impl(context):
    context.login_page.click_login_button()


@then('the error message is displayed "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later."')
def step_impl(context):
    assert "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later." in context.login_page.get_main_error_message()


