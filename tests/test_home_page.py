from tests.base_test import BaseTest
from pages.home_page import HomePage
import pytest
from tests.conftest import get_test_data


class TestHomePage(BaseTest):
    """Class for the 'Home' page of 'AUTO.RIA'"""

    def setup(self) -> None:
        """Setup for the each test.

        :return: None
        """
        self.driver.get("https://auto.ria.com/uk/")
        self.home_page = HomePage(self.driver)

    @pytest.mark.parametrize('category, expected_url',
                             get_test_data('category_dropdown.csv'))
    def test_categories_dropdown(self, category, expected_url) -> None:
        """Check all the options in the "Categories" dropdown.

        Steps:
            1. Click on the "Categories" dropdown
            2. Select an option
            3. Click on the "Пошук" button

        Expected result:
            1. Link in the address bar is changed to the address of the
               corresponding category.
        """
        self.home_page.category_dropdown.choose_dropdown_option(category)
        self.home_page.click_search_button()
        assert self.driver.current_url == expected_url
