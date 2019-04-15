# Created by ivanshadrin at 2019-04-14
Feature: Product sorting and filtering

  Scenario: Sort products by price
    Given a set of products
      | name      | price | description    |
      | Pen       | 30    | nice pen       |
      | Pineapple | 10    | nice pineapple |
      | Apple     | 20    | nice apple     |
    When I sort products by price ascending
    Then System returns the following set
      | name      | price | description    |
      | Pineapple | 10    | nice pineapple |
      | Apple     | 20    | nice apple     |
      | Pen       | 30    | nice pen       |

#  Scenario: Sort products by ProductIngredients