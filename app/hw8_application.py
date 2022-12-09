from pages.bestsellers_page import BestsellersPage
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.signin_page import SignInPage


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.bestsellers_page = BestsellersPage(self.driver)
        self.main_page = MainPage(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.sign_in_page = SignInPage(self.driver)