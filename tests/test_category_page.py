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
        PRICE_FROM = "10010"
        PRICE_TO = "10100"
        self.category_page.fill_price_from_field(PRICE_FROM)
        self.category_page.fill_price_to_field(PRICE_TO)
        self.category_page.click_search_link()

        print(self.category_page.product_card)

        for card in self.category_page.product_card:
            assert PRICE_FROM <= self.category_page.get_price(card) <= PRICE_TO

        while not self.category_page.is_disabled_navigation_link("next"):
            self.scroll_to_end()
            self.category_page.click_next_page_link()

            for card in self.category_page.product_card:
                assert PRICE_FROM <= self.category_page.get_price(
                    card) <= PRICE_TO

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

        for card in self.category_page.product_card:
            assert year in self.category_page.get_card_title(card)

        self.scroll_to_end()

        while not self.category_page.is_disabled_navigation_link("next"):
            self.category_page.click_next_page_link()
            for card in self.category_page.product_card:
                assert year in self.category_page.get_card_title(card)
            self.scroll_to_end()
