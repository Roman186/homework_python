from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://uitestingplayground.com/classattr")
blue_button = driver.find_element(By.CSS_SELECTOR, '.btn-primary')
blue_button.click()
sleep(3)

