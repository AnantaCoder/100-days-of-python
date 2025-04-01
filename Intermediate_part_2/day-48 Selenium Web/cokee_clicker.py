from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time 
import random

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://orteil.dashnet.org/cookieclicker/')

#lang popup click
try:
    lang_section = WebDriverWait(driver,100).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="langSelect-EN"]')))
    lang_section.click()

except Exception as e:
    print(f"An error occurred, while clicking the language: {e}")
    
#cookee click
try:
    cookie = WebDriverWait(driver,120).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="bigCookie"]')))
    time.sleep(5)
except Exception as es:
    print(f"An error occurred, while clicking the cookie: {es}")
    # driver.quit()
    
number_of_times = random.randint(100, 1000)
for _ in range(number_of_times):
    try:
        cookie.click()
        time.sleep(0.02)
    except Exception as e :
        print(f"An error occurred, while clicking the cookie: {e}")
        break