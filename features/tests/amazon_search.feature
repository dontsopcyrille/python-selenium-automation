# Created by donts at 10/1/2022
Feature:  Tests for amazon search
  Scenario: user search for a product
    Given open amazon page
    When Search for coffee
    Then  Search results for coffee are shown
