# Created by donts at 10/2/2022
  Feature:Tests for amazon cart icon
    Scenario:user clicks on the cart
      Given open amazon page
        When click on the cart icon
      Then  Amazon cart is empty