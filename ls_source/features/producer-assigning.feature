# Created by ivanshadrin at 2019-04-11
Feature: Auto-assigning producer based on order's district

  @fixture.flaskr_client
  Scenario: There is valid producer for this district
    Given a set of producers
      | name      | district    | address    | workers  | working_hours  |
      | Place1    | Vyborgskiy  | Severniy   | 1        | 10-21          |
      | Place2    | Primorskiy  | Kultury    | 2        | 10-23          |
      | Place3    | Centralniy  | Moyki      | 3        | 10-22          |
    And an order
      | customer_id   | order_status | district    |
      | Test User     | Pre-order    | Vyborgskiy  |
    When I confirm order
    Then System sets producer for given order to Place1
    And Order status is Payment

  @fixture.flaskr_client
  Scenario: There are no valid producers for this district
    Given a set of producers
      | name   | district   | address | workers | working_hours |
      | Place2 | Primorskiy | Kultury | 2       | 10-23         |
      | Place3 | Centralniy | Moyki   | 3       | 10-22         |
      | Place4 | Kurortniy  | Vokzal  | 1       | 10-21         |
    And an order
      | customer_id | order_status | district   |
      | Test User   | Pre-order    | Vyborgskiy |
    When I confirm order
    Then Producer for given order is not provided
    And Order status is Pre-order

#   Scenario: There are more than one valid producers for this district