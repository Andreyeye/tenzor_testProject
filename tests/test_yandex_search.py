import pytest
from pages.yandex_search_page import YandexSearchPage
from pages.yandex_search_result_page import YandexSearchResultPage


@pytest.mark.usefixtures('setup')
class TestYandexSearch:

    def test_yandex_search(self):
        self.yandex_search_page = YandexSearchPage(self.driver)
        self.yandex_search_result_page = YandexSearchResultPage(self.driver)
        self.search_text = 'Тензор'

        # Заходим на yandex.ru
        self.yandex_search_page.open()
        # Проверка, что мы на yandex.ru
        assert self.yandex_search_page.at_page(), 'Проверка, что мы на yandex.ru'
        # Получаем поле поиска
        search_field = self.yandex_search_page.get_search_field()
        # Проверка наличия поля поиска
        assert search_field, 'Проверка наличия поля поиска'
        # Вводим в поиск "Тензор"
        self.yandex_search_page.enter_in_search(search_field, self.search_text)
        # Проверка наличия таблицы с подсказками
        assert self.yandex_search_page.get_suggest(), 'Проверка наличия таблицы с подсказками'
        # Нажимаем поиск (Enter)
        self.yandex_search_page.search(search_field)

        # Проверка, что мы на странице результатов поиска
        assert self.yandex_search_result_page.at_page(self.search_text), 'Проверка, что мы на странице результатов поиска'
        # Получаем 1-ую ссылку из результатов поиска
        actual_first_link = self.yandex_search_result_page.get_first_link_text()
        # Проверка первая ссылка ведет на tensor.ru
        assert 'tensor.ru' in actual_first_link, 'Проверка первая ссылка ведет на tensor.ru'
