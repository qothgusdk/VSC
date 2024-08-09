from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
url = 'https://www.naver.com/'
driver.get(url)

driver.find_element(By.XPATH, '//*[@id="account"]/div/a').click() #로그인 버튼 선택
driver.find_element(By.ID, 'id').send_keys('id') #id 입력
driver.find_element(By.ID, 'pw').send_keys('pw') #pw 입력

time.sleep(2)
driver.find_element(By.ID, 'log.login').click() #로그인 버튼 선택