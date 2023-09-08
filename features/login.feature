
  Feature: Test the login module
    Scenario: Test unregistered email for "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later." when the user tries to log in with an unregistered email
      Given I am on the login page
      When I introduce an unregistered email in the email field
      And I introduce the password
      And I click on the login button
      Then the error message is displayed "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later."

