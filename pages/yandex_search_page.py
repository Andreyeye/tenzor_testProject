from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from pages.locators import YandexSearchPageLocators


class YandexSearchPage(SeleniumBase):
    """Реализует функционал для работы на странице yandex.ru"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = 'https://yandex.ru/'

    def open(self):
        """Переход на страницу yandex.ru"""
        self.driver.get(self.url)

    def at_page(self) -> bool:
        """Проверка, что мы на yandex.ru"""
        return 'Яндекс' == self.driver.title

    def get_search_field(self) -> WebElement:
        """Возвращает поле поиска"""
        return self.is_visible(*YandexSearchPageLocators.LOCATOR_SEARCH_FIELD)

    def enter_in_search(self, search_field: WebElement, search_text: str):
        """Ввод в поле поиска"""
        search_field.send_keys(search_text)

    def get_suggest(self) -> WebElement:
        """Возвращает таблицу с подсказками"""
        return self.is_visible(*YandexSearchPageLocators.LOCATOR_SUGGEST_FIELD)

    def search(self, search_field: WebElement):
        """Осуществляет поиск (Ввод клавиши Enter)"""
        search_field.send_keys(Keys.ENTER)

    def get_images_link(self):
        """Возвращает ссылку "Картинки" """
        return self.is_visible(*YandexSearchPageLocators.LOCATOR_IMAGES_LINK)

    def go_to_images(self, image_link: WebElement):
        """Переход на Яндекс Картинки"""
        image_link.click()
        current_handle = self.driver.current_window_handle
        handless = self.driver.window_handles
        for handle in handless:
            if handle != current_handle:
                self.driver.switch_to.window(handle)

