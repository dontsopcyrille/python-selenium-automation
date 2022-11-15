Feature: Tests for Amazon Best Sellers page

  Scenario: Amazon Best Sellers page is present
    Given Open amazon page
    Then Verify there are  5 links

  Scenario: Header has correct amount of links
    Given Open amazon page
    Then Verify that header has 5 links