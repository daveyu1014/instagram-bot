# -*- coding: utf-8 -*-
"""
Created on Sat May 28 19:01:34 2022

@author: dave7
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
import wget

class instagramBot:
    def __init__(self, username, password, url):
        self.username = username
        self.password = password
        self.driver= webdriver.chrome(r'C:\webdriver\chromedriver')
        self.url = "http://www.instagram.com"

    def get_driver():
        driver = webdriver.Chrome(r'C:\webdriver\chromedriver')
        driver.implicitly_wait(10)
        url="http://www.instagram.com"
        driver.get(url)

    def login(self):
    
        username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
        password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

        #username and password
        username.clear()
        username.send_keys("my_username")
        password.clear()
        password.send_keys("my_password")

        #login button and click
        button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

# NOT NOW
not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

#target the search input field
searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
searchbox.clear()

#hashtag keyword
keyword = "#travel"
searchbox.send_keys(keyword)
 
# Wait for 5 seconds
time.sleep(5)
searchbox.send_keys(Keys.ENTER)
time.sleep(5)
searchbox.send_keys(Keys.ENTER)
time.sleep(5)

driver.execute_script("window.scrollTo(0, 4000);")
images = driver.find_elements_by_tag_name('img')
images = [image.get_attribute('src') for image in images]
images = images[:-2]
print('Number of scraped images: ', len(images))


path = (r"C:\Users\dave7\Downloads")
print(path)
os.chdir(path)
path = os.path.join(path, 'test')
os.mkdir(path)
save_as = os.path.join(path, 'picture.jpg')
wget.download(url, save_as)
