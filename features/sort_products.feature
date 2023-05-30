Feature: Sort products

  Scenario: Sort products by price (low to high)
    Given I am logged in
    When I sort products by price (low to high)
    Then the products should be displayed in ascending order of price

  Scenario: Sort products by price (high to low)
    Given I am logged in
    When I sort products by price (high to low)
    Then the products should be displayed in descending order of price
