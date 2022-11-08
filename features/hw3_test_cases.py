# Find Amazon registration logo By class
driver.find_element(By.CSS_SELECTOR, ".a-icon.a-icon-logo")

# Find Amazon create account element By class + class
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

# Find Amazon your name bar element By ID
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")

# Find Amazon email element By attribute
driver.find_element(By.CSS_SELECTOR, "[for='ap_email']")

# Find Amazon password bar element By attribute
driver.find_element(By.CSS_SELECTOR, "[name='password']")

# Find Amazon Re-enter password bar element By ID
driver.find_element(By.CSS_SELECTOR, "#ap_password_check")

# Find  Amazon continue(create your Amazon account) bar element By ID
driver.find_element(By.CSS_SELECTOR, "#continue")

# Find  Amazon conditions of use By partial attribute
driver.find_element(By.CSS_SELECTOR, "a[href*='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use']")

# Find Amazon privacy notice bar element By ID
driver.find_element(By.CSS_SELECTOR, "#legalTextRow")

# Find Amazon sign in  element By attribute
driver.find_element(By.CSS_SELECTOR, "[class='a-link-emphasis']")







