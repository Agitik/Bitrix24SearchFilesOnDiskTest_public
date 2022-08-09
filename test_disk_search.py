# -*- coding: utf-8 -*-
import pytest

from .pages.base_page import BasePage
from .disk_register_maker import fill_file_register, clear_file_register
from .conftest import browser
from .pages.locators import DiskPageLocators
from .pages.locators import BasePageLocators
from .pages.locators import SearchResultLocators
from .pages.disk_page import DiskPage


def make_test_input():
    ret = []
    with open("D:\\AutoTestPortal_new\\file_and_folders.txt") as register:
        for file in register:
            ret.append(file.strip())
    return ret


# def test_disk_is_not_empty(browser):
#     link = ""
#     page = DiskPage(browser, link)
#     page.open()
#     page.should_be_files_and_folders()


# def test_we_can_make_file_register(browser):
#     clear_file_register()
#     prev_link = ""
#     current_link = ""
#     page = DiskPage(browser, prev_link)
#     fill_file_register(page, browser, prev_link, current_link)

@pytest.mark.parametrize("file", make_test_input())
def test_file_search(browser, file):
    link = ""
    page = BasePage(browser, link)
    page.open()
    browser.find_element(*BasePageLocators.SEARCH_LABEL).click()
    browser.find_element(*BasePageLocators.SEARCH_LABEL).send_keys(file)
    browser.find_element(*BasePageLocators.SEARCH_BUTTON).click()
    browser.find_element(*SearchResultLocators.DISK_PART_OF_RESULT).click()
    result = browser.find_element(*SearchResultLocators.FIRST_SEARCH_RESULT).text
    assert result == file, f"\nФайл/папка {file} не был(а) найден(а) в качестве первого результата поиска.\nПытался найти: {file}.\nПервый результат в поиске: {result}."
