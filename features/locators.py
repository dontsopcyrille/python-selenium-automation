from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\donts\\Desktop\\Automation\\python-selenium-automation\\chromedriver.exe")

# by ID

driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('coffee')


# by XPATH (all the bellow:tag only,attribute only,text,multiples attributes,multiples attributes etc..) are type of xpath?
driver.find_element(By.XPATH, "//a[@href='/ref=nav_logo']")
driver.find_element(By.XPATH, "//a[@class='nav-logo-link nav-progressive-attribute']")

# by tag only
driver.find_element(By.XPATH, "//input")
# by attribute only
driver.find_element(By.XPATH, "//*[@class='nav-logo-link nav-progressive-attribute']")
driver.find_element(By.XPATH, "//*[@href='/ref=nav_logo']")

# by text
driver.find_element(By.XPATH, "//a[text()='Back to School']")
# by multiple attributes
driver.find_element(By.XPATH, "//a[@class='nav-a  ' and @href='/backtoschool?ref_=nav_cs_bts']")
# by multiple attributes and text
driver.find_element(By.XPATH, "//a[@class='nav-a  ' and @href='/backtoschool?ref_=nav_cs_bts' and text()='Back to School']")

# by partial text / attributes => contains()
driver.find_element(By.XPATH, "//a[contains(text(), 'Back to')]")
driver.find_element(By.XPATH, "//a[contains(@href, 'backtoschool')]")

# By multiple nodes:
driver.find_element(By.XPATH, "//div[@id='nav-xshop-container']//a[contains(@href, 'new-releases')]")