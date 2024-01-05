import allure
from selene import by, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

def test_github():
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")

    with allure.step("Ищем репозиторий"):
        s(".header-search-button").click()
        s("#query-builder-test").send_keys("eroshenkoam/allure-example").press_enter()

    with allure.step("Переходим в репозиторий"):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Переходим в раздел Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие Issue с номером 76"):
        s(by.partial_text("#76")).should(be.visible)

def test_decorator_steps():
    open_main_page()
    search_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    go_to_issues()
    should_see_issue_with_number("#76")
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

@allure.step("Проверяем наличие Issue с номером {number}")
def should_see_issue_with_number(number):
    s(by.partial_text(number)).should(be.visible)