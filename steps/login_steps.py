from behave import *

@given("I am on the login page")
def step_impl(context):
    context.login_page.navigate_to_login_page()

@when("I introduce an unregistered email in the email field")
def step_impl(context):
    context.login_page.set_email()

@when("I introduce the password")
def step_impl(context):
    context.login_page.set_password()

@when("I click on the login button")
def step_impl(context):
    context.login_page.click_login_button()

@then('the error message is displayed "Your email or password is not valid."')
def step_impl(context):
    assert context.login_page.is_main_error_message_displayed()


