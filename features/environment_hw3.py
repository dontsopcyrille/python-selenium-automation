from selenium import webdriver
def browser_init(context):
    """
    :param context: Behave context
    """
    context.driver = webdriver.Chrome()
    context.driver = webdriver.Chrome(executable_path="C:\\Users\\donts\\Desktop\\Automation\\python-selenium-automation\\chromedriver.exe")
    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox()