from pages.base_page import BasePage
from selenium.webdriver import Remote
from locators import \
    LocatorsCategoryPage
from components import DropdownComponent


class CategoryPage(BasePage):
    """Class for the category page of 'AUTO.RIA'"""

    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.all_autos_button = driver.find_element(
            LocatorsCategoryPage.ALL_AUTOS_BUTTON)
        self.used_autos_button = driver.find_element(
            LocatorsCategoryPage.USED_AUTOS_BUTTON)
        self.new_autos_button = driver.find_element(
            LocatorsCategoryPage.NEW_AUTOS_BUTTON)
        self.autos_for_delivery_button = driver.find_element(
            LocatorsCategoryPage.AUTOS_FOR_DELIVERY_BUTTON)
        self.verified_vin_checkbox = driver.find_element(
            LocatorsCategoryPage.VERIFIED_VIN_CHECKBOX)
        self.plate_number_checkbox = driver.find_element(
            LocatorsCategoryPage.PLATE_NUMBER_CHECKBOX)
        self.sedan_checkbox = driver.find_element(
            LocatorsCategoryPage.SEDAN_CHECKBOX)
        self.crossover_checkbox = driver.find_element(
            LocatorsCategoryPage.CROSSOVER_CHECKBOX)
        self.minivan_checkbox = driver.find_element(
            LocatorsCategoryPage.MINIVAN_CHECKBOX)
        self.hatchback_checkbox = driver.find_element(
            LocatorsCategoryPage.HATCHBACK_CHECKBOX)
        self.universal_checkbox = driver.find_element(
            LocatorsCategoryPage.UNIVERSAL_CHECKBOX)
        self.coupe_checkbox = driver.find_element(
            LocatorsCategoryPage.COUPE_CHECKBOX)
        self.passenger_van_checkbox = driver.find_element(
            LocatorsCategoryPage.PASSENGER_VAN_CHECKBOX)
        self.convertible_checkbox = driver.find_element(
            LocatorsCategoryPage.CONVERTIBLE_CHECKBOX)
        self.pickup_checkbox = driver.find_element(
            LocatorsCategoryPage.PICKUP_CHECKBOX)
        self.liftback_checkbox = driver.find_element(
            LocatorsCategoryPage.LIFTBACK_CHECKBOX)
        self.limousine_checkbox = driver.find_element(
            LocatorsCategoryPage.LIMOUSINE_CHECKBOX)
        self.other_checkbox = driver.find_element(
            LocatorsCategoryPage.OTHER_CHECKBOX)
        self.roadster_checkbox = driver.find_element(
            LocatorsCategoryPage.ROADSTER_CHECKBOX)
        self.show_all_bodies_link = driver.find_element(
            LocatorsCategoryPage.SHOW_ALL_BODIES_LINK)
        self.show_less_bodies_link = driver.find_element(
            LocatorsCategoryPage.SHOW_LESS_BODIES_LINK)
        self.model_field = driver.find_element(
            LocatorsCategoryPage.MODEL_FIELD)
        self.another_model_link = driver.find_element(
            LocatorsCategoryPage.ANOTHER_MODEL_LINK)
        self.exclude_brand_link = driver.find_element(
            LocatorsCategoryPage.EXCLUDE_BRAND_LINK)
        self.exclude_brand_field = driver.find_element(
            LocatorsCategoryPage.EXCLUDE_BRAND_FIELD)
        self.price_from_field = driver.find_element(
            LocatorsCategoryPage.PRICE_FROM_FIELD)
        self.price_to_field = driver.find_element(
            LocatorsCategoryPage.PRICE_TO_FIELD)
        self.bargain_checkbox = driver.find_element(
            LocatorsCategoryPage.BARGAIN_CHECKBOX)
        self.region_link = driver.find_element(
            LocatorsCategoryPage.REGION_LINK)
        self.city_field = driver.find_element(
            LocatorsCategoryPage.CITY_FIELD)
        self.miles_from_field = driver.find_element(
            LocatorsCategoryPage.MILES_FROM_FIELD)
        self.miles_to_field = driver.find_element(
            LocatorsCategoryPage.MILES_TO_FIELD)
        self.automaton_checkbox = driver.find_element(
            LocatorsCategoryPage.AUTOMATON_CHECKBOX)
        self.tiptronic_checkbox = driver.find_element(
            LocatorsCategoryPage.TIPTRONIC_CHECKBOX)
        self.robot_checkbox = driver.find_element(
            LocatorsCategoryPage.ROBOT_CHECKBOX)
        self.variator_checkbox = driver.find_element(
            LocatorsCategoryPage.VARIATOR_CHECKBOX)
        self.show_all_gearboxes_link = driver.find_element(
            LocatorsCategoryPage.SHOW_ALL_GEARBOXES_LINK)
        self.show_less_gearboxes_link = driver.find_element(
            LocatorsCategoryPage.SHOW_LESS_GEARBOXES_LINK)
        self.petrol_checkbox = driver.find_element(
            LocatorsCategoryPage.PETROL_CHECKBOX)
        self.diesel_checkbox = driver.find_element(
            LocatorsCategoryPage.DIESEL_CHECKBOX)
        self.gas_checkbox = driver.find_element(
            LocatorsCategoryPage.GAS_CHECKBOX)
        self.gas_petrol_checkbox = driver.find_element(
            LocatorsCategoryPage.GAS_PETROL_CHECKBOX)
        self.hybrid_checkbox = driver.find_element(
            LocatorsCategoryPage.HYBRID_CHECKBOX)
        self.show_all_fuel_link = driver.find_element(
            LocatorsCategoryPage.SHOW_ALL_FUEL_LINK)
        self.show_less_fuel_link = driver.find_element(
            LocatorsCategoryPage.SHOW_LESS_FUEL_LINK)
        self.electro_checkbox = driver.find_element(
            LocatorsCategoryPage.ELECTRO_CHECKBOX)
        self.other_fuel_checkbox = driver.find_element(
            LocatorsCategoryPage.OTHER_FUEL_CHECKBOX)
        self.methane_gas_checkbox = driver.find_element(
            LocatorsCategoryPage.METHANE_GAS_CHECKBOX)
        self.propane_butane_gas_checkbox = driver.find_element(
            LocatorsCategoryPage.PROPANE_BUTANE_GAS_CHECKBOX)
        self.all_wheel_checkbox = driver.find_element(
            LocatorsCategoryPage.ALL_WHEEL_CHECKBOX)
        self.front_wheel_chekbox = driver.find_element(
            LocatorsCategoryPage.FRONT_WHEEL_CHEKBOX)
        self.back_wheel_checkbox = driver.find_element(
            LocatorsCategoryPage.BACK_WHEEL_CHECKBOX)
        self.engine_capacity_from_field = driver.find_element(
            LocatorsCategoryPage.ENGINE_CAPACITY_FROM_FIELD)
        self.engine_capacity_to_field = driver.find_element(
            LocatorsCategoryPage.ENGINE_CAPACITY_TO_FIELD)
        self.customs_clearance_checkbox = driver.find_element(
            LocatorsCategoryPage.CUSTOMS_CLEARANCE_CHECKBOX)
        self.non_customs_clearance_checkbox = driver.find_element(
            LocatorsCategoryPage.NON_CUSTOMS_CLEARANCE_CHECKBOX)
        self.auto_in_ukraine_checkbox = driver.find_element(
            LocatorsCategoryPage.AUTO_IN_UKRAINE_CHECKBOX)
        self.auto_not_in_ukraine_checkbox = driver.find_element(
            LocatorsCategoryPage.AUTO_NOT_IN_UKRAINE_CHECKBOX)
        self.auto_not_in_ukraine_checkbox = driver.find_element(
            LocatorsCategoryPage.AUTO_NOT_IN_UKRAINE_CHECKBOX)
        self.fixed_lacquer_select = driver.find_element(
            LocatorsCategoryPage.FIXED_LACQUER_SELECT)
        self.not_fixed_select = driver.find_element(
            LocatorsCategoryPage.NOT_FIXED_SELECT)
        self.not_damaged_select = driver.find_element(
            LocatorsCategoryPage.NOT_DAMAGED_SELECT)
        self.fixed_select = driver.find_element(
            LocatorsCategoryPage.FIXED_SELECT)
        self.not_fixed_damaged_select = driver.find_element(
            LocatorsCategoryPage.NOT_FIXED_DAMAGED_SELECT)
        self.unsuitable_select = driver.find_element(
            LocatorsCategoryPage.UNSUITABLE_SELECT)
        self.reset_filters_link = driver.find_element(
            LocatorsCategoryPage.RESET_FILTERS_LINK)
        self.advanced_search_link = driver.find_element(
            LocatorsCategoryPage.ADVANCED_SEARCH_LINK)
        self.search_link = driver.find_element(
            LocatorsCategoryPage.SEARCH_LINK)
        self.car_category_dropdown = \
            DropdownComponent(driver,
                              LocatorsCategoryPage.CAR_CATEGORY_DROPDOWN)
        self.damage_dropdown = \
            DropdownComponent(driver,
                              LocatorsCategoryPage.DAMAGE_DROPDOWN)
        self.not_on_the_move_dropdown = \
            DropdownComponent(driver,
                              LocatorsCategoryPage.NOT_ON_THE_MOVE_DROPDOWN)
        self.sort_dropdown = \
            DropdownComponent(driver,
                              LocatorsCategoryPage.SORT_DROPDOWN)
        self.period_dropdown = \
            DropdownComponent(driver,
                              LocatorsCategoryPage.PERIOD_DROPDOWN)
        self.brand_dropdown = \
            DropdownComponent(driver,
                              LocatorsCategoryPage.BRAND_DROPDOWN)
        self.year_from_dropdown = \
            DropdownComponent(driver,
                              LocatorsCategoryPage.YEAR_FROM_DROPDOWN)
        self.year_to_dropdown = \
            DropdownComponent(driver,
                              LocatorsCategoryPage.YEAR_TO_DROPDOWN)
        self.currency_dropdown = \
            DropdownComponent(driver,
                              LocatorsCategoryPage.CURRENCY_DROPDOWN)

    def click_all_autos_button(self):
        self.all_autos_button.click()

    def click_used_autos_button(self):
        self.used_autos_button.click()

    def click_new_autos_button(self):
        self.used_autos_button.click()

    def click_autos_for_delivery_button(self):
        self.autos_for_delivery_button.click()

    def click_verified_vin_checkbox(self):
        self.verified_vin_checkbox.click()

    def click_plate_number_checkbox(self):
        self.plate_number_checkbox.click()

    def click_sedan_checkbox(self):
        self.sedan_checkbox.click()

    def click_crossover_checkbox(self):
        self.crossover_checkbox.click()

    def click_minivan_checkbox(self):
        self.minivan_checkbox.click()

    def click_hatchback_checkbox(self):
        self.hatchback_checkbox.click()

    def click_universal_checkbox(self):
        self.universal_checkbox.click()

    def click_coupe_checkbox(self):
        self.coupe_checkbox.click()

    def click_passenger_van_checkbox(self):
        self.passenger_van_checkbox.click()

    def click_convertible_checkbox(self):
        self.convertible_checkbox.click()

    def click_pickup_checkbox(self):
        self.pickup_checkbox.click()

    def click_liftback_checkbox(self):
        self.liftback_checkbox.click()

    def click_limousine_checkbox(self):
        self.limousine_checkbox.click()

    def click_other_checkbox(self):
        self.other_checkbox.click()

    def click_roadster_checkbox(self):
        self.roadster_checkbox.click()

    def click_show_all_bodies_link(self):
        self.show_all_bodies_link.click()

    def click_show_less_bodies_link(self):
        self.show_less_bodies_link.click()

    def fill_model_field(self, data):
        self.model_field.send_keys(data)

    def click_another_model_link(self):
        self.another_model_link.click()

    def click_exclude_brand_link(self):
        self.exclude_brand_link.click()

    def fill_exclude_brand_field(self, data):
        self.exclude_brand_field.send_keys(data)

    def fill_price_from_field(self, data):
        self.price_from_field.send_keys(data)

    def fill_price_to_field(self, data):
        self.price_to_field.send_keys(data)

    def click_bargain_checkbox(self):
        self.bargain_checkbox.click()

    def click_region_link(self):
        self.region_link.click()

    def fill_city_field(self, data):
        self.city_field.send_keys(data)

    def fill_miles_from_field(self, data):
        self.miles_from_field.send_keys(data)

    def fill_miles_to_field(self, data):
        self.miles_to_field.send_keys(data)

    def click_automaton_checkbox(self):
        self.automaton_checkbox.click()

    def click_tiptronic_checkbox(self):
        self.tiptronic_checkbox.click()

    def click_robot_checkbox(self):
        self.robot_checkbox.click()

    def click_variator_checkbox(self):
        self.variator_checkbox.click()

    def click_show_all_gearboxes_link(self):
        self.show_all_gearboxes_link.click()

    def click_show_less_gearboxes_link(self):
        self.show_less_gearboxes_link.click()

    def click_petrol_checkbox(self):
        self.petrol_checkbox.click()

    def click_diesel_checkbox(self):
        self.diesel_checkbox.click()

    def click_gas_checkbox(self):
        self.gas_checkbox.click()

    def click_gas_petrol_checkbox(self):
        self.gas_petrol_checkbox.click()

    def click_hybrid_checkbox(self):
        self.hybrid_checkbox.click()

    def click_show_all_fuel_link(self):
        self.show_all_fuel_link.click()

    def click_show_less_fuel_link(self):
        self.show_less_fuel_link.click()

    def click_electro_checkbox(self):
        self.electro_checkbox.click()

    def click_other_fuel_checkbox(self):
        self.other_fuel_checkbox.click()

    def click_methane_gas_checkbox(self):
        self.methane_gas_checkbox.click()

    def click_propane_butane_gas_checkbox(self):
        self.propane_butane_gas_checkbox.click()

    def click_all_wheel_checkbox(self):
        self.all_wheel_checkbox.click()

    def click_front_wheel_chekbox(self):
        self.front_wheel_chekbox.click()

    def click_back_wheel_checkbox(self):
        self.back_wheel_checkbox.click()

    def click_engine_capacity_from_field(self):
        self.engine_capacity_from_field.click()

    def click_engine_capacity_to_field(self):
        self.engine_capacity_to_field.click()

    def click_customs_clearance_checkbox(self):
        self.customs_clearance_checkbox.click()

    def click_non_customs_clearance_checkbox(self):
        self.non_customs_clearance_checkbox.click()

    def click_auto_in_ukraine_checkbox(self):
        self.auto_in_ukraine_checkbox.click()

    def click_auto_not_in_ukraine_checkbox(self):
        self.auto_not_in_ukraine_checkbox.click()

    def click_fixed_lacquer_select(self):
        self.fixed_lacquer_select.click()

    def select_not_fixed(self):
        self.not_fixed_select.click()

    def select_not_damaged(self):
        self.not_damaged_select.click()

    def select_fixed(self):
        self.fixed_select.click()

    def select_not_fixed_damaged(self):
        self.not_fixed_damaged_select.click()

    def select_unsuitable(self):
        self.unsuitable_select.click()

    def click_reset_filters_link(self):
        self.reset_filters_link.click()

    def click_advanced_search_link(self):
        self.advanced_search_link.click()

    def click_search_link(self):
        self.search_link.click()
