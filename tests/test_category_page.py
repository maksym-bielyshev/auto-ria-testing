import pytest

from tests.conftest import get_test_data_dictreader


class TestCategoryPage:
    """Class for the 'Home' page of 'AUTO.RIA'"""

    def test_price_filter(self, open_category_page) -> None:
        """Check that price filter is selected valid products.

        Steps:
            1. Open "Category" page.
            2. Fill the fields "Price From" and "Price To"
            3. Check if all prices in a valid range

        Expected result: all prices in a valid range
        """
        category_page = open_category_page
        PRICE_FROM = 10010
        PRICE_TO = 10100
        category_page.fill_price_from_field(PRICE_FROM)
        category_page.fill_price_to_field(PRICE_TO)
        category_page.click_search_link()

        break_loop = True
        while break_loop:
            for card in category_page.product_card:
                assert PRICE_FROM <= category_page.get_price(
                    card) <= PRICE_TO
            category_page.scroll_to_end()

            if not category_page.is_disabled_navigation_link("next"):
                category_page.click_next_page_link()
            else:
                break_loop = False

    @pytest.mark.parametrize(
        'language, year, _',
        get_test_data_dictreader('years_filter.csv'))
    def test_year_in_title(self, open_category_page, language, year, _):
        """Check that a specific year presents in product title.

        Steps:
            1. Choose any year "from"
            2. Choose the same year "to"
            3. Click on the search button

        Expected result:
            1. Selected year presents in all titles
        """
        category_page = open_category_page
        category_page.switch_proper_language(language)
        category_page.year_to_dropdown.choose_dropdown_option(year)
        category_page.year_from_dropdown.choose_dropdown_option(year)
        category_page.click_search_link()

        break_loop = True
        while break_loop:
            for card in category_page.product_card:
                assert year in category_page.get_card_title(card)
            category_page.scroll_to_end()
            if not category_page.is_disabled_navigation_link("next"):
                category_page.click_next_page_link()
            else:
                break_loop = False

    def test_previous_link_disabled(self, open_category_page):
        """Check that "Previous" link is disabled on the first "Category" page
        (https://auto.ria.com/uk/legkovie/?page=1).

        Steps:
            1. Move to the first page

        Expected result:
            The "Previous" link is disabled.
        """
        category_page = open_category_page
        assert category_page.is_disabled_navigation_link("previous")

    def test_previous_link(self, open_category_page):
        """Check that "Previous" link is working.

        Steps:
            1. Open the second page
            2. Move to the first page

        Expected result:
            "/?page=1" is in address.
        """
        category_page = open_category_page
        category_page.get("https://auto.ria.com/uk/legkovie/?page=2")
        category_page.scroll_to_end()
        category_page.click_previous_page_link()
        assert "/?page=1" in category_page.current_url

    def test_next_link(self, open_category_page):
        """Check that "Next" link is working.

        Steps:
            1. Click on the "Next" button

        Expected result:
            "/?page=2" is in address.
        """
        category_page = open_category_page
        category_page.scroll_to_end()
        category_page.click_next_page_link()
        assert "/?page=2" in category_page.current_url

    def test_next_link_disabled(self, open_category_page):
        """Check that "Next" link is disabled on the last page

        Steps:
            1. Move to the last page

        Expected result:
            The "Next" link is disabled
        """
        category_page = open_category_page
        category_page.scroll_to_end()
        category_page.click_last_middle_pagination_link()
        assert category_page.is_disabled_navigation_link("next")

    def test_middle_pagination_link(self, open_category_page):
        """Check the middle pagination for working

        Steps:
            1. Click on the "5" link in the middle pagination links

        Expected result:
            "/?page=5" is in address.
        """
        category_page = open_category_page
        category_page.scroll_to_end()
        category_page.click_fourth_middle_pagination_link()
        assert "/?page=5" in category_page.current_url

    def test_first_pagination_link(self, open_category_page):
        """Check that first pagination link is working

        Steps:
            1. Click on the "5" link in the middle pagination links
            2. Click on the "1" link in the middle pagination links

        Expected result:
             "/?page=1" is in address.
        """
        category_page = open_category_page
        category_page.scroll_to_end()
        category_page.click_fourth_middle_pagination_link()
        category_page.click_first_page_link()
        assert "/?page=1" in category_page.current_url
