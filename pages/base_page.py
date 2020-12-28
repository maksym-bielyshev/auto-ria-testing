from locators import LocatorsBasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Base page class."""

    def __init__(self, driver):
        """Initialize main class.

        :param driver: Remote.
        """
        self._driver = driver

    def switch_proper_language(self, language):
        if language == "ua" and "/uk/" not in self._driver.current_url:
            ukrainian_link = WebDriverWait(
                self._driver, 10).until(EC.visibility_of_element_located(
                LocatorsBasePage.UKRAINIAN_LINK))
            ukrainian_link.click()
        elif language == "ru" and "/uk/" in self._driver.current_url:
            russian_link = WebDriverWait(
                self._driver, 10).until(EC.visibility_of_element_located(
                LocatorsBasePage.RUSSIAN_LINK))
            russian_link.click()
