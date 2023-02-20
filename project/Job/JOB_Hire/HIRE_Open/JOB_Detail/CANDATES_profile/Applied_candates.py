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

# drive.refresh()
# time.sleep(4)

# Hiring in job
drive.find_element(By.XPATH,"(//div[@class='css-1iegyem'])[2]").click()
time.sleep(4)
#
# drive.refresh()
# time.sleep(15)



# job Detail click on job name
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[3]/div/div[2]/div/div[3]/div/div[1]/div[1]/span[1]").click()
time.sleep(4)

# drive.refresh()
# time.sleep(10)


# switch to new window
handles = drive.window_handles
drive.switch_to.window(handles[1])
time.sleep(10)

#scroll up it reach to applied section
element = drive.find_element(By.CSS_SELECTOR,"body > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > main:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)")
actions = ActionChains(drive)
actions.move_to_element(element).perform()
time.sleep(10)

# click on candidate profile in applied section
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div[2]/div[2]/div/div[1]/div/div[1]").click()
time.sleep(10)


# switch to new window
handles = drive.window_handles
drive.switch_to.window(handles[2])
time.sleep(10)

# click on download resume
drive.find_element(By.XPATH,"//div[@class='MuiBox-root css-0']//h2[@class='MuiTypography-root MuiTypography-h2 css-19qx84q'][normalize-space()='Download Resume']").click()
time.sleep(20)
# # massage text here
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div/div/div/div[4]/div[4]/div/p/div/div[1]/div[2]/div/textarea[1]").send_keys("A paragraph is basically a group of at least three to five sentences that discuss a central topic. An effective paragraph always begins with the topic sentence that supports the main idea of the entire paragraph.")
time.sleep(5)

# click on send
drive.find_element(By.XPATH,"(//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root css-1pi4f66'][normalize-space()='Send'])[1]").click()
time.sleep(3)

# delet send text
drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-74elj8'])[1]").click()
time.sleep(5)

# About candidate
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div/div/div/div[4]/div[1]/div/div/button[1]/div/h2").click()
time.sleep(3)

# candidate skill
drive.find_element(By.XPATH,"//body[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/p[1]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
time.sleep(3)
# candidate interests
drive.find_element(By.XPATH,"//body[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/p[1]/div[2]/div[1]/div[1]/div[1]/div[1]").click()
time.sleep(3)

# Industry
drive.find_element(By.XPATH,"//body[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/p[1]/div[3]/div[1]/div[1]").click()
time.sleep(2)
# function
drive.find_element(By.XPATH,"//body[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/p[1]/div[4]/div[1]/div[1]/div[1]/div[1]").click()
time.sleep(2)

# experience
drive.find_element(By.XPATH,"//body[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/p[1]/div[5]/div[1]/div[1]").click()
time.sleep(2)

# education
drive.find_element(By.XPATH,"//body[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/p[1]/div[6]/div[1]/div[1]").click()
time.sleep(2)

# affiliations
drive.find_element(By.XPATH,"//body[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/p[1]/div[7]/div[1]/div[1]").click()
time.sleep(2)

# Awards & certification
drive.find_element(By.XPATH,"//body[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/p[1]/div[8]/div[1]/div[1]/div[1]/div[1]").click()
time.sleep(2)

# publication
drive.find_element(By.XPATH,"//body[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/p[1]/div[9]/div[1]/div[1]/div[1]/div[1]").click()
time.sleep(2)

# langauge
drive.find_element(By.XPATH,"//body[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/p[1]/div[10]/div[1]/div[1]/div[1]/div[1]").click()
time.sleep(2)

# addational information
drive.find_element(By.XPATH,"//body[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/p[1]/div[11]/div[1]/div[1]/div[1]/div[1]").click()
time.sleep(2)
# again clicking
drive.find_element(By.XPATH,"//body[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/p[1]/div[11]/div[1]/div[1]/div[1]/div[1]").click()



# done
