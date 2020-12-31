from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators import LocatorsReviewPage
from components import DropdownComponent
from selenium.webdriver.common.action_chains import ActionChains
from locators import LocatorsCategoryPage

class ReviewPage(BasePage):
    """Class for the review page of 'AUTO.RIA'"""

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def product_cards(self):
        return self._driver.find_elements(
            *LocatorsReviewPage.PRODUCT_CARD)

    @property
    def offers(self):
        return self._driver.find_element(*LocatorsReviewPage.PRODUCT_OFFERS)

    def get_score(self, card):
        return card.find_element(*LocatorsReviewPage.PRODUCT_SCORE).text

    def click_product_photo(self, card):
        ActionChains(self._driver).move_to_element(card.find_element(
            *LocatorsReviewPage.PRODUCT_PHOTO)).click().perform()

    def get_price(self, card):
        price = card.find_element(*LocatorsReviewPage.PRODUCT_PRICE).text
        return int(''.join(price.split(' ')))

    def click_offers(self):
        ActionChains(self._driver).move_to_element(
            self.offers).click().perform()
