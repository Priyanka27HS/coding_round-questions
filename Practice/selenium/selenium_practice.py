import time
from selenium.webdriver.support import expected_conditions as EC

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://testvagrant.myshopify.com/")
driver.maximize_window()

shop_all_button = (By.XPATH, "//a[contains(text(),'Shop all')]")
actual_price_element_locator = (
    By.XPATH, "(//span[contains(text(),'Rs. 70.00')]/..//span[contains(text(),'Regular price')])[1]")
search_button = (By.XPATH, "//input[@id='Search-In-Modal']")
search_val = (By.XPATH, "(//*[name()='svg'][@role='presentation'])[7]")


# "//button[contains(text(),'Search for 'anime'')]//*[name()='svg']")

# correct xpath :
# //button[contains(text(),'Search for “anime”')]//*[name()='svg']

# def select_shopall():
#     shop_all_element = driver.find_element(*shop_all_button)
#     shop_all_element.click()
#
#
# def get_actual_price():
#     actual_price_element = driver.find_element(*actual_price_element_locator)
#     actual_price_value = actual_price_element.text
#
#     expected_price = "Rs. 70.00"  # Replace with your expected price
#
#     if actual_price_value == expected_price:
#         print(f"Actual Price ({actual_price_value}) matches Expected Price ({expected_price}).")
#     else:
#         print(f"Actual Price ({actual_price_value}) does not match Expected Price ({expected_price}).")
#
#     return actual_price_value


def search_titles():
    search_product = driver.find_element(*search_button)
    wait = WebDriverWait(driver, 10)
    search_product = wait.until(EC.element_to_be_clickable((By.XPATH, search_product)))

    time.sleep(5)
    search_product.click()
    time.sleep(5)
    search_product.send_keys("anime")
    search_anime = driver.find_element(*search_val)
    time.sleep(3)
    search_anime.click()


# select_shopall()
# actual_price = get_actual_price()
search_titles()

driver.close()
