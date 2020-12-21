from selenium.webdriver import Remote


class BasePage:
    """Base page class."""

    def __init__(self, driver: Remote):
        """Initialize main class.

        :param driver: Remote.
        """
        self._driver = driver

    def switch_to_ukrainian(self):
        if self._driver.current_url != "https://auto.ria.com/uk/":
            self._driver.get("https://auto.ria.com/uk/")
