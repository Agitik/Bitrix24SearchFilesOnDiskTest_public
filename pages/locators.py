from selenium.webdriver.common.by import By


class BasePageLocators:
    SEARCH_LABEL = (By.CSS_SELECTOR, ".header-search-input")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".header-search-icon")


class DiskPageLocators:
    FOLDER = (By.CSS_SELECTOR, ".js-disk-grid-folder")
    FILE = (By.CSS_SELECTOR, ".bx-disk-folder-title[data-actions]")


class SearchResultLocators:
    DISK_PART_OF_RESULT = (By.CSS_SELECTOR, "#nav-item-disk > a")
    FIRST_SEARCH_RESULT = (By.CSS_SELECTOR, ".search-name")


