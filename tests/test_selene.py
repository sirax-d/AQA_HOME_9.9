from selene import by, be
from selene import browser
from selene.support.shared.jquery_style import s


def test_github():
    browser.open("https://github.com")
    s(".header-search-button").click()  # Выбираем область поиска
    s("#query-builder-test").send_keys("sirax-d/AQA_HOME_9.9").press_enter()  # Вводим в поиск репозиторий
    s(by.link_text("sirax-d/AQA_HOME_9.9")).click()  # Переходим в репозиторий
    s("#issues-tab").click()  # Переходим в раздел Issues
    s(by.partial_text("Hello allure world!")).should(be.visible)  # Проверяем наличие Issue
