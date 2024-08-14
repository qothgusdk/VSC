from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys #키보드 사용
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
url = 'https://www.google.co.kr/'
driver.get(url)

driver.execute_script('window.open("https://www.naver.com/");') 

time.sleep(1)
driver.execute_script('window.open("https://www.daum.net/");')

time.sleep(1)
driver.switch_to.window(driver.window_handles[0])

driver.find_element(By.CSS_SELECTOR, '.gLFyf').send_keys('파이썬')
driver.find_element(By.CSS_SELECTOR, '.gLFyf').send_keys(Keys.ENTER)
driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div[1]/div/div/span/a/h3').click()
driver.back()

time.sleep(1)
driver.switch_to.window(driver.window_handles[1])