# Created by ivanshadrin at 2019-04-11
Feature: Auto-assigning producer based on order's district

  Scenario: There is valid producer for this district
    # Enter steps here
    Given a set of producers
      | name      | district    | address    | workers  | working_hours  |
      | Place1    | Vyborgskiy  | Severniy   | 1        | 10-21          |
      | Place2    | Primorskiy  | Kultury    | 2        | 10-23          |
      | Place3    | Centralniy  | Moyki      | 3        | 10-22          |
      And  an order
      | customer_id   | order_status | district    |
      | Test User     | Pre-order    | Vyborgskiy  |
    When I confirm order
    Then System updates district of the order to Vyborgskiy
#  Scenario: There are more than one valid producers for this district



#  Scenario: There are no valid producers for this district