# open google.com
# search campusx
# learnwith.campusx.in
# dsmp course page

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

s = Service("D:/Advanced Web - scarp using Selenium/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get('https://google.com')
time.sleep(2)

#fetch the search input box using xpath
user_input = driver.find_element(by=By.XPATH , value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
user_input.send_keys('Campus x')
time.sleep(1)

user_input.send_keys(Keys.ENTER)
time.sleep(1)

link = driver.find_element(by=By.XPATH,value='//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[1]/div/a')
link.click()
time.sleep(1)

link2 = driver.find_element(by=By.XPATH,value='/html/body/div[1]/header/section[2]/a[5]')
link2.click()

