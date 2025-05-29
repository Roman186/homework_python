from selenium import webdriver


driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/textinput")

LOCATOR_FIELD = ("xpath", "//input[@id='newButtonName']")
LOCATOR_BUTTON = ("xpath", "//button[@id='updatingButton']")

input_field = driver.find_element(*LOCATOR_FIELD)
input_field.send_keys("Skypro")

button = driver.find_element(*LOCATOR_BUTTON)
button.click()

print(f"Текст кнопки: {button.text}")

driver.quit()

