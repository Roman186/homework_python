from selenium import webdriver


driver = webdriver.Chrome()
driver.implicitly_wait(16)

driver.get("http://uitestingplayground.com/ajax")

LOCATOR_BUTTON = ("xpath", "//button[@id='ajaxButton']")
LOCATOR_TXT = ("xpath", "//p[@class='bg-success']")

button = driver.find_element(*LOCATOR_BUTTON)
button.click()

txt = driver.find_element(*LOCATOR_TXT).text

print(f"Текст: {txt} виден и отображается")

driver.quit()


