Feature: Add item to cart

  Scenario: Add item to cart
    Given I am logged in
    When I add an item to the cart
    Then the item should be added successfully
    And the cart count should increase