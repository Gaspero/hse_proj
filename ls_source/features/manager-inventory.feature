# Created by ilya at 19.01.2019
Feature: Managing Inventory
  Template

  Scenario: Add items to inventory
     Given a set of items arrived from AlphaBeta Ltd
        | name             | category    | producer    | price |
        | Harry Potter     | Book        | not me      | 15.99 |
        | Name of the Rose | Book        | somebody    | 39.99 |
        | iPhone X         | Electronics | apple       | 299.99 |
    When we add items to inventory
    Then we will find 2 Books items in inventory
     But we will find 1 Electronics items in inventory