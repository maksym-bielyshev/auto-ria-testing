from selenium.webdriver import Remote
from pages.base_page import BasePage
from locators import LocatorsHomeFilter
from components import DropdownComponent


class HomePage(BasePage):
    """Class for the home page of 'AUTO.RIA'"""

    def __init__(self, driver: Remote):
        super().__init__(driver)

    @property
    def all_autos(self):
        return self._driver.find_element(
            *LocatorsHomeFilter.ALL_AUTOS)

    @property
    def used_autos(self):
        return self._driver.find_element(
            *LocatorsHomeFilter.USED_AUTOS)

    @property
    def new_autos(self):
        return self._driver.find_element(
            LocatorsHomeFilter.NEW_AUTOS)

    @property
    def autos_for_delivery(self):
        return self._driver.find_element(
            *LocatorsHomeFilter.AUTOS_FOR_DELIVERY)

    @property
    def checked_vin(self):
        return self._driver.find_element(
            *LocatorsHomeFilter.CHECKED_VIN)

    @property
    def category_dropdown(self):
        return DropdownComponent(
            self._driver, LocatorsHomeFilter.CATEGORY_DROPDOWN)

    @property
    def brand_dropdown(self):
        return self._driver.find_element(
            *LocatorsHomeFilter.BRAND_DROPDOWN)

    @property
    def model_dropdown(self):
        return self._driver.find_element(
            *LocatorsHomeFilter.MODEL_DROPDOWN)

    @property
    def region_dropdown(self):
        return self._driver.find_element(
            *LocatorsHomeFilter.REGION_DROPDOWN)

    @property
    def year_from_dropdown(self):
        return DropdownComponent(
            self._driver, LocatorsHomeFilter.YEAR_FROM_DROPDOWN)

    @property
    def year_to_dropdown(self):
        return DropdownComponent(
            self._driver, LocatorsHomeFilter.YEAR_TO_DROPDOWN)

    @property
    def price_from(self):
        return self._driver.find_element(
            *LocatorsHomeFilter.PRICE_FROM)

    @property
    def price_to(self):
        return self._driver.find_element(
            *LocatorsHomeFilter.PRICE_TO)

    @property
    def search_button(self):
        return self._driver.find_element(*LocatorsHomeFilter.SEARCH_BUTTON)

    def click_all_autos(self):
        self.all_autos.click()

    def click_used_autos(self):
        self.used_autos.click()

    def click_new_autos(self):
        self.new_autos.click()

    def click_autos_for_delivery(self):
        self.autos_for_delivery.click()

    def click_checked_vin(self):
        self.checked_vin.click()

    def choose_brand(self, data: str):
        self.brand_dropdown.send_keys(data)

    def choose_model(self, data: str):
        self.model_dropdown.send_keys(data)

    def choose_region(self, data: str):
        self.region_dropdown.send_keys(data)

    def set_price_from(self, data: str):
        self.price_from.send_keys(data)

    def set_price_to(self, data: str):
        self.price_to.send_keys(data)

    def click_search_button(self):
        self._driver.execute_script("return document.readyState")
        import time
        time.sleep(5)
        self.search_button.click()

    def get_all_categories(self):
        categories_dropdown = self._driver.find_element(*LocatorsHomeFilter.
                                                        CATEGORY_DROPDOWN)
        categories = [x for x in
                      categories_dropdown.find_elements_by_tag_name("option")]
        return categories
