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
        """Check if price filter is selected valid products.

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
        prices = self.category_page.get_prices()
        while True:
            for price in prices:
                assert PRICE_FROM <= price <= PRICE_TO
            try:
                self.category_page.click_next_page_link()
            except Exception:
                break

    @pytest.mark.parametrize(
        'language, year, _',
        get_test_data_dictreader('years_filter.csv'))
    def test_year_in_title(self, language, year, _) -> None:
        """Check if a specific year presents in product title.

        Steps:
            1. Choose any year "from"
            2. Choose the same year "to"
            3. Click on the search button

        Expected result:
            1. Selected year presents in all titles
        """
        import time
        self.category_page.switch_proper_language(language)
        self.category_page.year_to_dropdown.choose_dropdown_option(year)
        self.category_page.year_from_dropdown.choose_dropdown_option(year)
        self.category_page.click_search_link()

        def assert_year_in_titles():
            titles = self.category_page.get_titles()
            for title in titles:
                assert year in title
            self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")

        assert_year_in_titles()

        while not self.category_page.if_disabled_navigation_link("next"):
            self.category_page.click_next_page_link()
            assert_year_in_titles()
