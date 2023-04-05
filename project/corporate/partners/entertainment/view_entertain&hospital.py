import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service
import time

# from project.Common.initial import *
# drive=commonlogin()
# time.sleep(5)

drive=webdriver.Chrome(r"C:\Users\Gowtham p\Downloads\chromedriver_win32\chromedriver.exe")
drive.get("http://linkcxo-frontend-testing.s3-website.ap-south-1.amazonaws.com/")
drive.maximize_window()
time.sleep(4)

# click on corporate
drive.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/header/div/div/div[2]/div[3]/div[4]").click()
time.sleep(3)

# click on partners
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[1]/div/div/div/button[2]/div/h5[1]").click()
time.sleep(3)

# click on entertainment& Hospitality
drive.find_element(By.XPATH,"")
