from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/inputs")
input_box = driver.find_element('xpath', '//input[@type="number"]')
input_box.send_keys("Sky")
input_box.clear()
input_box.send_keys("Pro")
driver.quit()
