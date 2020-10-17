Feature: charger

  Scenario:
     Given A charger
      When I plug my phone for 60 minutes
      Then I will have at least 50% in my phone battery
