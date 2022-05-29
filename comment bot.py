from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time 
import random 

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
        scrolls = 3
        for i in range(1, scrolls):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)

        
    def leave_comment(self,count):
        anchors = self.driver.find_elements_by_tag_name("a")
        anchors = [a.get_attribute("href") for a in anchors]
        anchors = [a for a in anchors if a.startswith("https://www.instagram.com/p/")]
        data = anchors[:count]
        #greeting = ["Hi", "Hello", "Hey", "Heeey", "Greetings"]

        for a in data:
            self.driver.get(a)
            time.sleep(5)

            #random_idx = random.randint(0, (len(greeting)-1))
            my_comment = " Nice Picture !! "
            
            form = self.driver.find_element_by_tag_name("form").click()
            text_area = self.driver.find_element_by_tag_name("textarea")
            text_area.send_keys(my_comment)
            
            submit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
            seconds = random.randint(1,10)
            time.sleep(seconds)
            


#input usename, password
acc= instagramBot(username, password) 
acc.login()
#input keyword to search
acc.search_img(keyword)
while True:
    try:
        #input qty count to comment
        acc.leave_comment(3)

    except Exception as e:
        acc.close_alert()
        print(e)
    finally:
        acc.driver.close()
        break
