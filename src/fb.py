from selenium import  webdriver
import time
import config
import os
from selenium.webdriver.common.keys import Keys

PATH="C:\Program Files (x86)\chromedriver.exe"

def get_image_path():

    img_files=os.listdir(config.image_path)
    return img_files

def facebook_group_post(user,pwd):
    chrome_options = webdriver.ChromeOptions()
    pref = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", pref)
    driver = webdriver.Chrome(PATH, chrome_options=chrome_options)

    #Login to facebook
    driver.get("https://www.facebook.com/")
    time.sleep(5)
    driver.find_element_by_name("email").send_keys(user)
    driver.find_element_by_name("pass").send_keys(pwd, Keys.RETURN)
    time.sleep(10)

    try:

        for k,v in config.FB_group_props.items():
            print(f"Posting contenet in {k} group/page")
            driver.get(v['url'])
            time.sleep(5)

            # Find the element to click on the post text box on the wall
            driver.find_element_by_xpath(v['wall_post_xpath']).click()
            time.sleep(10)

            #Write the text on the pop-up to post
            driver.find_element_by_xpath(v['popup_post_xpath']).send_keys("Hi Test post, 3/6 Take8")
            time.sleep(10)

            #Check if the Image Flag is set , if set upload the image
            if v['post_img_flag']:
                upload_img=driver.find_element_by_xpath(v['upload_img_input_xpath'])
                time.sleep(5)
                for file in os.listdir(config.image_path):
                    upload_img.send_keys(config.image_path+file)
                #upload_img.send_keys(get_image_path())

            #post the message and images
            post_msg=driver.find_element_by_xpath(v['submit_post'])
            time.sleep(5)
            post_msg.click()
            print(f"Posted sucessfully in the {k} group/page, opening next URL")
            time.sleep(5)

    except Exception as e:
        print("Exception Occurred: ",str(e))
    finally:
        print("Closing Browser....")
        time.sleep(10)
        driver.close()

def get_login():
    user = input("Please enter FB User Name:")
    pwd=input("Please enter FB Password:")
    #pwd = getpass.win_getpass("Password:")
    return user,pwd


