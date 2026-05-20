import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://demoqa.com/select-menu")

driver.find_element(By.XPATH, "//div[@id = 'withOptGroup']").click()
driver.find_element(By.XPATH, "//div[text() = 'Group 2, option 1']").click()

old_style = Select(driver.find_element(By.XPATH, "//select[@id = 'oldSelectMenu']"))
old_style.select_by_visible_text("Purple")

'''#select by value 
dropdown.select_by_value("2")

#select by index    
dropdown.select_by_index(1)'''

print("Selected option: ",old_style.first_selected_option.text)
print("The colour options are :" )
for options in old_style.options:
    print(options.text)

time.sleep(5)
driver.quit()