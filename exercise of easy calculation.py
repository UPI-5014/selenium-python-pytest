from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get("https://www.easycalculation.com/")
driver.maximize_window()
time.sleep(6)

sign_in_button = driver.find_element(By.XPATH, '//*[@id="wrap"]/div[2]/div[2]/span[2]/a/span')
sign_in_button.click()
time.sleep(6)


email_box = driver.find_element(By.ID, "log_email")
email_box.send_keys("208r1a05i2cse@gmail.com")
time.sleep(6)

password_box = driver.find_element(By.NAME, "log_password")
password_box.send_keys("Lasmaiah@5014")
time.sleep(6)

login_button = driver.find_element(By.XPATH, '//*[@id="log_frm"]/div[4]/input[1]')
login_button.click()
time.sleep(6)


search_box = driver.find_element(By.ID, "googleSearchId")
search_box.send_keys("Bangalore")
search_box.send_keys(Keys.RETURN)
time.sleep(6)



driver.quit()
print("Browser closed successfully.")











