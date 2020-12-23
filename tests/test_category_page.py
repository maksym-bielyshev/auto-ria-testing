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
        self.category_page.fill_price_from_field("10000")
        self.category_page.fill_price_to_field("40000")
        self.category_page.click_search_link()
        cards = self.category_page.product_cards
        for card in cards:
            pass
        b = self.driver.find_element_by_css_selector(".bold.green.size22")
        print(b.text)
