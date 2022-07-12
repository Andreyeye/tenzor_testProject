from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from typing import List
from selenium.webdriver.common.keys import Keys


class YandexSearchPage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.driver.get('https://yandex.ru/')

    def at_page(self):
        return 'Яндекс' == self.driver.title

    def get_search_field(self) -> WebElement:
        return self.is_visible('css', '#text', 'Search Field')

    def enter_in_search(self, search_field: WebElement, search_text: str):
        search_field.send_keys(search_text)

    def get_suggest(self) -> WebElement:
        return self.is_visible('css', 'div[class*=mini-suggest__popup]', 'Suggest Field')

    def search(self, search_field: WebElement):
        search_field.send_keys(Keys.ENTER)

    def get_images_link(self):
        return self.is_visible('css', 'a[data-id=images]', 'Ссылка "Картинки"')

    def go_to_images(self, image_link: WebElement):
        image_link.click()
        current_handle = self.driver.current_window_handle
        handless = self.driver.window_handles
        for handle in handless:
            if handle != current_handle:
                self.driver.switch_to.window(handle)

