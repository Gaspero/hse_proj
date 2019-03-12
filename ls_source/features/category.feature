# Created by ilya at 19.01.2019

Feature: Work with Category
  # Enter feature description here

  Scenario: Get categories
    Given APP is setup
    When i call categories
    Then i should see "1" records