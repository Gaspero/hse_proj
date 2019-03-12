Feature: Searching inventory description

  Scenario: Find item in inventory by title
     Given a set of items in category
        | name        |
        | Book        |
        | Electronics |
       And  a set of items in inventory
        | name             | category_id | producer    | price  |
        | Harry Potter     | 1           | not me      | 15.99  |
        | Name of the Rose | 1           | somebody    | 39.99  |
        | iPhone X         | 2           | apple       | 299.99 |
    When we search for items with name "Harry Potter"
    Then we will find 1 Book items

#  Scenario: Find items in inventory by category
#     Given a set of items in inventory
#        | name             | category    | producer    | price |
#        | Harry Potter     | Book        | not me      | 15.99 |
#        | Name of the Rose | Book        | somebody    | 39.99 |
#        | iPhone X         | Electronics | apple       | 299.99 |
#    When we search for items with category "Book"
#    Then we will find 2 Book items
#
#  Scenario: Find all info about the cheapest good
#     Given a set of items in inventory
#        | name             | category    | producer    | price |
#        | Harry Potter     | Book        | not me      | 15.99 |
#        | Name of the Rose | Book        | somebody    | 39.99 |
#        | iPhone X         | Electronics | apple       | 299.99 |
#    When we search for items with lowest price
#    Then we will get info for 1 items with name "Harry Potter"