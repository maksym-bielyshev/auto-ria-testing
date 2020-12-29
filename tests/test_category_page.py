from pages.category_page import CategoryPage
from tests.base_test import BaseTest


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
        prices = self.category_page.get_prices()
        while True:
            for price in prices:
                assert PRICE_FROM <= price <= PRICE_TO
            try:
                self.category_page.click_next_page_link()
            except Exception:
                break
