import allure
from allure_commons.types import Severity


def test_dynamic_labels():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Задачи")
    allure.dynamic.story("Авторизованный пользователь может создать задачу")
    allure.dynamic.link("https://github.com", name="Testing")
    pass

@allure.tag("critical")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "eroshenkoam")
@allure.feature("Задачи")
@allure.story("Авторизованный пользователь может создать задачу")
@allure.link("https://github.com", name="Testing")
def test_decorator_labels():
    pass