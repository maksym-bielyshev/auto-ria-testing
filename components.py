from selenium.webdriver import Remote
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement


class DropdownComponent:
    """Drop-down menu to choose option and check which option is chosen."""

    def __init__(self, driver: Remote, dropdown_locator: tuple,
                 parent_element: WebElement = None) -> None:
        """Initialize drop-down.

        :param driver: Remote
        :param dropdown_locator: tuple
        :return: None
        """
        self._driver = driver
        self.dropdown_locator = dropdown_locator
        self.parent_element = parent_element

    def _find_dropdown(self):
        """Find input field by parent element or driver.

        :return: None
        """
        WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable(self.dropdown_locator))
        if self.parent_element:
            self.checkbox_container = Select(
                self.parent_element.find_element(*self.dropdown_locator))
        else:
            self.checkbox_container = Select(
                self._driver.find_element(*self.dropdown_locator))

    def choose_dropdown_option(self, data: str) -> None:
        """Choose some option.

        :param data: str
        :return: None
        """
        self._find_dropdown()
        self.checkbox_container.select_by_visible_text(data)
        import time
        time.sleep(3)
