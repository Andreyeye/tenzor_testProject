import time
from base.seleniumbase import SeleniumBase
from pages.locators import YandexImagesPageLocators

class YandexImagesPage(SeleniumBase):
    """Реализует функционал для работы на странице Яндекс Картинки"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def at_page(self):
        """Проверка, что мы на странице Яндекс Картинки"""
        return 'https://yandex.ru/images/' in self.driver.current_url

    def open_first_category(self) -> str:
        """Открывает 1-ую категорию картинок и возвращает название категории"""
        first_cat_el = self.is_visible(*YandexImagesPageLocators.LOCATOR_FIRST_IMG_CAT)
        first_cat_name = first_cat_el.get_attribute('data-grid-text')
        first_cat_el.click()
        return first_cat_name

    def get_search_field_text(self) -> str:
        """Возвращает текст с поля поиска"""
        search_field = self.is_visible(*YandexImagesPageLocators.LOCATOR_SEARCH_FIELD)
        return search_field.get_attribute('value')

    def open_first_image(self):
        """Открывает первую картинку"""
        self.is_visible(*YandexImagesPageLocators.LOCATOR_FIRST_IMG).click()

    def get_image_src(self):
        """Возвращает атрибут src открытой картинки"""
        time.sleep(1)
        return self.is_visible(*YandexImagesPageLocators.LOCATOR_OPENED_IMG).get_attribute('src')

    def go_next_image(self):
        """Переход на следующую картинку"""
        self.is_present(*YandexImagesPageLocators.LOCATOR_BTN_NEXT_IMG).click()

    def go_back_image(self):
        """Переход на предыдущую картинку"""
        self.is_present(*YandexImagesPageLocators.LOCATOR_BTN_PREV_IMG).click()