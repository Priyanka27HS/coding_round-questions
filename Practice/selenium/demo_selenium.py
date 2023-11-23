import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testvagrant.myshopify.com/")
driver.maximize_window()

shop_all_button_locator = (By.XPATH, "//a[contains(text(),'Shop all')]")
shop_all_button = driver.find_element(*shop_all_button_locator)
time.sleep(2)
shop_all_button.click()
time.sleep(2)

search_element_locator = (By.XPATH, "(//*[name()='svg'][@class='modal__toggle-open icon icon-search'])[1]")
search_element = driver.find_element(*search_element_locator)
time.sleep(2)
search_element.click()
time.sleep(2)

search_bar = (By.XPATH, "//input[@name='q']")
# "//input[@id='Search-In-Modal']")
search_bar = driver.find_element(*search_bar)
time.sleep(2)
search_bar.click()
time.sleep(5)
search_bar.send_keys("anime")
time.sleep(5)

search_anime = (By.XPATH, "(//*[name()='svg'][@role='presentation'])[7]")
search_anime = driver.find_element(*search_anime)
time.sleep(2)
search_anime.click()
time.sleep(2)

driver.close()

# Select class

# All list box related methods are implemented inside the class “Select”

# 1. select_item_by_visible_text
# 2. select_item_by_index
# 3. select_by_value


# 1. select_item_by_visible_text

# from selenium.webdriver.support.select import Select

# open the browser
# driver = webdriver.Chrome()
# enter the url
# driver.get("https://www.w3schools.com/python/")

# select_by_visible_text Selects an <option> based upon its text

# list_box = driver.find_element_by_id("Cars")
# s = Select(list_box)
# s.select_by_visible_text("Audi")
# sleep(5)
# s.select_by_visible_text("Benz")


# 2. select_item_by_index

# select_by_index Selects an <option> based upon the <select> element's internal index
# Index starts from 1

# s.select_by_index(9)
# sleep(4)
# s.select_by_index(3)


# 3. select_by_value

# select_by_value selects an <option> based upon its value attribute

# s.select_by_value("ben")
# sleep(2)
# s.select_by_value("di")
