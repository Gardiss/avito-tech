import pytest
from pages.main_page import Main


@pytest.mark.usefixtures('user_login')
class TestCountersAuthorized:
    def test_counter_screenshot(self, browser):
        m = Main(browser)
        m.counter_screenshot("2")

