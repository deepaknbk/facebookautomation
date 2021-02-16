from selenium import  webdriver
import time
import collections
from selenium.webdriver.common.keys import Keys

PATH="C:\Program Files (x86)\chromedriver.exe"


def facebook_group_post(user,pwd):
    # Use a breakpoint in the code line below to debug your script.
    url = "https://www.facebook.com/groups/2512957342342147"
    driver = webdriver.Chrome(PATH)
    try:
        driver.get(url)
        time.sleep(5)
        driver.find_element_by_name("email").send_keys(user)
        driver.find_element_by_name("pass").send_keys(pwd,Keys.RETURN)
        #driver.find_element_by_name("pass").send_keys(Keys.RETURN)
        time.sleep(10)
        temp=driver.find_elements_by_class_name("a8c37x1j")
        #driver.find_element_by_class_name("a8c37x1j").send_keys("Hi this is test")
        print(len(temp))
        for t in temp:

            if 'Create a public post' in t.text:
                print(t, t.text)
                t.click()
                time.sleep(10)
                driver.find_element_by_class_name("bi6gxh9e").send_keys("Hi this is a test post")

                #t.send_keys("Hi this is a test post")

        # driver.find_element_by_class_name("thodolrn")
        # groups = driver.find_elements_by_class_name("oajrlxb2")
        # for group in groups:
        #     if group.get_attribute("aria-label")=="Groups":
        #         group.click()
        #         time.sleep(10)
        #         break
    except Exception as e:
        print("Exception Occurred: ",str(e))
    finally:
        print("Closing Browser....")
        driver.close()

    pass

def get_login():
    user = input(f"Please enter FB User Name :")
    pwd = input(f"Please enter FB Password :")
    return user,pwd


