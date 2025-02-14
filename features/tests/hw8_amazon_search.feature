
Feature: Tests for amazon search
  Scenario: User can search for coffee
    Given Open amazon page
    When Search for coffee
    Then Search results for "coffee" are shown
#

#  Scenario: User can search for mug
#    Given Open amazon page
#    When Search for mug
#    Then Search results for "mug" are shown
   Scenario Outline: User can search for a product
    Given Open amazon page
    When Search for <product>
    Then Search results for <search_result> are shown
   Examples:
     |product                                 |search_result                             |
     |coffee                                  |"coffee"                                  |
     |mug                                     |"mug"                                     |
     |dress                                   |"dress"                                   |
     |Tritan Farm to Table Pitcher on amazon  |"Tritan Farm to Table Pitcher on amazon"  |
     |Tritan Farm to Table Pitcher on amazon  |"Tritan Farm to Table Pitcher"  |

   Scenario: User can add a product to the cart
    Given Open Amazon page
    When Search for Tritan Farm to Table Pitcher on amazon
    And Click on the first product
    And Store product name
    And Click on Add to cart button
    And Open cart page
    Then Verify cart has 1 item(s)
    And Verify cart has correct product
    And Verify cart has correct product

  Scenario: Verify that user can see product names and images
    Given Open Amazon page
    When Search for coffee
    Then Verify that every product has a name and an image

  Scenario Outline: User can select and search in a department
    Given Open Amazon page
    When Select department by value <value>
    And Search for Faust
    Then Verify <department> department is selected
    Examples:
    |value        |department |
    |stripbooks   |books      |
    |audible      |audible    |