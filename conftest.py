import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome", help="Выберите браузер:Chrome or Firefox")
    parser.addoption('--language', action='store', default="en", help="Язык не входит в список рекомендованных языков сайта")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option ('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print ("\nЗапуск браузера Хром...")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print ("\nЗапуск браузера Файрфокс")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name не соответствует ни Хрому ни файрфоксу")
    yield browser
    print("\nБраузер закрывается")
    browser.quit()

