Feature: charger

  Scenario: buy new computer components
     Given 100000 pesos
      When I spend 100000 pesos in computer components
      Then I will have my new computer components

  Scenario: a new computer
     Given 5 computer components
     When I spend 2 hour matching computer components
     Then I will have my new computer
