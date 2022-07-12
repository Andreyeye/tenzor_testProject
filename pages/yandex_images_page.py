import time

from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from typing import List
from selenium.webdriver.common.keys import Keys


class YandexImagesPage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def at_page(self):
        return 'https://yandex.ru/images/' in self.driver.current_url

    def open_first_category(self) -> str:
        first_cat_el = self.is_visible('css', 'div[class=\'PopularRequestList-Item PopularRequestList-Item_pos_0\']', 'First Category')
        first_cat_name = first_cat_el.get_attribute('data-grid-text')
        first_cat_el.click()
        return first_cat_name

    def get_search_field_text(self) -> str:
        search_field = self.is_visible('css', 'input[name=text]', 'Search Field')
        return search_field.get_attribute('value')

    def open_first_image(self):
        self.is_visible('css', 'div[class*=serp-item_pos_0]', 'First Image').click()

    def get_image_src(self):
        time.sleep(0.5)
        return self.is_visible('css', 'img[class=MMImage-Preview]', 'Image').get_attribute('src')

    def go_next_image(self):
        self.is_present('css', 'div[class*=ButtonNext]', 'Button Next Image').click()

    def go_back_image(self):
        self.is_present('css', 'div[class*=ButtonPrev]', 'Button Next Image').click()