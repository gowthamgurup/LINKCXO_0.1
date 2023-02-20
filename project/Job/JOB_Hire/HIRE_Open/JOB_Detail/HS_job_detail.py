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
time.sleep(4)


# Hiring in job
drive.find_element(By.XPATH,"(//div[@class='css-1iegyem'])[2]").click()
time.sleep(20)

# click on see more
drive.find_element(By.XPATH,"(//h5[@class='MuiTypography-root MuiTypography-h5 css-15jga2m'][normalize-space()='See All'])[1]").click()
time.sleep(2)

# job Detail click on job name
drive.find_element(By.XPATH,"//h5s[normalize-space()='Senior Software Engineer']").click()
time.sleep(10)

# #click on view JD
# drive.find_element(By.XPATH,"//div[@class='MuiBox-root css-0']//h2[@class='MuiTypography-root MuiTypography-h2 css-19qx84q'][normalize-space()='View JD']").click()
# time.sleep(20)

# #click on download JD
# drive.find_element(By.XPATH,"//div[@class='MuiBox-root css-0']//h2[@class='MuiTypography-root MuiTypography-h2 css-19qx84q'][normalize-space()='Download JD']").click()
# time.sleep(20)

# done