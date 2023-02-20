
import pickle
import pprint

# import cookies as cookies
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import pickle
import os
import selenium.webdriver
# files = os.listdir("cookies")
files = "C:/Users/GOWTHAM/Downloads/web app/PycharmProjects/LINKCXO_0.1/project/cookies.pkl"
driver = selenium.webdriver.Chrome(r"C:\Users\Gowtham p\Downloads\chromedriver_win32\chromedriver.exe")
# driver.get("http://linkcxo-frontend-testing.s3-website.ap-south-1.amazonaws.com/")
#
#
#
# #  Be a member
# driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div/header/div/div[3]/button/a").click()
#
# # switch to mail or mobile numver
# # drive.find_element(By.XPATH,"//div/span/span/input").click()
#
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
# pickle.dump(driver.get_cookies(), open("cookies.txt", "wb"))
# # pickle.dump(driver.get_cookies(), open("cookies.txt", "wb"))
# # time.sleep(5)


#
# for f in files:
#     cookies = pickle.load(open(f, "rb"))
#     for cookie in cookies:
#         driver.add_cookie(cookie)


#
# cookies = pickle.load(open("cookies.pkl", "rb"))
# for cookie in cookies:
#     driver.add_cookie(cookie)
#     time.sleep(5)



# cookies = pickle.load(open("cookies.txt", "rb"))
# for cookie in cookies:
#     driver.add_cookie(cookie)
#     time.sleep(5)



