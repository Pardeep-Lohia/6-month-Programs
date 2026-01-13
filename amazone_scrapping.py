from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://dir.indiamart.com/search.mp?ss=womens+watches&prdsrc=1&v=4&mcatid=108288&catid=248&cq=ludhiana&tags=res:RC2|ktp:N0|stype:attr=1|mtp:G|wc:2|lcf:3|cq:ludhiana|qr_nm:gl-gd|cs:19412|com-cf:nl|ptrs:na|mc:16919|cat:248|qry_typ:P|lang:en|tyr:2|qrd:260112|mrd:260113|prdt:260113|msf:ls|pfen:1|gli:U0G0I0|gc:Ludhiana|ic:Ludhiana|scw:1|emt:100")
time.sleep(5)

# ✅ Scroll to load all products
def scroll_to_bottom(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

scroll_to_bottom(driver)

links = driver.find_elements(By.CSS_SELECTOR, "a.cardlinks:not(.elps):not(.elps1)")
prices = driver.find_elements(By.CSS_SELECTOR, "p.price, p.getquote")

print("Links found:", len(links))
print("Prices found:", len(prices))


count = min(len(links), len(prices))

for i in range(count):
    link_text = links[i].text.strip()
    price_text = prices[i].text.strip()
    print(f"{link_text} : {price_text}")

with open("output.txt", "w", encoding="utf-8") as f:
    for i in range(count):
        link_text = links[i].text.strip()
        price_text = prices[i].text.strip()
        f.write(f"{link_text} : {price_text}\n")
driver.quit()
