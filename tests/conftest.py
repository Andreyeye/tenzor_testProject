import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def get_chrome_options():
    """Настройка опций для вебдрайвера Selenium"""
    options = chrome_options()
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    """Настройка вебдрайвера Selenium"""
    options = get_chrome_options
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    """Инициализация вебдрайвера Selenium и передача тестовым функциям"""
    driver = get_webdriver
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()