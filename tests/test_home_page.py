from tests.base_test import BaseTest
from pages.home_page import HomePage
import pytest
from tests.conftest import get_test_data, get_test_data_dictreader
from pages.base_page import BasePage
from locators import LocatorsHomeFilter


class TestHomePage(BaseTest):
    """Class for the 'Home' page of 'AUTO.RIA'"""

    def setup(self) -> None:
        """Setup for the each test.

        :return: None
        """
        self.driver.get("https://auto.ria.com/uk/")
        self.home_page = HomePage(self.driver)

    @pytest.mark.parametrize(
        'language, category, substring',
        get_test_data_dictreader('category_dropdown.csv'))
    def test_categories_dropdown_transition(
            self, language, category, substring) -> None:
        """Check all the options in the "Categories" dropdown.
        Steps:
            1. Click on the "Categories" dropdown
            2. Select an option
            3. Click on the "Пошук" button
        Expected result:
            1. Link in the address bar is changed to the address of the
               corresponding category.
        """
        BasePage(self.driver).switch_proper_language(language)
        self.home_page.category_dropdown.choose_dropdown_option(category)
        self.home_page.click_search_button()
        assert substring in self.driver.current_url

    @pytest.mark.parametrize(
        'language, category, substring',
        get_test_data('category_dropdown_without_naming.csv'))
    def test_categories_dropdown_transition_without_naming(
            self, language, category, substring) -> None:
        """Check options in the "Categories" dropdown, which have no
        specific naming for categories in the address.

        Steps:
            1. Click on the "Categories" dropdown
            2. Select an option
            3. Click on the "Пошук" button
        Expected result:
            1. Link in the address bar is changed to the address of the
               corresponding category.
        """
        BasePage(self.driver).switch_proper_language(language)
        self.home_page.category_dropdown.choose_dropdown_option(category)
        self.home_page.click_search_button()
        assert substring in self.driver.current_url

    @pytest.mark.parametrize(
        'language, expected_categories',
        get_test_data('category_dropdown_list.csv'))
    def test_categories_dropdown_options_list_ua(self, language,
                                                 expected_categories) -> None:
        """Check if "Categories" dropdown list is equal to expected list
        in Ukrainian.

        Steps:
            1. Change language to a proper language
            2. Click on the "Categories" dropdown
            3. Check if an option in the expected list.

        Expected result: all options are in the expected list.
        """
        BasePage(self.driver).switch_proper_language(language)
        categories_dropdown = self.driver.find_element(*LocatorsHomeFilter.
                                                       CATEGORY_DROPDOWN)
        options = [x for x in
                   categories_dropdown.find_elements_by_tag_name("option")]
        for element in options:
            assert element.text in expected_categories
