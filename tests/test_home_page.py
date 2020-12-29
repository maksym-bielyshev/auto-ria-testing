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

    @pytest.mark.parametrize(
        'language, expected_categories, _',
        get_test_data_dictreader('category_dropdown.csv',
                                 'category_dropdown_without_naming.csv'))
    def test_categories_dropdown_options_list(self, language,
                                              expected_categories, _) -> None:
        """Check that "Categories" dropdown list is equal to expected list.

        Steps:
            1. Change language to a proper language
            2. Click on the "Categories" dropdown
            3. Check an option is in the expected list.

        Expected result: all options are in the expected list.
        """
        self.home_page.switch_proper_language(language)
        actual_categories = [c.text for c in
                             self.home_page.get_all_categories()]
        assert expected_categories in actual_categories

    @pytest.mark.parametrize('language, _, __',
                             get_test_data_dictreader('languages.csv'))
    def test_no_doubles_dropdown_categories(self, language, _, __):
        print(language)
        self.home_page.switch_proper_language(language)
        actual_categories = [c.text for c in
                             self.home_page.get_all_categories()]
        assert len(set(actual_categories)) == len(actual_categories)
