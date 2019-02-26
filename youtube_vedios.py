import time
from selenium.webdriver import Chrome
from contextlib import closing
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def BMP(s):
    return "".join((i if ord(i) < 10000 else '\ufffd' for i in s))

chrome_options = Options()  
chrome_options.add_argument("--headless")

with closing(Chrome(chrome_options=chrome_options)) as driver:
    wait = WebDriverWait(driver,20)
    driver.get("https://www.youtube.com/watch?v=t2eNRMAz8b4")

    for item in range(3): #by increasing the highest range you can get more content
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(3)

    for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#comment #content-text"))):
        print(BMP(comment.text))

