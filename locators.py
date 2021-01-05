from selenium.webdriver.common.by import By


class LocatorsBasePage:
    RUSSIAN_LINK = (
        By.XPATH, "//a[@class='selectLang ml-l']")
    UKRAINIAN_LINK = (
        By.XPATH, "//a[@class='selectLang ml-r']")


class LocatorsHomeFilter:
    ALL_AUTOS = (
        By.XPATH, "//input[@id='allRadioType']")
    USED_AUTOS = (
        By.XPATH, "//input[@id='buRadioType']")
    NEW_AUTOS = (
        By.XPATH, "//input[@id='naRadioType']")
    AUTOS_FOR_DELIVERY = (
        By.XPATH, "//input[@id='orderRadioType']")
    CHECKED_VIN = (
        By.XPATH, "//input[@id='verifiedVIN']")
    CATEGORY_DROPDOWN = (
        By.XPATH, "//select[@id='categories']")
    BRAND_DROPDOWN = (
        By.XPATH, "//input[@id='brandTooltipBrandAutocompleteInput-brand']")
    MODEL_DROPDOWN = (
        By.XPATH, "//input[@id='brandTooltipBrandAutocompleteInput-model']")
    REGION_DROPDOWN = (
        By.XPATH, "//input[@id='brandTooltipBrandAutocompleteInput-region']")
    YEAR_FROM_DROPDOWN = (
        By.XPATH, "//select[@id='yearFrom']")
    YEAR_TO_DROPDOWN = (
        By.XPATH, "//select[@id='yearTo']")
    PRICE_FROM = (
        By.XPATH, "//input[@id='priceFrom']")
    PRICE_TO = (
        By.XPATH, "//input[@id='priceTo']")
    SEARCH_BUTTON = (
        By.CSS_SELECTOR, "button[type='submit']")


class LocatorsProductPage:
    SELLER_NAME_TEXT = (
        By.CLASS_NAME, "seller_info_name bold")
    SHOW_PHONE_LINK = (
        By.CLASS_NAME, "size14 phone_show_link link-dotted mhide")
    SELLER_PHONE_TEXT = (
        By.XPATH, "//section[@id='userInfoBlock']//"
                  "div[contains(@class,'phones_item')]//"
                  "span['data-phone-number']")
    AUTO_TITLE = (
        By.CLASS_NAME, "auto-content_title")
    MILE_AGE_TEXT = (
        By.XPATH, "//dl[@class='unstyle']//dd[2]")
    ENGINE_TEXT = (
        By.XPATH, "//dl[@class='unstyle']//dd[3]")
    GEARBOX_TEXT = (
        By.XPATH, "//dl[@class='unstyle']//dd[5]")
    WHEEL_TEXT = (
        By.XPATH, "//dl[@class='unstyle']//dd[6]")
    COLOR_TEXT = (
        By.XPATH, "//dl[@class='unstyle']//dd[7]")
    FULL_DESCRIPTION_TEXT = (
        By.XPATH, "//dl[@class='unstyle']//dd[8]")
    LACQUER_TEXT = (
        By.XPATH, "//dl[@class='unstyle']//dd[9]")
    TECHNICAL_CONDITION_TEXT = (
        By.XPATH, "//dl[@class='unstyle']//dd[10]")
    CONDITION_TEXT = (
        By.XPATH, "//dl[@class='unstyle']//dd[11]")
    SAFETY_TEXT = (
        By.XPATH, "//dl[@class='unstyle']//dd[12]")
    COMFORT_TEXT = (
        By.XPATH, "//dl[@class='unstyle']//dd[13]")
    MEDIA_TEXT = (
        By.XPATH, "//dl[@class='unstyle']//dd[14]")
    OTHER_TEXT = (
        By.XPATH, "//dl[@class='unstyle']//dd[15]")


