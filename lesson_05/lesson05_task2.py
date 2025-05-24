from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")
blue_button = driver.find_element('xpath', '//button[text()="Button with Dynamic ID"]')
blue_button.click()
sleep(3)
driver.quit()