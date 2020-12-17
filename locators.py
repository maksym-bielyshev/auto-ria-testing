from selenium.webdriver.common.by import By


class LocatorsLogin:
    LOGIN_FIELD = (By.ID, "emailloginform-email")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='emailloginform-password']")
    CONTINUE_BUTTON = (By.XPATH, "//button[contains(text(),'Увійти')]")
