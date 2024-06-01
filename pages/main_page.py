from pages.base import Base
from data.constants import Constants
from Locators.auth import Auth
from Locators.counters import Counter
from data.assertions import Assertions
from playwright.sync_api import Page

class Main(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.assertion = Assertions(page)

    def user_login(self):
        self.open("")
        self.click(Auth.Auth_button)
        self.wait_s(1000)
        self.page = self.switch_to_previous_tab(1)
        self.wait_for_element(Auth.LOGIN_BTN)
        self.wait_for_element(Auth.LOGIN_BTN)
        self.input(Auth.USERNAME_INPUT, Constants.login)
        self.input(Auth.PASSWORD_INPUT, Constants.password)
        self.click(Auth.LOGIN_BTN)
        self.wait_for_element(Auth.MESSAGE_BUTTON,100000)
        self.assertion.check_url("", "Wrong URL")

    def counter_screenshot(self, testcase: str):
        self.open("")
        self.page.wait_for_load_state()
        self.wait_s(1000)
        self.screen_element(Counter.first_counter, testcase+".1")
        self.screen_element(Counter.second_counter, testcase+".2")
        self.screen_element(Counter.third_counter, testcase+".3")
        self.screen_page(testcase+".0")
