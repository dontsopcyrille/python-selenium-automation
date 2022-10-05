# Created by donts at 10/2/2022
Feature:  Tests for amazon search
    Scenario: user search for a product
    Given open amazon page
      When Search for soccer ball
      Then  Search results for sign in page opened sign in header is visible