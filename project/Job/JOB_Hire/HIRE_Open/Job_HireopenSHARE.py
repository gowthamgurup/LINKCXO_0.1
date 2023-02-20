from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

from project.Common.initial import *
drive = commonlogin()

# job in home page
drive.find_element(By.XPATH,"//*[@id='root']/div[1]/div/header/div/div/div[2]/div[3]/div[2]").click()
time.sleep(2)

# Hiring in job
drive.find_element(By.XPATH,"(//div[@class='css-1iegyem'])[2]").click()
time.sleep(2)

drive.refresh()
time.sleep(15)

# open 1 one share
drive.find_element(By.XPATH,"(//button[contains(text(),'Share')])[1]").click()
time.sleep(9)

# in that share click on img
drive.find_element(By.XPATH,"(//img[@alt='logo'])[2]").click()
time.sleep(7)

# than click on drop down
drive.find_element(By.XPATH,"//div[@id='demo-simple-select']").click()
time.sleep(8)


#click on opend drop down full form
act_invite = drive.find_element(By.XPATH,"(//ul[@role='listbox'])[1]")

#select a option
drive.find_element(By.XPATH,"//li[2]//span[1]//input[1]").click()
time.sleep(4)  #now  not getting any option


act_invite.send_keys(Keys.ESCAPE)



#click on share button
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/button").click()

#AFTER SELECTION OPTATION  IT WILL WORK

