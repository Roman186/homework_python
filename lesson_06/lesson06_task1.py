from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

driver.get("http://uitestingplayground.com/ajax")

LOCATOR_BUTTON = ("xpath", "//button[@id='ajaxButton']")
LOCATOR_TXT = ("xpath", "//p[@class='bg-success']")

button = driver.find_element(*LOCATOR_BUTTON)
button.click()

txt = wait.until(EC.visibility_of_element_located(LOCATOR_TXT)).text

print(f"Текст: {txt} виден и отображается")

driver.quit()
