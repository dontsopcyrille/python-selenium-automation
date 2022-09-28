from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\donts\\Desktop\\Automation\\python-selenium-automation\\chromedriver.exe")
driver.get('https://www.amazon.com/')
driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('soccer ball')
driver.find_element(By.ID, 'nav-search-submit-button').click()
driver.find_element(By.XPATH, "//a[@class='a-link-normal s-color-swatch-link puis-spacing-small s-hidden-in-quick-view']").click()
driver.find_element(By.ID, 'buy-now-button').click()

expected_result = 'Sign in'
actual_result = driver.find_element(By.XPATH, "//*[@class='a-spacing-small']").text
assert expected_result==actual_result, f'Error! Expected {expected_result}, but got {actual_result}'
print('Test case passed')

