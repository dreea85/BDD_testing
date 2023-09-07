
  Feature: Test the login module
    Scenario: Test unregistered email for "Your email or password is not valid."
      when the user tries to log in with an unregistered email
      Given I am on the login page
      When I introduce an unregistered email in the email field
      And I introduce the password
      And I click on the login button
      Then the error message is displayed "Your email or password is not valid."

