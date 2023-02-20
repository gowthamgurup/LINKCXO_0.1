
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
time.sleep(10)


#scroll up it reach to applied section
element = drive.find_element(By.XPATH,"(//div[@class='css-7dckhh'])[3]")
actions = ActionChains(drive)
actions.move_to_element(element).perform()
time.sleep(10)


#click on 3 dot
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[3]/div/div[4]/div/div[1]/div/div[1]/div[2]/div/button").click()
time.sleep(5)

# click on report
drive.find_element(By.XPATH,"//span[normalize-space()='Report']").click()
time.sleep(5)


# bug is there need to fix

# write here
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div[2]/div/div/textarea[1]").send_keys("Search Ai Certification Course Online, Top Information From Trusted Internet Sources. Ai Certification Course Online, Get Expert Advice and Curated Content on Searchley.")
time.sleep(5)


# click on subbmit button
drive.find_element(By.XPATH,"(//button[normalize-space()='Submit'])[1]").click()
time.sleep(5)


# click on job name
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[3]/div/div[4]/div/div[1]/div/div[1]/div[1]/span[1]/div/h5s").click()
time.sleep(5)
#

# drive.refresh()
# time.sleep(20)

# switch to new window
handles = drive.window_handles
drive.switch_to.window(handles[1])
time.sleep(5)

#scroll up it reach to msg
element = drive.find_element(By.XPATH,"(//div[@class='MuiBox-root css-naw2yn'])[1]")
actions = ActionChains(drive)
actions.move_to_element(element).perform()
time.sleep(10)


#  massage text here
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div[2]/div[1]/div[2]/div/textarea[1]").send_keys("A paragraph is basically a group of at least three to five sentences that discuss a central topic. An effective paragraph always begins with the topic sentence that supports the main idea of the entire paragraph.")
time.sleep(5)

# click on send   /html/body/div[1]/div[2]/div/main/div/div[1]/div[2]/div[2]/div/button
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div[2]/div[2]/div/button").click()
time.sleep(5)

# share button
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div[1]/div/div[2]/div/div/div/div/div[9]/div[2]/div[2]/div/button").click()
time.sleep(2)

# in that share click on img
drive.find_element(By.XPATH,"(//img[@alt='logo'])[2]").click()
time.sleep(2)

# than click on drop down
drive.find_element(By.XPATH,"//div[@id='demo-simple-select']").click()
time.sleep(2)
#click on opend drop down full form
act_invite = drive.find_element(By.XPATH,"(//ul[@role='listbox'])[1]")

#select a option
drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li[2]").click()
time.sleep(5)
act_invite.send_keys(Keys.ESCAPE)



#click on share button
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/button").click()
time.sleep(5)

# click on withdrow button
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div[1]/div/div[2]/div/div/div/div/div[9]/div[2]/div[1]/div/button").click()
time.sleep(20)




#  not done its having bug
