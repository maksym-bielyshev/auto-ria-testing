from selenium import webdriver


class BasePage:
    """Base page class."""

    def __init__(self, driver):
        """Initialize main class.

        :param driver: Remote.
        """
        self._driver = driver

    def switch_to_ukrainian(self):
        if "auto.ria.com/uk" not in self._driver.current_url:
            self._driver.find_element_by_xpath(
                "//a[@class='selectLang ml-r']").click()

    def switch_to_russian(self):
        if "auto.ria.com/uk" in self._driver.current_url:
            self._driver.find_element_by_xpath(
                "//a[@class='selectLang ml-l']").click()
