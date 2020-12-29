import pytest

from pages.category_page import CategoryPage
from tests.base_test import BaseTest
from tests.conftest import get_test_data_dictreader


class TestCategoryPage(BaseTest):
    """Class for the 'Home' page of 'AUTO.RIA'"""

    def setup(self) -> None:
        """Setup for the each test.

        :return: None
        """
        self.driver.get("https://auto.ria.com/uk/legkovie/?page=1")
        self.category_page = CategoryPage(self.driver)

    def test_price_filter(self) -> None:
        """Check that price filter is selected valid products.

        Steps:
            1. Open "Category" page.
            2. Fill the fields "Price From" and "Price To"
            3. Check if all prices in a valid range

        Expected result: all prices in a valid range
        """
        PRICE_FROM = 10010
        PRICE_TO = 10100
        self.category_page.fill_price_from_field(PRICE_FROM)
        self.category_page.fill_price_to_field(PRICE_TO)
        self.category_page.click_search_link()

        assert self.category_page.if_price_in_proper_range(PRICE_FROM,
                                                           PRICE_TO)

        while not self.category_page.is_disabled_navigation_link("next"):
            self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            self.category_page.click_next_page_link()
            assert self.category_page.if_price_in_proper_range(PRICE_FROM,
                                                               PRICE_TO)

    @pytest.mark.parametrize(
        'language, year, _',
        get_test_data_dictreader('years_filter.csv'))
    def test_year_in_title(self, language, year, _) -> None:
        """Check that a specific year presents in product title.

        Steps:
            1. Choose any year "from"
            2. Choose the same year "to"
            3. Click on the search button

        Expected result:
            1. Selected year presents in all titles
        """
        self.category_page.switch_proper_language(language)
        self.category_page.year_to_dropdown.choose_dropdown_option(year)
        self.category_page.year_from_dropdown.choose_dropdown_option(year)
        self.category_page.click_search_link()

        assert self.category_page.if_proper_year_in_titles(year)
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

        while not self.category_page.is_disabled_navigation_link("next"):
            self.category_page.click_next_page_link()
            assert self.category_page.if_proper_year_in_titles(year)

    def test_previous_link_disabled(self):
        """Check that "Previous" link is disabled on the first "Category" page
        (https://auto.ria.com/uk/legkovie/?page=1).

        Steps:
            1. Move to the first page

        Expected result:
            The "Previous" link is disabled.
        """
        assert self.category_page.is_disabled_navigation_link("previous")

    def test_previous_link(self):
        """Check that "Previous" link is working.

        Steps:
            1. Open the second page
            2. Move to the first page

        Expected result:
             "/?page=1" is in address.
        """
        self.driver.get("https://auto.ria.com/uk/legkovie/?page=2")
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        self.category_page.click_previous_page_link()
        assert "/?page=1" in self.driver.current_url

    def test_next_link(self):
        """Check that "Next" link is working.

        Steps:
            1. Click on the "Next" button

        Expected result: "/?page=2" is in address.
        """
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        self.category_page.click_next_page_link()
        assert "/?page=2" in self.driver.current_url
