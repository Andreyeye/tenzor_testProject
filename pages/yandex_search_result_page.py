import time
from base.seleniumbase import SeleniumBase
from locators import YandexSearchResultPageLocators


class YandexSearchResultPage(SeleniumBase):
    """Реализует функционал для работы на странице результатов поиска Яндекс"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def at_page(self, search_text: str):
        """Проверка, что мы на странице результатов поиска"""
        time.sleep(1)
        return self.title_contains(f'{search_text} — Яндекс:')

    def get_first_link_text(self) -> str:
        """Возвращает первую ссылку из результатов поиска"""
        links = self.are_visible(YandexSearchResultPageLocators.LOCATOR_SEARCH_RESULT_LINKS)
        links[0].click()
        return links[0].get_attribute('href')






