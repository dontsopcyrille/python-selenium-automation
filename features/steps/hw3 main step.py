from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('click on the cart icon')
def search_product(context):
    context.driver.find_element(By.CSS_SELECTOR,"#nav-cart-count").click()
