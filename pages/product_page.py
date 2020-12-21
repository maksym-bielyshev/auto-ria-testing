from pages.base_page import BasePage
from selenium.webdriver import Remote
from locators import \
    LocatorsProductPage


class ProductPage(BasePage):
    """Class for the product page of 'AUTO.RIA'"""

    def __init__(self, driver: Remote):
        super().__init__(driver)

        self.SELLER_NAME_TEXT = driver.find_element(
            LocatorsProductPage.SELLER_NAME_TEXT)
        self.SHOW_PHONE_LINK = driver.find_element(
            LocatorsProductPage.SHOW_PHONE_LINK)
        self.SELLER_PHONE_TEXT = driver.find_element(
            LocatorsProductPage.SELLER_PHONE_TEXT)
        self.AUTO_TITLE = driver.find_element(
            LocatorsProductPage.AUTO_TITLE)
        self.MILE_AGE_TEXT = driver.find_element(
            LocatorsProductPage.MILE_AGE_TEXT)
        self.ENGINE_TEXT = driver.find_element(
            LocatorsProductPage.ENGINE_TEXT)
        self.GEARBOX_TEXT = driver.find_element(
            LocatorsProductPage.GEARBOX_TEXT)
        self.WHEEL_TEXT = driver.find_element(
            LocatorsProductPage.WHEEL_TEXT)
        self.COLOR_TEXT = driver.find_element(
            LocatorsProductPage.COLOR_TEXT)
        self.FULL_DESCRIPTION_TEXT = driver.find_element(
            LocatorsProductPage.FULL_DESCRIPTION_TEXT)
        self.LACQUER_TEXT = driver.find_element(
            LocatorsProductPage.LACQUER_TEXT)
        self.TECHNICAL_CONDITION_TEXT = driver.find_element(
            LocatorsProductPage.TECHNICAL_CONDITION_TEXT)
        self.CONDITION_TEXT = driver.find_element(
            LocatorsProductPage.CONDITION_TEXT)
        self.SAFETY_TEXT = driver.find_element(
            LocatorsProductPage.SAFETY_TEXT)
        self.COMFORT_TEXT = driver.find_element(
            LocatorsProductPage.COMFORT_TEXT)
        self.MEDIA_TEXT = driver.find_element(
            LocatorsProductPage.MEDIA_TEXT)
        self.OTHER_TEXT = driver.find_element(
            LocatorsProductPage.OTHER_TEXT)
