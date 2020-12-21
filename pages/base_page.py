from selenium.webdriver import Remote


class BasePage:
    """Base page class."""

    def __init__(self, driver: Remote):
        """Initialize main class.

        :param driver: Remote.
        """
        self._driver = driver

    def switch_to_ukrainian(self):
        if "auto.ria.com/uk" not in self._driver.current_url:
            self._driver.find_element_by_xpath(
                "//a[@class='selectLang ml-r']").click()
