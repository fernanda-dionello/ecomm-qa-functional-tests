Feature: Logout functionality

  Scenario: Successful logout
    Given I am logged in
    When I click on the logout button
    Then I should be logged out successfully
    And redirected to the login page
