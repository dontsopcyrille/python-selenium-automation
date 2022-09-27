#  locate amazon sign in  logo  by attribute only
driver.find_element(By.XPATH, "//*[@class='a-icon a-icon-logo']")
#  locate amazon email field   by ID
driver.find_element(By.ID, 'ap_email')

# locate amazon continue button by attribute only
driver.find_element(By.XPATH, "//*[@aria-labelledby='continue-announce']")

# locate amazon need help link by  attribute
driver.find_element(By.XPATH, "//*[@class='a-expander-prompt']")
#  locate amazon forgot password link by  ID
driver.find_element(By.ID, 'auth-fpp-link-bottom')

#  locate amazon other issue with sigh in link by  ID
driver.find_element(By.ID, 'ap-other-signin-issues-link')
#  locate create your amazon account button by  attribute only
driver.find_element(By.XPATH, "//*[@class='a-button-text']")



