Scenario: Footer has correct amount of links
    Given Open amazon page
    Then Verify that footer has 38 links

  Scenario: User can see language options
    Given Open Amazon page
    When Hover over language options
    Then Verify Spanish option present