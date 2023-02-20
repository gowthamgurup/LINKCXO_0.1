# import pathlib, pickle
# from lib2to3.pgen2 import driver
#
# # import chromedriver as chromedriver
# from selenium.webdriver.chrome.options import Options
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys
# import time
#
# # import undetected_chromedriver as chromedriver
#
# # chromedriver.TARGER_VERSION=110
# # chromedriver.install()
#
#
# # def save_cookies_file(url):
# #     chrome_driver_path = '{0}C:/Users/GOWTHAM/Downloads/web app/PycharmProjects/LINKCXO_0.1/drive/chromedriver.exe'.format(
# #         str(pathlib.path(__file__).parent.absolute()))
# #     chrome_options = Options()
# #     # chrome_options.add_experimental_option('debuggerAddress','127.0.0.1:9222')
# #     drive=webdriver.Chrome(options=chrome_options,executable_path=chrome_driver_path)
# #     drive.get(url)
# #     pickle.dump(drive.get_cookies(),open("cookies.txt","wb"))
# # save_cookies_file("http://linkcxo-frontend-testing.s3-website.ap-south-1.amazonaws.com/")
#
#
# import pprint
# import pickle
# import selenium.webdriver
#
# driver = selenium.webdriver.Chrome(r"C:\Users\Gowtham p\Downloads\chromedriver_win32\chromedriver.exe")
# driver.get("http://linkcxo-frontend-testing.s3-website.ap-south-1.amazonaws.com/")
#
#
# #  Be a member
# driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div/header/div/div[3]/button/a").click()
# time.sleep(2)
# # phone number
# driver.find_element(By.ID, "outlined-basic").send_keys("9162849798")
# time.sleep(2)
#
# # click on arrow
# driver.find_element(By.XPATH, "//button[@aria-label='next']//*[name()='svg']").click()
# time.sleep(10)
#
# ##otp box
# driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/form/div[1]/div/div[1]/input").send_keys("198989")
# driver.implicitly_wait(2)
#
# # click on verify
#
# driver.find_element(By.XPATH, "//div[@class='css-1t62lt9']/button").click()
# time.sleep(5)
# x = driver.title
# print("The title of the current page is :" + x)
# pprint.pprint(driver.get_cookies())
# print ("=====================\n")
#
# time.sleep(5)
#
# pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
#
# time.sleep(5)
#
#
# cookies = pickle.load(open("cookies.pkl", "rb"))
# for cookie in cookies:
#     driver.add_cookie(cookie)
#     time.sleep(5)


#
#

import pathlib, pickle

import pickle
import pprint

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

#
# # "start frome here"
#
#
#
#
#
# # "end from here"
#
#
#
#
# # def save_cookies_file(url):
# #     chrome_driver_path= str(pathlib.path(__file__).parent.absolute())+'/chromedriver.exe'
# #     chrome_options= Options()
# #     # chrome_options.add_experimental_option('debuggerAddress','127.0.0.1:9222')
# #     drive=webdriver.Chrome(options=chrome_options,executable_path=chrome_driver_path)
# #     drive.get(url)
# #     pickle.dump(drive.get_cookies(),open("cookies.txt","wb"))
# # save_cookies_file("http://linkcxo-frontend-testing.s3-website.ap-south-1.amazonaws.com/")
# #
#


def save_cookies(driver,location):
    pickle.dump(driver.get_cookies(), open(location, "wb"))

def load_cookies(driver,location,url=None):
    cookies=pickle.load(open(location,"rb"))
    driver.delete_all_cookies()
    url="http://linkcxo-frontend-testing.s3-website.ap-south-1.amazonaws.com/"
    driver.get(url)
    for cookie in cookies:
        driver.add_cookie(cookie)


def delete_cookies(driver,domains=None):
    cookies = driver.get_cookies()
    for cookie in cookies:
        if domains is not None:
            if str(cookie["domain"]) in domains:
                cookies.remove(cookie)
        else:
            driver.delete_all_cookies()
            return
    driver.delete_all_cookies()
    for cookie in cookies:
        driver.add_cookie(cookie)


# # # initial load of the domain that we want to save cookies for
# chrome = webdriver.Chrome()
# chrome.get("http://linkcxo-frontend-testing.s3-website.ap-south-1.amazonaws.com/")

# #  Be a member
# chrome.find_element(By.XPATH, "/html/body/div/div/div[1]/div/header/div/div[3]/button/a").click()
#
# # switch to mail or mobile numver
# # chrome.find_element(By.XPATH,"//div/span/span/input").click()
#
# # phone number
# chrome.find_element(By.ID, "outlined-basic").send_keys("9162849798")
# time.sleep(2)
#
# # click on arrow
# chrome.find_element(By.XPATH, "//button[@aria-label='next']//*[name()='svg']").click()
# time.sleep(10)
#
# ##otp box
# chrome.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/form/div[1]/div/div[1]/input").send_keys("198989")
# chrome.implicitly_wait(2)
#
# # click on verify
#
# chrome.find_element(By.XPATH, "//div[@class='css-1t62lt9']/button").click()
# time.sleep(10)
# x = chrome.title
# print("The title of the current page is :" + x)
# save_cookies(chrome,"C:/Users/GOWTHAM/Downloads/web app/PycharmProjects/LINKCXO_0.1/project/cookies.pkl")
# pprint.pprint(chrome.get_cookies())
# print ("=====================\n")

# save_cookies(chrome,"")

#
#
#
# #load of the page we cannot accse the page without cookies
# chrome = webdriver.Chrome()
# chrome.get("http://linkcxo-frontend-testing.s3-website.ap-south-1.amazonaws.com/")
# time.sleep(10)


#load of the page we cannot accse the page without cookies
chrome = webdriver.Chrome()
load_cookies(chrome,"C:/Users/GOWTHAM/Downloads/web app/PycharmProjects/LINKCXO_0.1/project/cookies.pkl")
chrome.get("http://linkcxo-frontend-testing.s3-website.ap-south-1.amazonaws.com/profile")
time.sleep(10)
#
#
#
#
# # #load of the page we cannot accse the page without cookies
# # chrome = webdriver.Chrome()
# # chrome.get("http://linkcxo-frontend-testing.s3-website.ap-south-1.amazonaws.com/")
# # time.sleep(3)
# # pprint.pprint(chrome.get_cookies())
# # print ("=====================\n")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#