class LocatorsCategoryPage:
    ALL_AUTOS_BUTTON = (
        By.XPATH,
        "//label[@for='indexName_all']")
    USED_AUTOS_BUTTON = (
        By.XPATH,
        "//label[@for='indexName_bu']")
    NEW_AUTOS_BUTTON = (
        By.XPATH,
        "//label[@for='indexName_new']")
    AUTOS_FOR_DELIVERY_BUTTON = (
        By.XPATH,
        "//label[@for='indexName_order']")
    VERIFIED_VIN_CHECKBOX = (
        By.XPATH,
        "//label[@for='verifiedVIN']")
    PLATE_NUMBER_CHECKBOX = (
        By.XPATH,
        "//label[@for='plateNumber']")
    CAR_CATEGORY_DROPDOWN = (
        By.XPATH,
        "//select[@id='category']")
    SEDAN_CHECKBOX = (
        By.XPATH,
        "//label[@for='bodyBlockItem_0']")
    CROSSOVER_CHECKBOX = (
        By.XPATH,
        "//label[@for='bodyBlockItem_1']")
    MINIVAN_CHECKBOX = (
        By.XPATH,
        "//label[@for='bodyBlockItem_2']")
    HATCHBACK_CHECKBOX = (
        By.XPATH,
        "//label[@for='bodyBlockItem_3']")
    UNIVERSAL_CHECKBOX = (
        By.XPATH,
        "//label[@for='bodyBlockItem_4']")
    COUPE_CHECKBOX = (
        By.XPATH,
        "//label[@for='bodyBlockItem_5']")
    PASSENGER_VAN_CHECKBOX = (
        By.XPATH,
        "//label[@for='bodyBlockItem_6']")
    CONVERTIBLE_CHECKBOX = (
        By.XPATH,
        "//label[@for='bodyBlockItem_7']")
    PICKUP_CHECKBOX = (
        By.XPATH,
        "//label[@for='bodyBlockItem_8']")
    LIFTBACK_CHECKBOX = (
        By.XPATH,
        "//label[@for='bodyBlockItem_9']")
    LIMOUSINE_CHECKBOX = (
        By.XPATH,
        "//label[@for='bodyBlockItem_10']")
    OTHER_CHECKBOX = (
        By.XPATH,
        "//label[@for='bodyBlockItem_11']")
    ROADSTER_CHECKBOX = (
        By.XPATH,
        "//label[@for='bodyBlockItem_12']")

    SHOW_ALL_BODIES_LINK = (
        By.XPATH,
        "//div[@title='Тип кузова']//"
        "a[@class='el-selected open'][contains(text(),'Показати')]")
    SHOW_LESS_BODIES_LINK = (
        By.XPATH,
        "//div[@title='Коробка передач']//"
        "a[@class='el-selected close'][contains(text(),'Сховати')]")
    BRAND_DROPDOWN = (
        By.XPATH,
        "//label[@for='brandTooltipBrandAutocompleteInput-0']")
    MODEL_FIELD = (
        By.XPATH,
        "//label[@for='brandTooltipModelAutocompleteInput-0']")
    YEAR_FROM_DROPDOWN = (
        By.XPATH,
        "//select[@id='brandTooltipYearGte_0']")
    YEAR_TO_DROPDOWN = (
        By.XPATH,
        "//select[@id='brandTooltipYearLte_0']")
    ANOTHER_MODEL_LINK = (
        By.XPATH,
        "//div[@id='brandTooltip']//a[@id='brandTooltipAddMore']")
    EXCLUDE_BRAND_LINK = (
        By.XPATH,
        "//a[@id='brandExcludeSelect']")
    EXCLUDE_BRAND_FIELD = (
        By.XPATH,
        "//label[@for='brandTooltipBrandAutocompleteInput-1']")
    PRICE_FROM_FIELD = (
        By.XPATH,
        "//input[@name='price.USD.gte']")
    PRICE_TO_FIELD = (
        By.XPATH,
        "//input[@name='price.USD.lte']")
    CURRENCY_DROPDOWN = (
        By.XPATH,
        "//select[@name='price.currency']")
    BARGAIN_CHECKBOX = (
        By.XPATH,
        "//label[@for='priceBlockOptionsAuction']")
    REGION_LINK = (
        By.CLASS_NAME,
        "label gray")
    CITY_FIELD = (
        By.CLASS_NAME,
        "text")
    MILES_FROM_FIELD = (
        By.NAME,
        "mileage.gte")
    MILES_TO_FIELD = (
        By.XPATH,
        "//input[@name='mileage.lte']")
    MANUAL_MECHANICS_CHECKBOX = (
        By.XPATH,
        "//label[@for='gearboxBlockItem_0']")
    AUTOMATON_CHECKBOX = (
        By.XPATH,
        "//label[@for='gearboxBlockItem_1']")
    TIPTRONIC_CHECKBOX = (
        By.XPATH,
        "//label[@for='gearboxBlockItem_2']")
    ROBOT_CHECKBOX = (
        By.XPATH,
        "//label[@for='gearboxBlockItem_3']")
    VARIATOR_CHECKBOX = (
        By.XPATH,
        "//label[@for='gearboxBlockItem_4']")
    SHOW_ALL_GEARBOXES_LINK = (
        By.XPATH,
        "//div[@title='Коробка передач']//"
        "a[@class='el-selected open'][contains(text(),'Показати')]")
    SHOW_LESS_GEARBOXES_LINK = (
        By.XPATH,
        "//div[@title='Коробка передач']//"
        "a[@class='el-selected close'][contains(text(),'Сховати')]")
    PETROL_CHECKBOX = (
        By.XPATH,
        "//label[@for='fuelBlockItem_0']")
    DIESEL_CHECKBOX = (
        By.XPATH,
        "//label[@for='fuelBlockItem_1']")
    GAS_CHECKBOX = (
        By.XPATH,
        "//label[@for='fuelBlockItem_2']")
    GAS_PETROL_CHECKBOX = (
        By.XPATH,
        "//label[@for='fuelBlockItem_3']")
    HYBRID_CHECKBOX = (
        By.XPATH,
        "//label[@for='fuelBlockItem_4']")
    SHOW_ALL_FUEL_LINK = (
        By.XPATH,
        "//div[@title='Паливо']//"
        "a[@class='el-selected open'][contains(text(),'Показати')]")
    SHOW_LESS_FUEL_LINK = (
        By.XPATH,
        "//div[@title='Паливо']//"
        "a[@class='el-selected close'][contains(text(),'Сховати')]")
    ELECTRO_CHECKBOX = (
        By.XPATH,
        "//label[@for='fuelBlockItem_5']")
    OTHER_FUEL_CHECKBOX = (
        By.XPATH,
        "//label[@for='fuelBlockItem_6']")
    METHANE_GAS_CHECKBOX = (
        By.XPATH,
        "//label[@for='fuelBlockItem_7']")
    PROPANE_BUTANE_GAS_CHECKBOX = (
        By.XPATH,
        "//label[@for='fuelBlockItem_8']")
    ALL_WHEEL_CHECKBOX = (
        By.XPATH,
        "//label[@for='driveBlockItem_0']")
    FRONT_WHEEL_CHEKBOX = (
        By.XPATH,
        "//label[@for='driveBlockItem_1']")
    BACK_WHEEL_CHECKBOX = (
        By.XPATH,
        "//label[@for='driveBlockItem_2']")
    ENGINE_CAPACITY_FROM_FIELD = (
        By.XPATH,
        "//input[@name='engine.gte']")
    ENGINE_CAPACITY_TO_FIELD = (
        By.XPATH,
        "//input[@name='engine.lte']")
    CUSTOMS_CLEARANCE_CHECKBOX = (
        By.XPATH,
        "//label[@for='_custom1']")
    NON_CUSTOMS_CLEARANCE_CHECKBOX = (
        By.XPATH,
        "//label[@for='_custom2']")
    AUTO_IN_UKRAINE_CHECKBOX = (
        By.XPATH,
        "//label[@for='_abroad1']")
    AUTO_NOT_IN_UKRAINE_CHECKBOX = (
        By.XPATH,
        "//label[@for='_abroad2']")
    LACQUER_SELECT = (
        By.XPATH,
        "//label[@for='paintCondition-1']")
    FIXED_LACQUER_SELECT = (
        By.XPATH,
        "//label[@for='paintCondition-2']")
    NOT_FIXED_SELECT = (
        By.XPATH,
        "//label[@for='paintCondition-3']")
    NOT_DAMAGED_SELECT = (
        By.XPATH,
        "//label[@for='technicalCondition-1']")
    FIXED_SELECT = (
        By.XPATH,
        "//label[@for='technicalCondition-2']")
    NOT_FIXED_DAMAGED_SELECT = (
        By.XPATH,
        "//label[@for='technicalCondition-3']")
    UNSUITABLE_SELECT = (
        By.XPATH,
        "//label[@for='technicalCondition-4']")
    DAMAGE_DROPDOWN = (
        By.ID,
        "damageBlockSelect")
    NOT_ON_THE_MOVE_DROPDOWN = (
        By.XPATH,
        "sparesBlockSelect")
    SORT_DROPDOWN = (
        By.ID,
        "leftFilterSortSelect")
    PERIOD_DROPDOWN = (
        By.ID,
        "leftFilterPeriodSelect")
    RESET_FILTERS_LINK = (
        By.CLASS_NAME,
        "filt-reset")
    ADVANCED_SEARCH_LINK = (
        By.XPATH,
        "//a[@id='leftFilterAdvancedSearch']")
    SEARCH_LINK = (
        By.ID,
        "floatingSearchButton")

    PRODUCT_CARD_OBJECTS = (
        By.CLASS_NAME,
        "content-bar")
    PREVIOUS_PAGE_LINK = (
        By.XPATH,
        "//span[@class='page-item prev']//a")
    NEXT_PAGE_LINK = (
        By.XPATH,
        "//span[@class='page-item next text-r']//a")
    FIRST_PAGE_LINK = (
        By.XPATH,
        "//div[@id='searchPagination']//span[2]//a")
    LAST_PAGE_LINK = (
        By.XPATH,
        "//div[@id='searchPagination']//span[9]//a")
    FIRST_MIDDLE_PAGINATION_LINK = (
        By.XPATH,
        "//div[@id='searchPagination']//span[4]//a")
    SECOND_MIDDLE_PAGINATION_LINK = (
        By.XPATH,
        "//div[@id='searchPagination']//span[5]//a")
    THIRD_MIDDLE_PAGINATION_LINK = (
        By.XPATH,
        "//div[@id='searchPagination']//span[6]//a")
    FOURTH_MIDDLE_PAGINATION_LINK = (
        By.XPATH,
        "//div[@id='searchPagination']//span[7]//a")
    PRODUCT_PRICE = (
        By.CSS_SELECTOR,
        ".bold.green.size22")
    PRODUCT_TITLE = (
        By.CLASS_NAME,
        "address"
    )
