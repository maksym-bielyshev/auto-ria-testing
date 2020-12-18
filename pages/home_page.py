from selenium.webdriver import Remote
from pages.base_page import BasePage
from locators import LocatorsHomeFilter
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from components import DropdownComponent


class HomePage(BasePage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

        self.all_autos = driver.find_element(
            *LocatorsHomeFilter.ALL_AUTOS
        )
        self.used_autos = driver.find_element(
            *LocatorsHomeFilter.USED_AUTOS
        )
        self.new_autos = driver.find_element(
            *LocatorsHomeFilter.NEW_AUTOS
        )
        self.autos_for_delivery = driver.find_element(
            *LocatorsHomeFilter.AUTOS_FOR_DELIVERY
        )
        self.checked_vin = driver.find_element(
            *LocatorsHomeFilter.CHECKED_VIN
        )
        self.category_dropdown = DropdownComponent(
            driver,
            LocatorsHomeFilter.CATEGORY_DROPDOWN
        )
        self.brand_dropdown = driver.find_element(
            *LocatorsHomeFilter.BRAND_DROPDOWN
        )
        self.model_dropdown = driver.find_element(
            *LocatorsHomeFilter.MODEL_DROPDOWN
        )
        self.region_dropdown = driver.find_element(
            *LocatorsHomeFilter.REGION_DROPDOWN
        )
        self.year_from_dropdown = DropdownComponent(
            driver,
            LocatorsHomeFilter.YEAR_FROM_DROPDOWN
        )
        self.year_to_dropdown = DropdownComponent(
            driver,
            LocatorsHomeFilter.YEAR_TO_DROPDOWN
        )
        self.price_from = driver.find_element(
            *LocatorsHomeFilter.PRICE_FROM
        )
        self.price_to = driver.find_element(
            *LocatorsHomeFilter.PRICE_TO
        )
        self.search_button = driver.find_element(
            *LocatorsHomeFilter.SEARCH_BUTTON
        )

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

    def choose_brand(self, input):
        self.brand_dropdown.send_keys(input)

    def choose_model(self, input):
        self.model_dropdown.send_keys(input)

    def choose_region(self, input):
        self.region_dropdown.send_keys(input)

    def set_price_from(self, input):
        self.price_from.send_keys(input)

    def set_price_to(self, input):
        self.price_to.send_keys(input)

    def click_search_button(self):
        self.search_button.click()
