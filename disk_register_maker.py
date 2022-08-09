# -*- coding: utf-8 -*-
from selenium.webdriver.edge.webdriver import WebDriver

from .pages.locators import DiskPageLocators
from .pages.disk_page import DiskPage


class DiskObject:
    """
    Класс для имитации объектов Selenium.

    Мне пришлось сделать его для рекурсивности функции поиска файла на портале.
    Selenium запоминает ID'шники объектов только в рамках одной страницы.
    При переходе на другую (когда открываем новую страницу, к примеру)
    итерация ломается из-за того, что Selenium меняет поисковой кэш.

    Короче по итогу итерация делается через вот такой простой объект.
    Столько текста предназначено для более хорошего понимания Selenium.
    """
    def __init__(self, url, name, df):
        self.url = url
        self.name = name
        self.type = df


def fill_file_register(dp: DiskPage, browser: WebDriver, prev_link: str, current_link: str):
    # Тут нужны комментарии, чтобы не свихнуться.
    # Заходим в папку.
    folders = []
    dp.url = current_link
    dp.open()
    # Если в папке есть другие папки
    if dp.is_element_present(*DiskPageLocators.FOLDER):
        # Для каждой папки
        for file in dp.get_all_folders():
            try:
                folders.append(DiskObject(file.get_attribute("href"), file.text, "folder"))
            except BaseException:
                print(f"\nОшибка кодировки (скорее всего) по ссылке:\n{current_link}")
                continue
        for file in folders:
            try:
                # Если ее нет в регистре файлов и папок
                if not is_file_or_folder_in_file_register(file.name):
                    # Записываем название папки в регистр
                    add_object_to_file_register(file.name)
                    # Берем ссылку нынешней папки для возвращения назад
                    prev = browser.current_url
                    # Берем ссылку папки, которую хотим исследовать
                    curr = file.url
                    # Запускаем эту же функцию для нее :)
                    fill_file_register(dp, browser, prev, curr)
            except BaseException:
                print(f"\nОшибка кодировки (скорее всего) по ссылке:\n{current_link}")
                continue
    if dp.is_element_present(*DiskPageLocators.FILE):
        # Просто выписываем названия всех файлов и папок.
        files = []
        for file in dp.get_all_files():
            try:
                files.append(DiskObject(file.get_attribute("href"), file.text, "file"))
            except BaseException:
                print(f"\nОшибка кодировки (скорее всего) по ссылке:\n{current_link}")
                continue
        for file in files:
            try:
                if not is_file_or_folder_in_file_register(file.name):
                    add_object_to_file_register(file.name)
            except BaseException:
                print(f"\nОшибка кодировки (скорее всего) по ссылке:\n{current_link}")
                continue
    # Возвращаемся туда, где начали.
    dp.url = prev_link
    dp.open()


def add_object_to_file_register(string: str):
    """
    Добавляет строку к файлу file_and_folders.txt
    :param string: Строка
    """
    with open("file_and_folders.txt", "a+") as file:
        file.write(string + "\n")


def clear_file_register():
    """
    Очищает файл file_and_folders.txt
    """
    with open("file_and_folders.txt", "w+") as file:
        file.write("")


def is_file_or_folder_in_file_register(filename: str):
    """
    Проверяет, есть ли название файла в регистре.
    :param filename: название файла
    :return: True или False
    """
    with open('file_and_folders.txt', 'r+') as file:
        if filename in file.read():
            return True
        else:
            return False


def get_files_from_register() -> list:
    """
    Возвращает список, где каждый элемент - строка регистра.
    :return: Список, где каждый элемент - строка регистра
    """
    with open("file_and_folders.txt", "r+") as file:
        content = file.readlines()
    return [x.strip() for x in content]

