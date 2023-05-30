Feature: Remove item from cart

  Scenario: Remove item from cart
    Given I am logged in
    And there is an item in the cart
    When I remove the item from the cart
    Then the item should be removed successfully
    And the cart count should decrease
