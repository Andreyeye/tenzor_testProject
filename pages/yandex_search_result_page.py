from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from typing import List
from selenium.webdriver.common.keys import Keys


class YandexSearchResultPage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def at_page(self, search_text: str):
        title = self.driver.title
        return f'{search_text} — Яндекс:' in title

    def get_first_link_text(self) -> str:
        links = self.are_visible('css', 'a[class*=Link_theme_outer]', 'Search Results')
        links[0].click()
        return links[0].get_attribute('href')






