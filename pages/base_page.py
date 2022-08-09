# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.edge.webdriver import WebDriver


class BasePage:
    """
    Базовый класс для всех страниц.
    """

    def __init__(self, browser: WebDriver, url, timeout=10):
        """
        Конструктор класса базовой страницы.
        :param browser: Selenium webdriver.
        :param url: Ссылка на страницу.
        :param timeout: Время ожидания загрузки страницы.
        """
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """
        Открытие страницы по ссылке.
        """
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        """
        Проверка на наличие элемента на странице.
        :param how: Каким образом ищем элемент (Селектор, Xpath и т.д.)
        :param what: Какой элемент мы ищем
        :return: Возвращает true или false.
        """
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
