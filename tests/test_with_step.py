import allure
from selene import by, be, browser
from selene.support.shared.jquery_style import s


def test_decorator_steps():
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")


    with allure.step("Ищем репозиторий {repo}"):
        s(".header-search-button").click()
        s("#query-builder-test").send_keys("sirax-d/AQA_HOME_9.9").press_enter()

    with allure.step("Переходим в репозиторий"):
        s(by.link_text("sirax-d/AQA_HOME_9.9")).click()


    with allure.step("Переходим в раздел Issues"):
        s("#issues-tab").click()


    with allure.step("Проверяем наличие Issue с номером {number}"):
        s(by.partial_text("Hello allure world!")).should(be.visible)
