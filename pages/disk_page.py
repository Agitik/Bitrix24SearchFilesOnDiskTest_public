# -*- coding: utf-8 -*-
from .base_page import BasePage
from .locators import DiskPageLocators


class DiskPage(BasePage):
    def should_be_files_and_folders(self):
        """
        Проверяет наличие вообще любых файлов на странице диска.
        (Тест на отсутсвие PHP ошибки на странице.)
        """
        assert self.is_element_present(*DiskPageLocators.FILE) or self.is_element_present(*DiskPageLocators.FOLDER), \
            "Отсутствуют фалйы и папки на диске. Предположительно диск не прогрузился."

    def get_all_folders(self):
        return self.browser.find_elements(*DiskPageLocators.FOLDER)

    def get_all_files(self):
        return self.browser.find_elements(*DiskPageLocators.FILE)
