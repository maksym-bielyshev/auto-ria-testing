from tests.base_test import BaseTest
from pages.review_page import ReviewPage
from pages.category_page import CategoryPage
from pages.home_page import HomePage
from pages.base_page import BasePage


class TestHomePage(BaseTest):
    """Class for the 'Review' page of 'AUTO.RIA'"""

    def setup(self) -> None:
        """Setup for the each test.
        :return: None
        """
        self.driver.get("https://auto.ria.com/uk/reviews/")
        self.review_page = ReviewPage(self.driver)

    def test_prices_analysis(self):
        SCORE = "5.0"
        prices_lists = []
        cards = []

        for card in self.review_page.product_cards:
            if self.review_page.get_score(card) == SCORE:
                cards.append(card)

        splitted_title = self.review_page.get_title(cards[0]).split()
        brand = splitted_title[0]
        model = splitted_title[-2]
        year = splitted_title[-1]

        self.driver.get("https://auto.ria.com/uk/")

        self.home_page = HomePage(self.driver)

        self.home_page.year_to_dropdown.choose_dropdown_option(year)
        self.home_page.year_from_dropdown.choose_dropdown_option(year)

        self.home_page.choose_brand(brand)
        self.home_page.choose_model(model)
        self.home_page.click_search_button()

        break_loop = True
        while break_loop:
            self.category_page = CategoryPage(self.driver)
            prices_lists.append(self.category_page.get_prices())
            BasePage(self.driver).scroll_to_end()
            if not self.category_page.is_disabled_navigation_link("next"):
                self.category_page.click_next_page_link()
            else:
                break_loop = False

        prices = []
        for lists in prices_lists:
            for item in lists:
                prices.append(item)

        min_price = min(prices)
        max_price = max(prices)
        average_price = sum(prices)/len(prices)
        price_fluctuation = (average_price-min(prices))/10, \
                            (average_price-max(prices))/10

        print(f'Min price: {min_price} $. '
              f'Max price: {max_price} $. '
              f'Average price: {average_price} $. '
              f'Price fluctuation: {price_fluctuation}', prices_lists)
