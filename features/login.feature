Feature: Login functionality

  Scenario: Successful login
    Given I am on the login page
    When I enter valid credentials
    And click on the login button
    Then I should be logged in successfully
    And redirected to the products page
