from pages.base_page import BasePage
from selenium.webdriver import Remote
from locators import LocatorsProductPage


class ProductPage(BasePage):
    """Class for the product page of 'AUTO.RIA'"""

    def __init__(self, driver: Remote):
        super().__init__(driver)

    @property
    def seller_name_text(self):
        return self._driver.find_element(
            LocatorsProductPage.SELLER_NAME_TEXT)

    @property
    def show_phone_link(self):
        return self._driver.find_element(
            LocatorsProductPage.SHOW_PHONE_LINK)

    @property
    def seller_phone_text(self):
        return self._driver.find_element(
            LocatorsProductPage.SELLER_PHONE_TEXT)

    @property
    def auto_title(self):
        return self._driver.find_element(
            LocatorsProductPage.AUTO_TITLE)

    @property
    def mile_age_text(self):
        return self._driver.find_element(
            LocatorsProductPage.MILE_AGE_TEXT)

    @property
    def engine_text(self):
        return self._driver.find_element(
            LocatorsProductPage.ENGINE_TEXT)

    @property
    def gearbox_text(self):
        return self._driver.find_element(
            LocatorsProductPage.GEARBOX_TEXT)

    @property
    def wheel_text(self):
        return self._driver.find_element(
            LocatorsProductPage.WHEEL_TEXT)

    @property
    def color_text(self):
        return self._driver.find_element(
            LocatorsProductPage.COLOR_TEXT)

    @property
    def full_description_text(self):
        return self._driver.find_element(
            LocatorsProductPage.FULL_DESCRIPTION_TEXT)

    @property
    def lacquer_text(self):
        return self._driver.find_element(
            LocatorsProductPage.LACQUER_TEXT)

    @property
    def technical_condition_text(self):
        return self._driver.find_element(
            LocatorsProductPage.TECHNICAL_CONDITION_TEXT)

    @property
    def condition_text(self):
        return self._driver.find_element(
            LocatorsProductPage.CONDITION_TEXT)

    @property
    def safety_text(self):
        return self._driver.find_element(
            LocatorsProductPage.SAFETY_TEXT)

    @property
    def comfort_text(self):
        return self._driver.find_element(
            LocatorsProductPage.COMFORT_TEXT)

    @property
    def media_text(self):
        return self._driver.find_element(
            LocatorsProductPage.MEDIA_TEXT)

    @property
    def other_text(self):
        return self._driver.find_element(
            LocatorsProductPage.OTHER_TEXT)

    def get_phone_number(self):
        return self.seller_phone_text
