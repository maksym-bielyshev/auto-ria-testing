from selenium.webdriver import Remote
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators import LocatorsLogin


class LoginPage(BasePage):
    """Register page class."""

    def __init__(self, driver: Remote) -> None:
        """Initialize objects to work with this page.

        :param driver: Remote
        :return: None
        """
        super().__init__(driver)
        self.login_field = self._driver.find_element(
            *LocatorsLogin.LOGIN_FIELD
        )
        self.password_field = self._driver.find_element(
            *LocatorsLogin.PASSWORD_FIELD
        )

    def click_continue_button(self) -> None:
        """Click continue button to submit all data to login.

        :return: None
        """
        continue_button = self._driver.find_element(
            *LocatorsLogin.CONTINUE_BUTTON
        )
        continue_button.click()
