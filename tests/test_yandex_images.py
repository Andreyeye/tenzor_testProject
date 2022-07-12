import pytest
from pages.yandex_images_page import YandexImagesPage
from pages.yandex_search_page import YandexSearchPage


@pytest.mark.usefixtures('setup')
class TestYandexImages:

    def test_yandex_images(self):
        self.yandex_search_page = YandexSearchPage(self.driver)
        self.yandex_images_page = YandexImagesPage(self.driver)

        # Заходим на yandex.ru
        self.yandex_search_page.open()
        # Получаем ссылку на "Яндекс Картинки"
        images_link = self.yandex_search_page.get_images_link()
        # Проверяем что такая ссылка есть
        assert images_link, 'Проверка наличия ссылки "Картинки"'
        # Переходим на Яндекс Картинки
        self.yandex_search_page.go_to_images(images_link)
        # Проверяем, что перешли на https://yandex.ru/images/
        assert self.yandex_images_page.at_page()
        # Открываем 1-ую категорию и сохраняем ее название
        first_cat_name = self.yandex_images_page.open_first_category()
        # Получаем текст с поля поиска
        search_field_text = self.yandex_images_page.get_search_field_text()
        # Проверка название категории в поле поиска
        assert first_cat_name == search_field_text, 'Проверка название категории в поле поиска'
        # Открываем 1-ую картинку
        self.yandex_images_page.open_first_image()
        # Проверка, что картинка открылась и запоминаем ее
        first_image_src = self.yandex_images_page.get_image_src()
        assert first_image_src, 'Проверка, что картинка открылась'
        # Переходим на следующую картинку
        self.yandex_images_page.go_next_image()
        # Проверка, что картинка открылась и запоминаем ее
        second_image_src = self.yandex_images_page.get_image_src()
        assert second_image_src, 'Проверка, что картинка открылась'
        # Проверка, что картинка сменилась
        assert first_image_src != second_image_src
        # Переходим на предыдущую картинку
        self.yandex_images_page.go_back_image()
        # Проверка, что картинка открылась и запоминаем ее
        image_src = self.yandex_images_page.get_image_src()
        assert image_src, 'Проверка, что картинка открылась'
        # Проверка, что эта ранее открытая нами картинка
        assert first_image_src == image_src, 'Проверка, что эта ранее открытая нами картинка'





