from selenium.webdriver.common.by import By
from behave import given, when,  then


@then('Search results for Amazon cart is empty are shown')
def verify_search_results(context):
    expected_result = 'Amazon cart is empty'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "[class='a-row sc-your-amazon-cart-is-empty']").text
assert expected_result==actual_result, f'Error! Expected {expected_result}, but got {actual_result}'

