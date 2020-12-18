from selenium.webdriver.common.by import By


class LocatorsHomeFilter:
    ALL_AUTOS = (
        By.XPATH,
        "//body/div[@id='app']/main[1]/div[2]/div[2]/form[1]/div[1]/label[1]"
    )
    USED_AUTOS = (
        By.XPATH,
        "//body/div[@id='app']/main[1]/div[2]/div[2]/form[1]/div[1]/label[2]"
    )
    NEW_AUTOS = (
        By.XPATH,
        "//body/div[@id='app']/main[1]/div[2]/div[2]/form[1]/div[1]/label[3]"
    )
    AUTOS_FOR_DELIVERY = (
        By.XPATH,
        "//body/div[@id='app']/main[1]/div[2]/div[2]/form[1]/div[1]/label[4]"
    )
    CATEGORY_DROPDOWN = (
        By.XPATH,
        "//select[@id='categories']"
    )
    BRAND_DROPDOWN = (
        By.XPATH,
        "//input[@id='brandTooltipBrandAutocompleteInput-brand']"
    )
    MODEL_DROPDOWN = (
        By.XPATH,
        "//body/div[@id='app']/main[1]/div[2]/div[2]/form[1]/div[2]/div[1]/"
        "div[3]/div[1]/div[2]/div[1]/label[1]"
    )
    REGION_DROPDOWN = (
        By.XPATH,
        "//input[@id='brandTooltipBrandAutocompleteInput-region']"
    )
    YEAR_FROM_DROPDOWN = (
        By.XPATH,
        "//select[@id='yearFrom']"
    )
    YEAR_TO_DROPDOWN = (
        By.XPATH,
        "//select[@id='yearTo']"
    )
    PRICE_FROM = (
        By.XPATH,
        "//input[@id='priceFrom']"
    )
    PRICE_TO = (
        By.XPATH,
        "//input[@id='priceTo']"
    )
    SEARCH_BUTTON = (
        By.XPATH,
        "//body/div[@id='app']/main[1]/div[2]/div[2]/form[1]/div[3]/button[1]/"
        "span[1]"
    )
    CHECKED_VIN = (
        By.XPATH,
        "//body/div[@id='app']/main[1]/div[2]/div[2]/form[1]/div[2]/div[3]/"
        "label[1]/span[1]"
    )
