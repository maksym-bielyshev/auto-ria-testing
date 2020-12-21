from selenium.webdriver.common.by import By


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
        By.XPATH, "//button[@type='submit']//span[contains(text(),'Пошук')]")


class LocatorsProductPage:
    SELLER_NAME_TEXT = (
        By.CLASS_NAME, "seller_info_name bold")
    SHOW_PHONE_LINK = (
        By.CLASS_NAME, "size14 phone_show_link link-dotted mhide")
    SELLER_PHONE_TEXT = (
        By.XPATH, "//span[contains(@title,'телефон')]")
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
