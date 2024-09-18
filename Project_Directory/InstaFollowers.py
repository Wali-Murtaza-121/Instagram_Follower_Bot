from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import os
import time

USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]
SIMILAR_ACCOUNTS = os.environ["SIMILAR_ACCOUNTS"]

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get(url="https://www.instagram.com")
        time.sleep(5)
        self.user_name = self.driver.find_element(By.XPATH,value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        self.user_name.send_keys(USERNAME)
        time.sleep(5)
        self.password = self.driver.find_element(By.XPATH,value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        self.password.send_keys(PASSWORD)
        time.sleep(5)
        self.password.send_keys(Keys.ENTER)
        # self.login_button = self.driver.find_element(By.XPATH,value='//*[@id="loginForm"]/div/div[3]/button')
        # self.login_button.click()
        time.sleep(2)
        self.notnow_button = self.driver.find_element(By.XPATH,value='//*[@id="mount_0_0_23"]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div/div[contains(text(),"Not now")]')
        if self.notnow_button:
            self.notnow_button.click()

    def find_followers(self):
        time.sleep(5)
        self.driver.get(url=f"https://www.instagram.com/the_chefs_wife_/followers")
        time.sleep(8.2)
        self.scroll = self.driver.find_element(By.XPATH,value='/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",self.scroll)
            time.sleep(2)

    def follower(self):
        self.all_buttons = self.driver.find_elements(By.CLASS_NAME,value="._acan")
        for button in self.all_buttons:
                button.click()
                time.sleep(1.1)