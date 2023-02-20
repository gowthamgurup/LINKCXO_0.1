from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
import time
drive=webdriver.Chrome(r"C:\Users\Gowtham p\Downloads\chromedriver_win32\chromedriver.exe")
url=r"http://linkcxo-frontend-testing.s3-website.ap-south-1.amazonaws.com"
drive.get(url)
drive.maximize_window()
time.sleep(3)

# About us
drive.find_element(By.LINK_TEXT,"About Us").click()
time.sleep(2)

#scroll up it reach to applied section
element = drive.find_element(By.XPATH,"/html/body/div/div/div[3]")
actions = ActionChains(drive)
actions.move_to_element(element).perform()
time.sleep(2)

element = drive.find_element(By.XPATH,"/html/body/div/div/div[4]/div/div[2]")
actions = ActionChains(drive)
actions.move_to_element(element).perform()
time.sleep(2)

element = drive.find_element(By.XPATH,"/html/body/div/div/div[4]/div/div[4]")
actions = ActionChains(drive)
actions.move_to_element(element).perform()
time.sleep(2)

element = drive.find_element(By.XPATH,"/html/body/div/div/div[6]/div/div/div[1]")
actions = ActionChains(drive)
actions.move_to_element(element).perform()
time.sleep(2)

# click on home
drive.find_element(By.XPATH,"/html/body/div/div/div[1]/div/header/div/div[2]/a/img").click()
time.sleep(2)
# job
drive.find_element(By.LINK_TEXT,"Jobs").click()
time.sleep(2)

# to click right arrow
drive.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div[13]/div/div/div[2]/div/div/button[1]/img").click()
time.sleep(4)

# to click right arrow
drive.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div[13]/div/div/div[2]/div/div/button[1]/img").click()
time.sleep(4)

# to click right arrow
drive.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div[13]/div/div/div[2]/div/div/button[1]/img").click()
time.sleep(4)
#

# # to click right arrow
# drive.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div[13]/div/div/div[2]/div/div/button[1]/img").click()
# time.sleep(4)
# # to click right arrow
# drive.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div[13]/div/div/div[2]/div/div/button[2]/img").click()
# time.sleep(4)
#
# # to click right arrow
# drive.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div[13]/div/div/div[2]/div/div/button[2]/img").click()
# time.sleep(4)
#
# # to click right arrow
# drive.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div[13]/div/div/div[2]/div/div/button[2]/img").click()
# time.sleep(4)
#
# # to click right arrow
# drive.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div[13]/div/div/div[2]/div/div/button[2]/img").click()
# time.sleep(4)
#
# # to click right arrow
# drive.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div[13]/div/div/div[2]/div/div/button[2]/img").click()
# time.sleep(2)
#
# # to click right arrow
# drive.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div[13]/div/div/div[2]/div/div/button[2]/img").click()
# time.sleep(2)


# click on details button
drive.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div[13]/div/div/div[2]/div/div/ul/li[6]/div/div/div[3]/button").click()
time.sleep(5)

# in side details click on apply button
drive.find_element(By.XPATH,"//*[@id='no-padding']/div[2]/div/div/div[4]/div/a/button").click()
time.sleep(2)

# phone number
drive.find_element(By.ID,"outlined-basic").send_keys("7483331671")
time.sleep(2)

# click on arrow
drive.find_element(By.XPATH,"//div[@class='jss10 MuiBox-root css-0']/button").click()
time.sleep(50)

# ##otp box
# drive.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/form/div[1]/div/div[1]/input").send_keys("198989")
# drive.implicitly_wait(2)


# click on verify
drive.find_element(By.XPATH,"//div[@class='css-1t62lt9']/button").click()
time.sleep(30)

# #scroll up it reach to applied section
# element1 = drive.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div/div[9]")
# actions1 = ActionChains(drive)
# actions1.move_to_element(element).perform()
# time.sleep(2)


# click on save job
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div[1]/div/div[2]/div/div/div/div/div[9]/div[2]/div[1]/div/button").click()
time.sleep(8)

#  # share button
# drive.find_element(By.XPATH,"//*[@id='jobdetails']/div/div[2]/div/div/div/div/div[9]/div[2]/div[3]/div/button").click()
# time.sleep(2)
#
# # in that share click on img
# drive.find_element(By.XPATH,"(//img[@alt='logo'])[2]").click()
# time.sleep(2)
#
# # than click on drop down
# drive.find_element(By.XPATH,"//div[@id='demo-simple-select']").click()
# time.sleep(2)
#
#
# #click on opend drop down full form
# act_fun=drive.find_element(By.XPATH,"/html/body/div[3]/div[3]")
#
#
# #select a option
# drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li[2]").click()
# time.sleep(2)  #now  not getting any option
# # drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li[3]/span[1]/input").click()
# # time.sleep(2)
# # drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li[4]/span[1]/input").click()
# # time.sleep(2)
#
# # passing escape key
# act_fun.send_keys(Keys.ESCAPE)
#
#
# #click on share button
# drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/button").click()
# time.sleep(8)


