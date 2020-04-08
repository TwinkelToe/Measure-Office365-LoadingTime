from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from datetime import datetime
import os
import time
import requests
from lxml import html

def getCookie():
    #launch url
    url = "SHAREPOINTURL"

    # create a new Firefox session
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)    

    adfs_timer = time.time()
    driver.get(url)

    #After opening the url above, Selenium clicks the specific agency link
    python_textbox = driver.find_element_by_id('i0116') #FHSU
    python_textbox.send_keys('UserName')

    NextButton = driver.find_element_by_id('idSIButton9')
    NextButton.click()

    #After opening the url above, Selenium clicks the specific agency link
    python_textbox = driver.find_element_by_id('passwordInput') #FHSU
    python_textbox.send_keys('Password' + Keys.ENTER)
    driver.implicitly_wait(50)
   
     adfs_timer = time.time() - adfs_timer
    print("ADFS Login time: {}".format(adfs_timer))
    onedrive_timer = time.time()
    try:
        wait = WebDriverWait(driver, 60)
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[3]/div[2]/div/section/div/div/div/div/div/div/div/div/div[2]/div[3]/button/div/i')))
    except:
        print("Never found Approot, exit")
        exit
    onedrive_timer = time.time() - onedrive_timer
    print("OneDrive Login time: {}".format(onedrive_timer))

    f = open("loadingtimes.txt", "a")
    f.write("\n{},{},{}".format(datetime.now(), adfs_timer, onedrive_timer))
    f.close()
    print()
    # s = requests.Session()    
    print("done")

    # driver.quit()
if __name__ == "__main__":
    while True:
        getCookie()
        time.sleep(30)

