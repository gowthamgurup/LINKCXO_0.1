#
# import pickle
# import pprint
# import time
#
# import selenium
# from selenium.webdriver.chrome.options import Options
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys
#
# from selenium import webdriver
#
#
# driver = selenium.webdriver.Chrome(r"C:\Users\Gowtham p\Downloads\chromedriver_win32\chromedriver.exe")
# driver.get("http://linkcxo-frontend-testing.s3-website.ap-south-1.amazonaws.com")
#
# if __name__ == '__main__':
#     num = "9162849798"
#     pas = "198989"
#
#
# #  Be a member
# driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div/header/div/div[3]/button/a").click()
#
# # switch to mail or mobile numver
# # drive.find_element(By.XPATH,"//div/span/span/input").click()
#
# # phone number
# driver.find_element(By.ID, "outlined-basic").send_keys(num)
# time.sleep(2)
#
# # click on arrow
# driver.find_element(By.XPATH, "//button[@aria-label='next']//*[name()='svg']").click()
# time.sleep(10)
#
# ##otp box
# driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/form/div[1]/div/div[1]/input").send_keys(pas)
# driver.implicitly_wait(2)
#
# # click on verify
# driver.find_element(By.XPATH, "//div[@class='css-1t62lt9']/button").click()
# time.sleep(5)
# x = driver.title
# print("The title of the current page is :" + x)
# pprint.pprint(driver.get_cookies())
# print ("=====================\n")
#
# cookies = driver.get_cookies()
#
# pickle.dump(cookies, open("cookies.pkl", "wb"))



import time

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver = selenium.webdriver.Chrome(r"C:\Users\Gowtham p\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("http://linkcxo-frontend-testing.s3-website.ap-south-1.amazonaws.com")


