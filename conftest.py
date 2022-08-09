# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser(request):
    """
    Данная фикстура создает браузер для проведения атвотеста в нем.
    :param request: Запрос
    :return: Браузер для дальнейшей работы.
    """
    browser = webdriver.Edge(executable_path="msedgedriver.exe")
    browser.implicitly_wait(1)
    yield browser
    print("\nТест окончен. Выключаю браузер.")
    browser.quit()