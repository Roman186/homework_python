from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)
driver.get("http://uitestingplayground.com/textinput")

LOCATOR_FIELD = ("xpath", "//input[@id='newButtonName']")
LOCATOR_BUTTON = ("xpath", "//button[@id='updatingButton']")

input_field = driver.find_element(*LOCATOR_FIELD)
input_field.send_keys("Skypro")

button = driver.find_element(*LOCATOR_BUTTON)
button.click()

button_text = wait.until(EC.text_to_be_present_in_element(LOCATOR_BUTTON, "Skypro"))

print(f"Текст кнопки: {button.text}")

driver.quit()
