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
        """Check if price filter is selected valid products.

        Steps:
            1. Open "Category" page.
            2. Fill the fields "Price From" and "Price To"
            3. Check if all prices in a valid range

        Expected result: all prices in a valid range
        """
        self.category_page.fill_price_from_field("10000")
        self.category_page.fill_price_to_field("40000")
        self.category_page.click_search_link()
        cards = self.category_page.product_cards
        prices_str = []
        for card in cards:
            price = card.find_element_by_css_selector(
                ".bold.green.size22").text
            price_split = price.split(' ')
            price_join = ''.join(price_split)
            prices_str.append(price_join)
        prices_int = []
        for price in prices_str:
            prices_int.append(int(price))
        for price in prices_int:
            assert 99999 > price < 40001
