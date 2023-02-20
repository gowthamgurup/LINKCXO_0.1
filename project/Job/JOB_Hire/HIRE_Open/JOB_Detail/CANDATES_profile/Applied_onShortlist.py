from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

from project.Common.initial import *
drive = commonlogin()
time.sleep(6)


# job in home page
drive.find_element(By.XPATH,"//*[@id='root']/div[1]/div/header/div/div/div[2]/div[3]/div[2]").click()
time.sleep(4)


# Hiring in job
drive.find_element(By.XPATH,"(//div[@class='css-1iegyem'])[2]").click()
time.sleep(20)

# # click on see more
# drive.find_element(By.XPATH,"(//h5[@class='MuiTypography-root MuiTypography-h5 css-15jga2m'][normalize-space()='See All'])[1]").click()
# time.sleep(10)

# job Detail click on job name
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[3]/div/div[2]/div/div[3]/div/div[1]/div[1]/span[1]").click()
time.sleep(10)

handles = drive.window_handles
drive.switch_to.window(handles[1])
time.sleep(3)

#scroll up it reach to applied section
element = drive.find_element(By.XPATH,"(//div[@class='css-7dckhh'])[2]")
actions = ActionChains(drive)
actions.move_to_element(element).perform()
time.sleep(10)
print("just before.....")


# click on candidate profile in applied section in that hold section
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div[2]/div[2]/div/div[1]/div/div[1]").click()
time.sleep(10)


# switch to new window
handles = drive.window_handles
drive.switch_to.window(handles[2])
time.sleep(10)


# # click on download resume
# drive.find_element(By.XPATH,"//div[@class='MuiBox-root css-0']//h2[@class='MuiTypography-root MuiTypography-h2 css-19qx84q'][normalize-space()='Download Resume']").click()
# time.sleep(20)

#  massage text here
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div/div/div/div[4]/div[4]/div/p/div/div[1]/div[2]/div/textarea[1]").send_keys("A paragraph is basically a group of at least three to five sentences that discuss a central topic. An effective paragraph always begins with the topic sentence that supports the main idea of the entire paragraph.")
time.sleep(5)
# click on send
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div/div/div/div[4]/div[4]/div/p/div/div[2]/div/button").click()
time.sleep(3)

# About candidate
drive.find_element(By.XPATH,"//div[@class='MuiBox-root css-0']//h2[@class='MuiTypography-root MuiTypography-h2 css-19qx84q'][normalize-space()='About']").click()
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
time.sleep(2)

# switch to new window
handles = drive.window_handles
drive.switch_to.window(handles[1])
time.sleep(10)


#scroll up it reach to applied section
element = drive.find_element(By.XPATH,"//body/div[@id='root']/div[@class='MuiBox-root css-216mb9']/div[@class='wrapper_home']/main/div[@class='wrapper_inner']/div[@class='MuiBox-root css-0']/div[@class='MuiBox-root css-mro3c9']/div[1]")
actions = ActionChains(drive)
actions.move_to_element(element).perform()
time.sleep(10)


# after check that candidate profile than we make  hold or short list or  reject

# ##  click on hold  button
# drive.find_element(By.XPATH,"(//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root css-8j296x'][normalize-space()='Hold'])[2]").click()
# time.sleep(1)
#
# ##  it will scroll to the hold  section
# drive.find_element(By.XPATH,"(//div[@class='MuiGrid-root MuiGrid-container css-1d3bbye'])[4]").click()
# time.sleep(10)
# #
#
# # click on short list in hold section
# drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div[2]/div[6]/div/div/div/div[2]/div[3]/div/div[1]/button").click()
# time.sleep(10)
# #


# #click on rejact in shortlist
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div[2]/div[4]/div/div/div/div[2]/div[3]/div/div[2]/button").click()
time.sleep(10)

##  click on undo button in reject section
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div[2]/div[8]/div/div/div/div[2]/div[3]/div/div/button").click()
time.sleep(10)

##  click on hold  button from shortlist
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div[2]/div[4]/div/div/div/div[2]/div[3]/div/div[1]/button").click()
time.sleep(10)


##  click on hold  button from shortlist
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div[2]/div[6]/div").click()
time.sleep(10)



# # done
