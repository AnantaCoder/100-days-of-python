'''INTERNET SPEED COMPLAINE BOT ONLINE AUTOMATION'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys 
import time 
import random
#--------------------------------------------------cons-----------------------------------------------------------------


PROMISED_DOWNLOAD = 500
PROMISED_UPLOAD = 100
TWITTER_PASSWORD = 0
SPEEDTEST = 'https://www.speedtest.net/'
TWITTER_URL = 'https://twitter.com/login'

class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down_speed = 0
        self.up_speed = 0
        
    def get_internet_speed(self):
        self.driver.get(SPEEDTEST)
        pop =  WebDriverWait(self.driver,50).until(EC.element_to_be_clickable((By.ID,'onetrust-accept-btn-handler')))
        pop.click()

        go_button = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')))
        go_button.click()
        #
        id_element = WebDriverWait(self.driver,100).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[1]/div/div/div[2]/div[2]/a'))).text
        print(id_element)

        down_speed = WebDriverWait(self.driver,100).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span'))).text
        up_speed = WebDriverWait(self.driver,100).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'))).text
        
        self.down_speed = float(down_speed)
        self.up_speed = float(up_speed)
        print(f'Download speed is {down_speed}, Upload speed is {up_speed}')
        # self.driver.quit()
    def tweet_at_provider(self):

        self.driver.get('https://twitter.com/login')

        username = WebDriverWait(self.driver,100).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')))
        username.click()
        username.send_keys('my username')
        username.send_keys(Keys.RETURN)
        time.sleep(5)
        # enter = WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH,'///*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div/span/span')))
        # enter.click()

        password = WebDriverWait(self.driver,100).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')))
        password.click()
        password.send_keys('my password ')
        password.send_keys(Keys.RETURN)

        form = WebDriverWait(self.driver,100).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')))
        form.click()
        form.send_keys(f"Hey JIO, why is my internet speed {self.down_speed} Mbps Down/{self.up_speed} Mbps Up when I pay for {PROMISED_DOWNLOAD} Mbps Down/{PROMISED_UPLOAD} Mbps Up? Please fix it for me.")
        post_btn = WebDriverWait(self.driver,100).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span')))
        post_btn.click()
            

if __name__ == "__main__":
    bot = InternetSpeedTwitterBot()
    bot.get_internet_speed()
    bot.tweet_at_provider()
    print("Your ISP is providing the expected speed of the Internet.")
    
    