# # than click on * to close share
#
# # than click on * to close share
# drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-m4t9js'])[1]").click()
# time.sleep(3)
#
# drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-m4t9js'])[1]").click()
# time.sleep(2)

# still share drop down is not working
# but next apply button is performing


# job apply
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div[1]/div/div[2]/div/div/div/div/div[9]/div[2]/div[2]/div/button").click()
time.sleep(2)

# Write to the Hiring Manager text field
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div/form/div/div[3]/div/div/textarea[1]").send_keys("fresher need to find job in link cxo ")
time.sleep(2)

# click on attchment
drive.find_element(By.XPATH,"//input[@id='icon-button-doc']").send_keys("E:/gotham_1.pdf")
time.sleep(2)

# apply button
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div/form/div/div[4]/div[2]/div/button").click()
time.sleep(10)

# #scroll up it reach to applied section
# element = drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[3]/div/div[5]/div/div")
# actions = ActionChains(drive)
# actions.move_to_element(element).perform()
# time.sleep(8)


drive.refresh()
time.sleep(5)
#click on 3 dot
dots=drive.find_element(By.XPATH,"//div[@class='MuiCardHeader-root css-qwqjve']/div/div/button")
print("dots......",dots)
dots.click()
time.sleep(5)

# click on report
drive.find_element(By.XPATH,"//span[normalize-space()='Report']").click()
time.sleep(5)

# write here
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div[2]/div/div/textarea[1]").send_keys("Search Ai Certification Course Online, Top Information From Trusted Internet Sources. Ai Certification Course Online, Get Expert Advice and Curated Content on Searchley.")
time.sleep(5)

# click on subbmit button
drive.find_element(By.XPATH,"(//button[normalize-space()='Submit'])[1]").click()
time.sleep(5)



# click on job name
drive.find_element(By.XPATH,"//*[@id='recommended']/div[4]/div/div/div/div[1]/div[1]/span[1]/div/h5s").click()
time.sleep(10)

# switch to the window
handles = drive.window_handles
print(handles)
drive.switch_to.window(handles[1])

# massage text here
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div[2]/div[1]/div[2]/div/textarea[1]").send_keys("A paragraph is basically a group of at least three to five sentences that discuss a central topic. An effective paragraph always begins with the topic sentence that supports the main idea of the entire paragraph.")
time.sleep(5)

# click on send
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div[2]/div[2]/div/button").click()
time.sleep(10)


# click on delet
drive.find_element(By.XPATH,"//div[@class='MuiBox-root css-0']//div[@class='MuiBox-root css-1v3caum']//div[@class='MuiBox-root css-1y7nw8f']//*[name()='svg']").click()
time.sleep(5)

# share button
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div[1]/div/div[2]/div/div/div/div/div[9]/div[2]/div[2]/div/button").click()
time.sleep(2)

# in that share click on img
drive.find_element(By.XPATH,"(//img[@alt='logo'])[2]").click()
time.sleep(2)
#
# than click on drop down
drive.find_element(By.XPATH,"//div[@id='demo-simple-select']").click()
time.sleep(2)
#


# #select a option
# drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li[2]").click()
# time.sleep(2)  #now  not getting any option
#



#click on opend drop down full form
act_fun=drive.find_element(By.XPATH,"/html/body/div[3]/div[3]")


#select a option
drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li[2]").click()
time.sleep(2)  #now  not getting any option
drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li[3]/span[1]/input").click()
time.sleep(2)
drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li[4]/span[1]/input").click()
time.sleep(2)

# passing escape key
act_fun.send_keys(Keys.ESCAPE)

#click on share button
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/button").click()
time.sleep(5)
# click on withdrow button
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div[1]/div/div[2]/div/div/div/div/div[9]/div[2]/div[1]/div/button").click()
time.sleep(10)

# drive.back()
# time.sleep(5)

# click on save
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div[1]/div/div[2]/div/div/div/div/div[9]/div[2]/div[1]/div/button").click()
time.sleep(5)

#scroll up it reach to applied section
element = drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div[2]/div[1]/div/div")
actions = ActionChains(drive)
actions.move_to_element(element).perform()



# till home page it will reach  done




