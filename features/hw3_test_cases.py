from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\donts\\Desktop\\Automation\\python-selenium-automation\\chromedriver.exe")
driver.get('https://www.amazon.com/')
driver.find_element(By.CSS_SELECTOR, "#nav-cart-count").click()
expected_result = 'Your Amazon Cart is empty'
actual_result = driver.find_element(By.CSS_SELECTOR, "[class='a-row sc-your-amazon-cart-is-empty']").text
assert expected_result==actual_result, f'Error! Expected {expected_result}, but got {actual_result}'
print('Test case passed')


