from pages.base_page import BasePage
from selenium.webdriver import Remote
from locators import LocatorsCategoryPage
from components import DropdownComponent


class CategoryPage(BasePage):
    """Class for the category page of 'AUTO.RIA'"""

    def __init__(self, driver: Remote):
        super().__init__(driver)

    @property
    def all_autos_button(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.ALL_AUTOS_BUTTON)

    @property
    def used_autos_button(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.USED_AUTOS_BUTTON)

    @property
    def new_autos_button(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.NEW_AUTOS_BUTTON)

    @property
    def autos_for_delivery_button(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.AUTOS_FOR_DELIVERY_BUTTON)

    @property
    def verified_vin_checkbox(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.VERIFIED_VIN_CHECKBOX)

    @property
    def plate_number_checkbox(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.PLATE_NUMBER_CHECKBOX)

    @property
    def sedan_checkbox(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.SEDAN_CHECKBOX)

    @property
    def crossover_checkbox(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.CROSSOVER_CHECKBOX)

    @property
    def minivan_checkbox(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.MINIVAN_CHECKBOX)

    @property
    def hatchback_checkbox(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.HATCHBACK_CHECKBOX)

    @property
    def universal_checkbox(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.UNIVERSAL_CHECKBOX)

    @property
    def coupe_checkbox(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.COUPE_CHECKBOX)

    @property
    def passenger_van_checkbox(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.PASSENGER_VAN_CHECKBOX)

    @property
    def convertible_checkbox(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.CONVERTIBLE_CHECKBOX)

    @property
    def pickup_checkbox(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.PICKUP_CHECKBOX)

    @property
    def liftback_checkbox(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.LIFTBACK_CHECKBOX)

    @property
    def limousine_checkbox(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.LIMOUSINE_CHECKBOX)

    @property
    def other_checkbox(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.OTHER_CHECKBOX)

    @property
    def roadster_checkbox(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.ROADSTER_CHECKBOX)

    @property
    def show_all_bodies_link(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.SHOW_ALL_BODIES_LINK)

    @property
    def show_less_bodies_link(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.SHOW_LESS_BODIES_LINK)

    @property
    def model_field(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.MODEL_FIELD)

    @property
    def another_model_link(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.ANOTHER_MODEL_LINK)

    @property
    def exclude_brand_link(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.EXCLUDE_BRAND_LINK)

    @property
    def exclude_brand_field(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.EXCLUDE_BRAND_FIELD)

    @property
    def price_from_field(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.PRICE_FROM_FIELD)

    @property
    def price_to_field(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.PRICE_TO_FIELD)

    @property
    def bargain_checkbox(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.BARGAIN_CHECKBOX)

    @property
    def region_link(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.REGION_LINK)

    @property
    def city_field(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.CITY_FIELD)

    @property
    def miles_from_field(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.MILES_FROM_FIELD)

    @property
    def miles_to_field(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.MILES_TO_FIELD)

    @property
    def automaton_checkbox(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.AUTOMATON_CHECKBOX)

    @property
    def tiptronic_checkbox(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.TIPTRONIC_CHECKBOX)

    @property
    def robot_checkbox(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.ROBOT_CHECKBOX)

    @property
    def variator_checkbox(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.VARIATOR_CHECKBOX)

    @property
    def show_all_gearboxes_link(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.SHOW_ALL_GEARBOXES_LINK)

    @property
    def show_less_gearboxes_link(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.SHOW_LESS_GEARBOXES_LINK)

    @property
    def petrol_checkbox(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.PETROL_CHECKBOX)

    @property
    def diesel_checkbox(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.DIESEL_CHECKBOX)

    @property
    def gas_checkbox(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.GAS_CHECKBOX)

    @property
    def gas_petrol_checkbox(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.GAS_PETROL_CHECKBOX)

    @property
    def hybrid_checkbox(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.HYBRID_CHECKBOX)

    @property
    def show_all_fuel_link(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.SHOW_ALL_FUEL_LINK)

    @property
    def show_less_fuel_link(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.SHOW_LESS_FUEL_LINK)

    @property
    def electro_checkbox(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.ELECTRO_CHECKBOX)

    @property
    def other_fuel_checkbox(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.OTHER_FUEL_CHECKBOX)

    @property
    def methane_gas_checkbox(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.METHANE_GAS_CHECKBOX)

    @property
    def propane_butane_gas_checkbox(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.PROPANE_BUTANE_GAS_CHECKBOX)

    @property
    def all_wheel_checkbox(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.ALL_WHEEL_CHECKBOX)

    @property
    def front_wheel_chekbox(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.FRONT_WHEEL_CHEKBOX)

    @property
    def back_wheel_checkbox(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.BACK_WHEEL_CHECKBOX)

    @property
    def engine_capacity_from_field(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.ENGINE_CAPACITY_FROM_FIELD)

    @property
    def engine_capacity_to_field(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.ENGINE_CAPACITY_TO_FIELD)

    @property
    def customs_clearance_checkbox(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.CUSTOMS_CLEARANCE_CHECKBOX)

    @property
    def non_customs_clearance_checkbox(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.NON_CUSTOMS_CLEARANCE_CHECKBOX)

    @property
    def auto_in_ukraine_checkbox(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.AUTO_IN_UKRAINE_CHECKBOX)

    @property
    def auto_not_in_ukraine_checkbox(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.AUTO_NOT_IN_UKRAINE_CHECKBOX)

    @property
    def fixed_lacquer_select(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.FIXED_LACQUER_SELECT)

    @property
    def not_fixed_select(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.NOT_FIXED_SELECT)

    @property
    def not_damaged_select(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.NOT_DAMAGED_SELECT)

    @property
    def fixed_select(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.FIXED_SELECT)

    @property
    def not_fixed_damaged_select(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.NOT_FIXED_DAMAGED_SELECT)

    @property
    def unsuitable_select(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.UNSUITABLE_SELECT)

    @property
    def reset_filters_link(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.RESET_FILTERS_LINK)

    @property
    def advanced_search_link(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.ADVANCED_SEARCH_LINK)

    @property
    def search_link(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.SEARCH_LINK)

    @property
    def product_cards(self):
        return self._driver.find_elements(
            *LocatorsCategoryPage.PRODUCT_CARD_OBJECT)

    @property
    def previous_page_link(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.PRODUCT_CARD_OBJECT)

    @property
    def next_page_link(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.NEXT_PAGE_LINK)

    @property
    def first_page_link(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.FIRST_PAGE_LINK)

    @property
    def last_page_link(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.LAST_PAGE_LINK)

    @property
    def first_middle_pagination_link(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.FIRST_MIDDLE_PAGINATION_LINK)

    @property
    def second_middle_pagination_link(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.SECOND_MIDDLE_PAGINATION_LINK)

    @property
    def third_middle_pagination_link(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.THIRD_MIDDLE_PAGINATION_LINK)

    @property
    def fourth_middle_pagination_link(self):
        return self._driver.find_element(
            *LocatorsCategoryPage.FOURTH_MIDDLE_PAGINATION_LINK)

    @property
    def car_category_dropdown(self):
        return DropdownComponent(self._driver,
                                 *LocatorsCategoryPage.CAR_CATEGORY_DROPDOWN)

    @property
    def damage_dropdown(self):
        return DropdownComponent(self._driver,
                                 *LocatorsCategoryPage.DAMAGE_DROPDOWN)

    @property
    def not_on_the_move_dropdown(self):
        return DropdownComponent(self._driver,
                                 *LocatorsCategoryPage.NOT_ON_THE_MOVE_DROPDOWN)

    @property
    def sort_dropdown(self):
        return DropdownComponent(self._driver,
                                 *LocatorsCategoryPage.SORT_DROPDOWN)

    @property
    def period_dropdown(self):
        return DropdownComponent(self._driver,
                                 *LocatorsCategoryPage.PERIOD_DROPDOWN)

    @property
    def brand_dropdown(self):
        return DropdownComponent(self._driver,
                                 *LocatorsCategoryPage.BRAND_DROPDOWN)

    @property
    def year_from_dropdown(self):
        return DropdownComponent(self._driver,
                                 *LocatorsCategoryPage.YEAR_FROM_DROPDOWN)

    @property
    def year_to_dropdown(self):
        return DropdownComponent(self._driver,
                                 *LocatorsCategoryPage.YEAR_TO_DROPDOWN)

    @property
    def currency_dropdown(self):
        return DropdownComponent(self._driver,
                                 *LocatorsCategoryPage.CURRENCY_DROPDOWN)

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

    def click_previous_page_link(self):
        self.previous_page_link.click()

    def click_next_page_link(self):
        self.next_page_link.click()

    def click_first_page_link(self):
        self.first_page_link.click()

    def click_last_page_link(self):
        self.last_page_link.click()

    def click_first_middle_pagination_link(self):
        self.first_middle_pagination_link.click()

    def click_second_middle_pagination_link(self):
        self.second_middle_pagination_link.click()

    def click_third_middle_pagination_link(self):
        self.third_middle_pagination_link.click()

    def click_fourth_middle_pagination_link(self):
        self.fourth_middle_pagination_link.click()
