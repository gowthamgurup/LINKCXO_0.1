from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from project.Common.initial import *
drive = commonlogin()
time.sleep(2)

# job in home page
drive.find_element(By.XPATH,"//*[@id='root']/div[1]/div/header/div/div/div[2]/div[3]/div[2]").click()
time.sleep(1)
drive.refresh()
time.sleep(5)

# Hiring in job
drive.find_element(By.XPATH,"(//div[@class='css-1iegyem'])[2]").click()
time.sleep(10)

#  # click on see more
# var=drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div/div/div[3]/div[1]/div[1]/div/div/div[2]/h5")
# print("var.....",var)
# var.click()
# time.sleep(15)

#scroll up it reach to applied section
element = drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[3]/div/div[6]/div/div")
actions = ActionChains(drive)
actions.move_to_element(element).perform()
time.sleep(10)

# # click on see more
# drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[3]/div/div[6]/div/div/div[2]/h5").click()
# time.sleep(2)


# job Detail click on job name
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[3]/div/div[6]/div/div[1]/div/div[1]/div[1]/span[1]/div/h5s").click()
time.sleep(15)

# switch to new window
handles = drive.window_handles
drive.switch_to.window(handles[1])
time.sleep(5)

#scroll up it reach to applied section
var1=element1 = drive.find_element(By.XPATH,"(//div)[205]")
print("var1.....", var1)
actions2 = ActionChains(drive)
actions2.move_to_element(element1).perform()
time.sleep(10)





# done