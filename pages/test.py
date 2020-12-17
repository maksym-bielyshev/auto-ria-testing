from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://auto.ria.com/uk/login.html")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/form[1]/div[1]/div[2]/input[1]")))
elem = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/form[1]/div[1]/div[2]/input[1]")
elem.send_keys("test")

# driver = webdriver.Chrome()
# driver.get("https://www.google.com/")
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/div[@id='viewport']/div[@id='searchform']/form[@id='tsf']/div[2]/div[1]/div[1]/div[1]/div[2]/input[1]")))
# elem = driver.find_element_by_xpath("//body/div[@id='viewport']/div[@id='searchform']/form[@id='tsf']/div[2]/div[1]/div[1]/div[1]/div[2]/input[1]")
# elem.send_keys("test")
