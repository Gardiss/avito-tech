from playwright.sync_api import Page, TimeoutError, Response, expect
from data.environment import host

class Base:
    def __init__(self, page: Page):
        self.page = page

    def open(self, uri) -> Response | None:
        return self.page.goto(f"{host.get_base_url()}{uri}", wait_until='domcontentloaded')

    def click(self, locator: str) -> None:  # клик, при необходимости сам делает скролл к нужному элементу
        self.page.click(locator)

    def input(self, locator: str, data: str) -> None:  # ввод в поле
        self.page.locator(locator).fill(data)

    def get_text(self, locator: str,
                 index: int) -> str:  # достаем текст, если локатор один, то в аргумент прокидываем значение 0
        return self.page.locator(locator).nth(index).text_content()

    def screen_element(self, locator: str, testcase: str) -> None:
        self.page.locator(locator).screenshot(path="output/screenshot_"+testcase+".png")

    def screen_page(self, testcase: str) -> None:
        self.page.screenshot(path="output/screenshot_"+testcase+".png")

    def wait_s(self, timeout=12000) -> None:
        self.page.wait_for_timeout(timeout)

    def wait_for_element(self, locator, timeout=12000) -> None:  # ожидание какого то элемента если нужно
        self.page.wait_for_selector(locator, timeout=timeout)

    def wait_for_all_elements(self, locator, timeout=5000):  # ожидание всех элементов
        elements = self.page.query_selector_all(locator)

        for element in elements:
            self.page.wait_for_selector(locator, timeout=timeout)

        return elements

    def current_url(self) -> str:  # возвращает урл
        return self.page.url

    def close_tab(self, number):  # закрываем таб и возвращаемся на предыщущий, number-номер таба который хотим закрыть
        all_tabs = self.page.context.pages
        all_tabs[number].close()

    def switch_to_previous_tab(self,
                               number):  # number - номер вкладки на которую хотим свичнуться, сначала используем этот метод, потом закрываем вкладки
        all_tabs = self.page.context.pages  # Получаем список всех вкладок в контексте браузера
        new_tab = all_tabs[number]  # Получаем вкладку по указанному индексу
        return new_tab

    def refresh(self) -> Response | None:  # рефреш страницы
        return self.page.reload(wait_until='domcontentloaded')
