from selenium import webdriver
from locators import LocatorsBasePage


class BasePage:
    """Base page class."""

    def __init__(self, driver):
        """Initialize main class.

        :param driver: Remote.
        """
        self._driver = driver

    def switch_proper_language(self, language):
        if language == "ua" and "/uk/" not in self._driver.current_url:
            self._driver.find_element(*LocatorsBasePage.UKRAINIAN_LINK).click()
        elif language == "ru" and "/ru" not in self._driver.current_url:
            self._driver.find_element(*LocatorsBasePage.RUSSIAN_LINK).click()
