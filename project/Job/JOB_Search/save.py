from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time


# this is how we call the function in same project in other files
from project.Common.initial import *
drive = commonlogin()
time.sleep(10)

# job in home page
drive.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/header/div/div/div[2]/div[3]/div[2]/div[2]/h2").click()
time.sleep(2)



#scroll up it reach to saved
element = drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[3]/div/div[7]/div/div[3]")
actions = ActionChains(drive)
actions.move_to_element(element).perform()
time.sleep(10)


# click on un save
drive.find_element(By.XPATH,"//body[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/div[7]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
time.sleep(5)
