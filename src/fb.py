from selenium import  webdriver
import time
import collections
import getpass
from selenium.webdriver.common.keys import Keys

PATH="C:\Program Files (x86)\chromedriver.exe"


def facebook_group_post(user,pwd):
    # Use a breakpoint in the code line below to debug your script.
    url = "https://www.facebook.com/groups/2512957342342147"
    url2="https://www.facebook.com/groups/473152883710976"
    chrome_options = webdriver.ChromeOptions()
    pref = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", pref)
    driver = webdriver.Chrome(PATH,chrome_options=chrome_options)

    try:
        driver.get(url)
        time.sleep(5)
        driver.find_element_by_name("email").send_keys(user)
        driver.find_element_by_name("pass").send_keys(pwd,Keys.RETURN)
        #driver.find_element_by_name("pass").send_keys(Keys.RETURN)
        time.sleep(10)
        #temp=driver.find_element_by_xpath("a8c37x1j")

        post=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/"
                                          "div[2]/div/div/div[4]/div/div/div/div/div[1]/div[1]/div/div/div/div[1]/div/div[1]/span")

        time.sleep(10)
        post.click()
        time.sleep(5)
        post_popup=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/"
                                                "div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/"
                                                "div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div")
        time.sleep(10)
        post_popup.send_keys("Hi Test post, take7")

        # upload_img=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/"
        #                                         "div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/"
        #                                         "div/div[1]/div[3]/div[1]/div[2]/div[1]/input")
        # #print(len(upload_img))
        #
        # time.sleep(10)
        #
        # upload_img.send_keys("C:/Users/User/PycharmProjects/facebookautomation/images/download.jpg")

        post_msg=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/"
                                              "div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/"
                                              "div[3]/div[2]/div[1]/div")
        time.sleep(10)
        post_msg.click()
        print("Posted sucessfully in the group, open next URL")
        time.sleep(5)
        driver.get(url2)
        time.sleep(5)

        post = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div[1]/div[1]/div/div/div/div[1]/div/div[1]/span")
        time.sleep(10)
        post.click()
        time.sleep(5)
        post_popup = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/"
                                                  "div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/"
                                                  "div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div")
        time.sleep(10)
        post_popup.send_keys("Hi Test post in new group, take3")
        post_msg = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/"
                                                "div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div[3]/div[2]/div/div")
        time.sleep(10)
        post_msg.click()
        print("Posted sucessfully in the 2nd group")


        #driver.find_element_by_class_name("a8c37x1j").send_keys("Hi this is test")

        # for t in temp:
        #
        #     if 'Create a public post' in t.text:
        #         print(t, t.text)
        #         t.click()
        #         time.sleep(10)
        #         post_text=driver.find_elements_by_class_name("notranslate")
        #
        #
        #
        #         for p in post_text:
        #             if p.get_attribute("role")=="textbox":
        #                 p.send_keys("Hi test from Python")
        #                 btn=driver.find_elements_by_class_name("oajrlxb2")
        #
        #
        #                 for b in btn:
        #                     if b.get_attribute("aria-label")=="Post":
        #                         b.click()
        #                 time.sleep(10)


                # print(len(post))

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
    user = input("Please enter FB User Name:")
    pwd=input("Please enter FB Password:")
    #pwd = getpass.win_getpass("Password:")
    return user,pwd


