from playwright.sync_api import Page
from data.environment import host
from playwright.sync_api import expect
from pages.base import Base


class Assertions(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def check_url(self, uri, msg):
        expect(self.page).to_have_url(f"{host.get_base_url()}{uri}", timeout=10000), msg


