class YandexSearchPageLocators:
    """Локаторы для страницы yandex.ru"""

    # Поле поиска
    LOCATOR_SEARCH_FIELD = 'css', '#text', 'Search Field'
    # Таблица с подсказками
    LOCATOR_SUGGEST_FIELD = 'css', 'div[class*=mini-suggest__popup]', 'Suggest Field'
    # Ссылка на Яндекс Картинки
    LOCATOR_IMAGES_LINK = 'css', 'a[data-id=images]', 'Ссылка "Картинки"'

class YandexSearchResultPageLocators:
    """Локаторы для страницы результатов поиска Яндекс"""

    # Ссылки из результатов поиска
    LOCATOR_SEARCH_RESULT_LINKS = 'css', 'a[class*=Link_theme_outer]', 'Search Results'

class YandexImagesPageLocators:
    """Локаторы для страницы Яндекс Картинки"""

    # 1-ая категория картинок
    LOCATOR_FIRST_IMG_CAT = 'css', 'div[class=\'PopularRequestList-Item PopularRequestList-Item_pos_0\']', 'First Images Category'
    # Поле поиска
    LOCATOR_SEARCH_FIELD = 'css', 'input[name=text]', 'Search Field'
    # 1-ая картинка
    LOCATOR_FIRST_IMG = 'css', 'div[class*=serp-item_pos_0]', 'First Image'
    # Открытая картинка
    LOCATOR_OPENED_IMG = 'css', 'img[class=MMImage-Preview]', 'Opened Image'
    # Кнопка "следующая картинка"
    LOCATOR_BTN_NEXT_IMG = 'css', 'div[class*=ButtonNext]', 'Button Next Image'
    # Кнопка "предыдущая картинка"
    LOCATOR_BTN_PREV_IMG = 'css', 'div[class*=ButtonPrev]', 'Button Prev Image'
