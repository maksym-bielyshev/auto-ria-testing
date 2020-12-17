import pytest
from tests.base_test import BaseTest
from tests.conftest import get_test_data
from pages.login_page import LoginPage


class TestRegisterPage(BaseTest):
    """Class for the 'Register' page."""

    def setup(self) -> None:
        """Setup for the test.

        :return: None
        """
        self.driver.get('https://auto.ria.com/uk/login.html')
        self.login_page = LoginPage(self.driver)


    @pytest.mark.parametrize(
        'login_field,password_field',
        get_test_data('login_page/valid_login.csv'))
    def test_registration_form(self, login_field: str, password_field: str,) -> None:
        """Check the registration form on the registration page.

        :return: None
        """

        self.login_page.login_field.send_keys(login_field)
        self.login_page.login_field.send_keys(password_field)
        self.register_page.click_continue_button()

        assert self.register_page.get_title.get_title_page('Your Account Has Been Created!')
