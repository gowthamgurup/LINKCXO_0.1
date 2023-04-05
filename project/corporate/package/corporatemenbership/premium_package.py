from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time


# this is how we call the function in same project in other files
from project.Common.initial import *
drive = commonlogin()
time.sleep(10)

# clink on corporate
drive.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/header/div/div/div[2]/div[3]/div[4]").click()
time.sleep(2)



#click on corporate membership
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div[1]/div/img").click()
time.sleep(5)

# click on lxr50
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[3]/div/div/div/div[1]/div/div[1]/div/div/div/img").click()
time.sleep(5)

# click on for 50 membership
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[3]/div/div/div/div/div/div[1]/div/div/div/img").click()
time.sleep(5)

# click on purchase now
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div/div[3]/div[2]/div/button").click()
time.sleep(5)

# # click on
# drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div/div[3]/div[2]/div/button").click()
# time.sleep(5)

# click on alert
alert = Alert(drive)
print(alert.text)
alert.accept()
time.sleep(50)



