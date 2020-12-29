import pytest
from tests.conftest import get_test_data_dictreader


class TestHomePage:
    """Class for the 'Home' page of 'AUTO.RIA'"""

    @pytest.mark.parametrize(
        'language, category, substring',
        get_test_data_dictreader('category_dropdown.csv'))
    def test_categories_dropdown_transition(
            self, open_home_page, language, category, substring) -> None:
        """Check the options in the "Categories" dropdown where each option has
        a specific naming for categories in the address.

        Steps:
            1. Click on the "Categories" dropdown
            2. Select an option
            3. Click on the "Пошук" button

        Expected result:
            1. Link in the address bar is changed to the address of the
               corresponding category.
        """
        home_page = open_home_page
        home_page.switch_proper_language(language)
        home_page.category_dropdown.choose_dropdown_option(category)
        home_page.click_search_button()
        assert substring in home_page._driver.current_url

    @pytest.mark.parametrize(
        'language, category, substring',
        get_test_data_dictreader('category_dropdown_without_naming.csv'))
    def test_categories_dropdown_transition_without_naming(
            self, open_home_page, language, category, substring) -> None:
        """Check the options in the "Categories" dropdown where each option has
        no specific naming for categories in the address.

        Steps:
            1. Click on the "Categories" dropdown
            2. Select an option
            3. Click on the "Пошук" button

        Expected result:
            1. Link in the address bar is changed to the address of the
               corresponding category.
        """
        home_page = open_home_page
        home_page.switch_proper_language(language)
        home_page.category_dropdown.choose_dropdown_option(category)
        home_page.click_search_button()
        assert substring in home_page._driver.current_url
