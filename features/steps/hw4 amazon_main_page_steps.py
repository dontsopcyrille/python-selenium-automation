from selenium.webdriver.common.by import By
from behave import given, when, then


Best_Sellers = driver.find_element(By.ID, "zg_banner_text")
HEADER_LINKS = (By.CSS_SELECTOR, '._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq')



@given('Open amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')
@when('Search for {product}')
def search_product(context, product):
    element = context.driver.find_element(By.ID, 'twotabsearchtextbox')
    element.clear()
    element.send_keys(product)
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@then('Verify  Amazon Best Sellers page is present')
def verify_Best_Sellers_present(context):
    context.driver.find_element(*Best_Sellers)


@then('Verify that header has {expected_link_count} links')
def verify_link_count(context, expected_link_count):
    expected_link_count = int(expected_link_count)

    links = context.driver.find_elements(*HEADER_LINKS)

    assert len(links) == expected_link_count, \
        f'Expected {expected_link_count} links, but got {len(links)}'