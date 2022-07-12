import pytest
from pages.yandex_search_page import YandexSearchPage
from pages.yandex_search_result_page import YandexSearchResultPage


@pytest.mark.usefixtures('setup')
class TestYandexSearch:

    def test_yandex_search(self):
        self.yandex_search_page = YandexSearchPage(self.driver)
        self.yandex_search_result_page = YandexSearchResultPage(self.driver)
        self.search_text = 'Тензор'

        self.yandex_search_page.open()
        assert self.yandex_search_page.at_page()
        search_field = self.yandex_search_page.get_search_field()
        assert search_field, 'Проверка наличия поля поиска'
        self.yandex_search_page.enter_in_search(search_field, self.search_text)
        assert self.yandex_search_page.get_suggest(), 'Проверка наличия таблицы с подсказками'
        self.yandex_search_page.search(search_field)

        assert self.yandex_search_result_page.at_page(self.search_text)
        actual_first_link = self.yandex_search_result_page.get_first_link_text()
        assert 'tensor.ru' in actual_first_link, 'Проверка первая ссылка ведет на tensor.ru'
