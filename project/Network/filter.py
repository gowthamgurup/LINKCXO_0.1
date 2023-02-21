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
time.sleep(2)



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import
#  time
# (//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[6]


drive.refresh()
time.sleep(5)
# click on Network
drive.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/header/div/div/div[2]/div[3]/div[1]/div[2]/h2").click()
time.sleep(5)


# search
drive.find_element(By.XPATH,"(//*[name()='svg'][contains(@class,'MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv')])[4]").click()
time.sleep(5)


# search enter
drive.find_element(By.XPATH,"(//input[contains(@placeholder,'Search...')])[1]").send_keys("Manoj")
time.sleep(5)

# search
drive.find_element(By.XPATH,"(//*[name()='svg'][contains(@class,'MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-r8ihh6')])[2]").click()
time.sleep(5)


#click on filter
drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[5]").click()
time.sleep(2)

# #designation  min drop down
# drive.find_element(By.XPATH,"(//div[@id='demo-simple-select'])[1]").click()
# time.sleep(3)
# # click on option
# drive.find_element(By.XPATH,"//li[normalize-space()='Vice President - Sales & Marketing']").click()
# time.sleep(2)
#
# # company
# drive.find_element(By.XPATH,"(//input[@id='input-with-sx'])[1]").send_keys("exotelent")
# time.sleep(10)
#
# # location
# drive.find_element(By.XPATH,"(//input[@id='input-with-sx'])[2]").send_keys("hsr layout bangaluru")
# time.sleep(2)
#
# # click on reset
# drive.find_element(By.XPATH,"(//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root css-1pi4f66'][normalize-space()='Reset'])[1]").click()
# time.sleep(10)


#designation  min drop down
drive.find_element(By.XPATH,"(//div[@id='demo-simple-select'])[1]").click()
time.sleep(3)
# click on option
drive.find_element(By.XPATH,"//li[normalize-space()='Vice President - Sales & Marketing']").click()
time.sleep(2)

# company
drive.find_element(By.XPATH,"(//input[@id='input-with-sx'])[1]").send_keys("linkcxo")
time.sleep(10)

# location
drive.find_element(By.XPATH,"(//input[@id='input-with-sx'])[2]").send_keys("hsr layout bangaluru")
time.sleep(2)

 #Industry Drop Down radio button
drive.find_element(By.XPATH,"(//div[@id='demo-simple-select'])[2]").click()
time.sleep(2)

# click on option
drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li[10]/div/span").click()
time.sleep(2)

 #function Drop Down radio button
drive.find_element(By.XPATH,"(//div[@id='demo-simple-select'])[3]").click()
time.sleep(2)

# click on option
drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li[13]/div/span").click()
time.sleep(2)

# click on apply
drive.find_element(By.XPATH,"(//button[contains(@class,'MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root css-1pi4f66')][normalize-space()='Apply'])[1]").click()
time.sleep(20)

# not done it is having bug
