from selenium import  webdriver
import time
import collections
from selenium.webdriver.common.keys import Keys

PATH="C:\Program Files (x86)\chromedriver.exe"

url="https://www.facebook.com/"

def facebook_post(user,pwd):
    # Use a breakpoint in the code line below to debug your script.

    driver = webdriver.Chrome(PATH)
    driver.get(url)
    time.sleep(5)
    driver.find_element_by_id("email").send_keys(user)
    driver.find_element_by_id("pass").send_keys(pwd)
    driver.find_element_by_name("login").click()
    time.sleep(10)

    groups=driver.find_elements_by_class_name("a8c37x1j")
    for group in groups: print(group,group.text)

    pass

def get_login():
    user = input(f"Please enter FB User Name :")
    pwd = input(f"Please enter FB Password :")
    return user,pwd


