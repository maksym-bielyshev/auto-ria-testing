from tests.base_test import BaseTest
from pages.review_page import ReviewPage
from pages.category_page import CategoryPage


class TestHomePage(BaseTest):
    """Class for the 'Review' page of 'AUTO.RIA'"""

    def setup(self) -> None:
        """Setup for the each test.
        :return: None
        """
        self.driver.get("https://auto.ria.com/uk/reviews/")
        self.review_page = ReviewPage(self.driver)
        self.category_page = CategoryPage(self.driver)

    def test_prices_analysis(self):
        SCORE = "5.0"
        prices = []
        for card in self.review_page.product_cards:
            if self.review_page.get_score(card) == SCORE:
                self.review_page.click_product_photo(card)
                self.driver.close()
                self.review_page = ReviewPage(self.driver)
                self.review_page.click_offers()
                self.category_page = CategoryPage(self.driver)
                for card in self.category_page.product_card:
                    prices.append(self.review_page.get_price(card))

                    while not self.category_page.is_disabled_navigation_link(
                            "next"):
                        self.scroll_to_end()
                        self.category_page.click_next_page_link()

                        for card in self.review_page.product_cards:
                            prices.append(self.review_page.get_price(card))

        print(f'Min price: {min(prices)}')
        print(f'Max price: {max(prices)}')
        print(f'Price fluctuation: {(sum(prices)/len(prices)-min(prices))/10}'
              f'{(sum(prices)/len(prices)-max(prices))/10}')
