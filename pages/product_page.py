from pages.base_page import BasePage
from selenium.webdriver import Remote
from locators import \
    LocatorsProductPage


class ProductPage(BasePage):
    """Class for the product page of 'AUTO.RIA'"""

    def __init__(self, driver: Remote):
        super().__init__(driver)

        self.seller_name_text = driver.find_element(
            LocatorsProductPage.SELLER_NAME_TEXT)
        self.show_phone_link = driver.find_element(
            LocatorsProductPage.SHOW_PHONE_LINK)
        self.seller_phone_text = driver.find_element(
            LocatorsProductPage.SELLER_PHONE_TEXT)
        self.auto_title = driver.find_element(
            LocatorsProductPage.AUTO_TITLE)
        self.mile_age_text = driver.find_element(
            LocatorsProductPage.MILE_AGE_TEXT)
        self.engine_text = driver.find_element(
            LocatorsProductPage.ENGINE_TEXT)
        self.gearbox_text = driver.find_element(
            LocatorsProductPage.GEARBOX_TEXT)
        self.wheel_text = driver.find_element(
            LocatorsProductPage.WHEEL_TEXT)
        self.color_text = driver.find_element(
            LocatorsProductPage.COLOR_TEXT)
        self.full_description_text = driver.find_element(
            LocatorsProductPage.FULL_DESCRIPTION_TEXT)
        self.lacquer_text = driver.find_element(
            LocatorsProductPage.LACQUER_TEXT)
        self.technical_condition_text = driver.find_element(
            LocatorsProductPage.TECHNICAL_CONDITION_TEXT)
        self.condition_text = driver.find_element(
            LocatorsProductPage.CONDITION_TEXT)
        self.safety_text = driver.find_element(
            LocatorsProductPage.SAFETY_TEXT)
        self.comfort_text = driver.find_element(
            LocatorsProductPage.COMFORT_TEXT)
        self.media_text = driver.find_element(
            LocatorsProductPage.MEDIA_TEXT)
        self.other_text = driver.find_element(
            LocatorsProductPage.OTHER_TEXT)

    def get_phone_number(self):
        self.show_phone_link.click()
        return self.seller_phone_text
