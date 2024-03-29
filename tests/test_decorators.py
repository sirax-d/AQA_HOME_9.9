import allure
from allure_commons.types import Severity
from selene import by, be, browser
from selene.support.shared.jquery_style import s


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Krichanov")
@allure.feature("Задачи")
@allure.story("Поиск по ISSUES в github")
def test_decorator_steps():
    open_main_page()
    search_repository("sirax-d/AQA_HOME_9.9")
    go_to_repository("sirax-d/AQA_HOME_9.9")
    go_to_issues()
    should_see_issue_with_number("Hello allure world!")


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Ищем репозиторий {repo}")
def search_repository(repo):
    s(".header-search-button").click()
    s("#query-builder-test").send_keys(repo).press_enter()


@allure.step("Переходим в репозиторий {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Переходим в раздел Issues")
def go_to_issues():
    s("#issues-tab").click()


@allure.step("Проверяем наличие Issue")
def should_see_issue_with_number(number):
    s(by.partial_text(number)).should(be.visible)
