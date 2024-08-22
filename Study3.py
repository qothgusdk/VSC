from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

#time.sleep(10)
driver.implicitly_wait(10)
driver.get('https://www.naver.com/')

#button = driver.find_element(By.ID, 'search-btn')
button =  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search-btn")))
button.click()