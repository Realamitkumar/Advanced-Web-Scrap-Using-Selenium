from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

s = Service("D:/Advanced Web - scarp using Selenium/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get('https://www.smartprix.com/mobiles')
time.sleep(1)

# filter applying on smartphones
driver.find_element(by=By.XPATH,value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input').click()
time.sleep(1)
driver.find_element(by=By.XPATH,value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input').click()
time.sleep(2)


old_height = driver.execute_script('return document.body.scrollHeight')

counter = 1
while True:

    driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
    time.sleep(1)

    new_height = driver.execute_script('return document.body.scrollHeight')

    print(counter)
    counter += 1
    print(old_height)
    print(new_height)

    if new_height == old_height:
        break

    old_height = new_height

html = driver.page_source
with open('smartprix,html','w',encoding='utf-8') as f:
    f.write(html)



# load more smartphones
driver.find_element(by = By.XPATH,value='//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
time.sleep(1)
driver.find_element(by = By.XPATH,value='//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
time.sleep(1)
driver.find_element(by = By.XPATH,value='//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
time.sleep(1)