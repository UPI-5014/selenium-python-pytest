from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()


driver.get("https://www.opencart.com/index.php?route=account/account&member_token=2f82808973797142aee08e2ae7de85c7")

# Maximize the browser window
driver.maximize_window()
time.sleep(5)

edit_box = driver.find_element(By.ID, "email")
edit_box.send_keys("208r1a05i2cse@gmail.com")
edit_box.send_keys(Keys.RETURN)
time.sleep(5)

edit_box = driver.find_element(By.NAME, "password")
edit_box.send_keys("Lasmaiah@5014")
edit_box.send_keys(Keys.RETURN)
time.sleep(5)