import pickle
import pprint
import time

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

from selenium import webdriver


def save_cookies(driver, location):

    pickle.dump(driver.get_cookies(), open(location, "wb"))


def load_cookies(driver, location, url=None):

    cookies = pickle.load(open(location, "rb"))
    driver.delete_all_cookies()
    # have to be on a page before you can add any cookies, any page - does not matter which
    driver.get("//chromedriver.exe" if url is None else url)
    for cookie in cookies:
        if isinstance(cookie.get('expiry'), float):#Checks if the instance expiry a float
            cookie['expiry'] = int(cookie['expiry'])# it converts expiry cookie to a int
        driver.add_cookie(cookie)


def delete_cookies(driver, domains=None):

    if domains is not None:
        cookies = driver.get_cookies()
        original_len = len(cookies)
        for cookie in cookies:
            if str(cookie["domain"]) in domains:
                cookies.remove(cookie)
        if len(cookies) < original_len:  # if cookies changed, we will update them
            # deleting everything and adding the modified cookie object
            driver.delete_all_cookies()
            for cookie in cookies:
                driver.add_cookie(cookie)
    else:
        driver.delete_all_cookies()

# #
# # # Path where you want to save/load cookies to/from aka C:\my\fav\directory\cookies.txt
cookies_location = "C:/Users/GOWTHAM/Downloads/web app/PycharmProjects/LINKCXO_0.1/cookies.txt"
#
# Initial load of the domain that we want to save cookies for
chrome = webdriver.Chrome()
chrome.get("http://linkcxo-frontend-testing.s3-website.ap-south-1.amazonaws.com/")
time.sleep(10)
#  Be a member
chrome.find_element(By.XPATH, "/html/body/div/div/div[1]/div/header/div/div[3]/button/a").click()

# phone number
chrome.find_element(By.ID, "outlined-basic").send_keys("9162849798")
time.sleep(2)

# click on arrow
chrome.find_element(By.XPATH, "//button[@aria-label='next']//*[name()='svg']").click()
time.sleep(10)

##otp box
chrome.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/form/div[1]/div/div[1]/input").send_keys("198989")
chrome.implicitly_wait(2)

# click on verify
chrome.find_element(By.XPATH, "//div[@class='css-1t62lt9']/button").click()
time.sleep(10)
x = chrome.title
print("The title of the current page is :" + x)
pprint.pprint(chrome.get_cookies())
print ("=====================\n")

save_cookies(chrome, cookies_location)
chrome.quit()
#
# # Load of the page you cant access without cookies, this one will fail
# chrome = webdriver.Chrome()
# chrome.get("hhttp://linkcxo-frontend-testing.s3-website.ap-south-1.amazonaws.com/feed")
#
#
# # Load of the page you cant access without cookies, this one will go through
# chrome = webdriver.Chrome()
# load_cookies(chrome, cookies_location)
# chrome.get("http://linkcxo-frontend-testing.s3-website.ap-south-1.amazonaws.com/feed")

# chrome = webdriver.Chrome()
# chrome.get("https://google.com")
# time.sleep(2)
# pprint.pprint(chrome.get_cookies())
# print "=========================\n"
#
# delete_cookies(chrome, domains=["www.google.com"])
# pprint.pprint(chrome.get_cookies())
# print "=========================\n"
#
# delete_cookies(chrome)
# pprint.pprint(chrome.get_cookies())