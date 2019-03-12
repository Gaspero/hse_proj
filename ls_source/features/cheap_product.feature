# Created by vasilii at 19.01.2019
Feature: Find the cheapest product
  # Enter feature description here

  Scenario: We have the cheapest product and show it
    Given I have a set of products
        | name             | category    | producer    | price |
        | Harry Potter     | Book        | not me      | 15.99 |
        | Name of the Rose | Book        | somebody    | 39.99 |
        | iPhone X         | Electronics | apple       | 299.99|

    When I ask for the cheapest product
    Then System shows Harry Potter

  Scenario: We have more than one cheapest product
    Given I have a set of products
        | name             | category    | producer    | price |
        | Harry Potter     | Book        | not me      | 15.99 |
        | Name of the Rose | Book        | somebody    | 39.99 |
        | iPhone X         | Electronics | apple       | 15.99|

    When I ask for the cheapest product
    Then System shows Harry Potter
    And System shows iPhone X