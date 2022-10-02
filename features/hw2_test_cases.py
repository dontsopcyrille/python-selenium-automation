from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="C:\\Users\\donts\\Desktop\\Automation\\python-selenium-automation\\chromedriver.exe")
driver.get('https://www.amazon.com/')
# driver.refresh() will refresh your page in case sometimes a webpage asked you for captcha verification
driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('soccer ball')
driver.find_element(By.ID, 'nav-search-submit-button').click()
driver.find_element(By.XPATH, "//a[@class='a-link-normal s-color-swatch-link puis-spacing-small s-hidden-in-quick-view']").click()
driver.find_element(By.ID, 'buy-now-button').click()

expected_result = 'Sign in'
actual_result = driver.find_element(By.XPATH, "//*[@class='a-spacing-small']").text
assert expected_result==actual_result, f'Error! Expected {expected_result}, but got {actual_result}'
print('Test case passed')
# this is how you verify additional element. the Email field not found wont be found obviously cause amazon does not have that returm
# just locate the email field ap_email and input it on the script. make sure element is present somewhere on script
#.is_display actually make sure the test exist on the page
# assert driver.find_element(By.ID, 'ap_email') 'Email field not found' is the original command and we add .is_displayed for extra verification
#assert driver.find_element(By.ID, 'ap_email') 'Email field not found'.is_displayed
