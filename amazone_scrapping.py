from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open browser
driver = webdriver.Chrome()

# Open website
driver.get("https://dir.indiamart.com/search.mp?ss=mens+watches&src=as-popular%7Ckwd%3Dwatches%7Cpos%3D2%7Ccat%3D-2%7Cmcat%3D-2%7Ckwd_len%3D7%7Ckwd_cnt%3D1&prdsrc=1")

# Wait for page to load
time.sleep(2)

# Find all quotes
quotes = driver.find_elements(By.CLASS_NAME, "sidebarText")

# Print quotes
for q in quotes[:]:
    print(q.text)

# Close browser
driver.quit()



