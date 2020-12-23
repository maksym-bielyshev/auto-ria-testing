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
        By.XPATH, "//button[@type='submit']//span")
