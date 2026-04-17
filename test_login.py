from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver,10)
driver.get("https://the-internet.herokuapp.com/login")

wait.until(EC.visibility_of_element_located((By.NAME, 'username'))).send_keys("wrong")
wait.until(EC.visibility_of_element_located((By.ID, 'password'))).send_keys("wrong")

wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space() = 'Login']"))).click()
message = wait.until(EC.visibility_of_element_located((By.ID, 'flash'))).text
print(message)

driver.get("https://the-internet.herokuapp.com/login")#reload the page to clear the error message

wait.until(EC.visibility_of_element_located((By.NAME, 'username'))).send_keys("tomsmith")
wait.until(EC.visibility_of_element_located((By.ID, 'password'))).send_keys("SuperSecretPassword!")

wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space() = 'Login']"))).click()
message = wait.until(EC.visibility_of_element_located((By.ID, 'flash'))).text     
print(message)

wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space() = 'Logout']"))).click()
driver.quit()   
