from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 25)

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

LOCATOR_DONE = ("xpath", "//p[text()='Done!']")
LOCATOR_ALL_IMG = ("tag name", "img")

wait.until(EC.visibility_of_element_located(LOCATOR_DONE))

src_third_image = driver.find_elements(*LOCATOR_ALL_IMG)

print(f"src третьей картинки: {src_third_image[3].get_attribute('src')}")

driver.quit()
