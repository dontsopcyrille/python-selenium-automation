from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('search for soccer ball')
def search_product(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('soccer ball')
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()
    context.driver.find_element(By. XPATH,"//a[@class='a-link-normal s-color-swatch-link puis-spacing-small s-hidden-in-quick-view']").click()
    context.driver.find_element(By.ID, 'buy-now-button').click()