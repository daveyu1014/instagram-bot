# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
import wget

class instagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver= webdriver.Chrome(r'C:\webdriver\chromedriver')
        self.url="http://www.instagram.com"


    def get_driver(self):
        driver=self.driver
        driver.implicitly_wait(10)
        driver.get(self.url)

    def login(self):
        self.get_driver()
        username = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
        password = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
        #username and password
        username.clear()
        username.send_keys(self.username)
        password.clear()
        password.send_keys(self.password)
        #login button and click
        button = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
        time.sleep(5)
        x_path='/html/body/div[1]/section/main/div/div/div/div/button'
        not_now = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "稍後再說")]'))).click()
        time.sleep(3)

    def close_alert(self):
        not_now = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "稍後再說")]'))).click()
        
        
    def search_img(self,keyword):
        #target the search input field
        searchbox = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='搜尋']")))
        searchbox.clear()
        
        #hashtag keyword
        searchbox.send_keys('#' + keyword)
        time.sleep(2)
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        searchbox.send_keys(Keys.RETURN)
        time.sleep(5)
        
        # scroll image
        self.driver.execute_script("window.scrollTo(0, 4000);")
        images = self.driver.find_elements_by_tag_name('img')
        images = [image.get_attribute('src') for image in images]
        images = images[:-2]
        print('Number of scraped images: ', len(images))
        self.images = images

    def download_img(self, keyword):
            path= (f'C:\\Users\\dave7\\Downloads\\{keyword}')
            if not os.path.exists(path):
                os.makedirs(path)
            else:
                print('folder exists')
        
            counter = 0
            for img in self.images[1:]:
                save_as = os.path.join(path, keyword + str(counter) + '.jpg')
                wget.download(img, save_as)
                counter +=1

acc = instagramBot('username', 'password')
acc.login()
while True:
    try:
        acc.close_alert()
        keyword='travel'
        acc.search_img(keyword)
        
        acc.download_img(keyword)
    except Exception as e:
        acc.close_alert()
        print(e)
    finally:
        acc.driver.close()
        break