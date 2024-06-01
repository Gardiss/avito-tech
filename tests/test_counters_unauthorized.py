import pytest
from pages.main_page import Main

class TestCountersUnauthorized:
    def test_counter_screenshot(self, browser):
        m = Main(browser)
        m.counter_screenshot("1")