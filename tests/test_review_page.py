from pages.category_page import CategoryPage
from pages.home_page import HomePage


class TestHomePage:
    """Class for the 'Review' page of 'AUTO.RIA'"""

    def test_prices_analysis(self, open_review_page):
        review_page = open_review_page
        SCORE = "5.0"
        prices_lists = []
        cards = []

        for card in review_page.product_cards:
            if review_page.get_score(card) == SCORE:
                cards.append(card)

        splitted_title = review_page.get_title(cards[0]).split()
        brand = splitted_title[0]
        model = splitted_title[-3]
        year = splitted_title[-1]

        review_page._driver.get("https://auto.ria.com/uk/")

        home_page = HomePage(review_page._driver)

        home_page.year_to_dropdown.choose_dropdown_option(year)
        home_page.year_from_dropdown.choose_dropdown_option(year)

        home_page.choose_brand(brand)
        home_page.choose_model(model)
        home_page.click_search_button()

        category_page = CategoryPage(home_page._driver)

        break_loop = True
        while break_loop:
            prices_lists.append(category_page.get_prices())
            category_page.scroll_to_end()
            if not category_page.is_disabled_navigation_link("next"):
                category_page.click_next_page_link()
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
