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



drive.refresh()
time.sleep(20)

# job in home page
drive.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/header/div/div/div[2]/div[3]/div[2]/div[2]/h2").click()
time.sleep(2)




#click on filter
drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[5]").click()
time.sleep(2)

#salary min drop down
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div").click()
time.sleep(3)
# click on option
drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li[1]").click()
time.sleep(2)

#salary max drop down
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div").click()
time.sleep(3)
# click on option
drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li[7]").click()
time.sleep(2)

# location
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[1]/div/div/div/div/form/div/div/div[2]/div[2]/div/div[1]/div/div/input").send_keys("hsr layout bangaluru")
time.sleep(2)

# click on reset
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[1]/div/div/div/div/form/div/div/div[6]/div[1]/div/button").click()
time.sleep(2)





#salary min drop down
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div").click()
time.sleep(3)
# click on option
drive.find_element(By.XPATH,"//li[normalize-space()='50 lacs']").click()
time.sleep(2)

#salary min drop down
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div").click()
time.sleep(3)
# click on option
drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li[7]").click()
time.sleep(2)

# location
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[1]/div/div/div/div/form/div/div/div[2]/div[2]/div/div[1]/div/div/input").send_keys("hsr layout")
time.sleep(2)

#Experience min drop down
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[1]/div/div/div/div/form/div/div/div[3]/div[2]/div[2]/div[1]/div/div/div").click()
time.sleep(3)
# click on option
drive.find_element(By.XPATH,"//li[normalize-space()='10 years']").click()
time.sleep(2)

#Experience max drop down
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[1]/div/div/div/div/form/div/div/div[3]/div[2]/div[2]/div[2]/div/div/div").click()
time.sleep(3)





# # 1 way to scrol
#
# # click on down word
# c = 10
# while c:
#     drive.find_element(By.XPATH,"//div[@id='menu-']//div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']").send_keys(Keys.ARROW_DOWN)
#     time.sleep(1)
#     c = c - 1
# time.sleep(2)

# second way to scroll
#
# for i in range(20):  # adjust integer value for need
#     # you can change right side number for scroll convenience or destination
#     drive.execute_script("window.scrollBy(0, 250)")
#     # you can change time integer to float or remove
#     time.sleep(1)

# click on option
drive.find_element(By.XPATH,"//li[normalize-space()='20 years']").click()
time.sleep(2)

 #Industry Drop Down radio button
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[1]/div/div/div/div/form/div/div/div[4]/div[2]/div/div/div").click()
time.sleep(2)

# click on option
drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li[10]/div/span").click()
time.sleep(2)

 #function Drop Down radio button
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[1]/div/div/div/div/form/div/div/div[5]/div[2]/div/div/div").click()
time.sleep(2)

# click on option
drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li[13]/div/span").click()
time.sleep(2)

# click on apply
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[1]/div/div/div/div/form/div/div/div[6]/div[2]/div/button").click()
time.sleep(20)


# click on job name
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div/div/div/div/div[1]/div[1]/span[1]/div/h5s").click()
time.sleep(5)



# switch to new window
handles = drive.window_handles
drive.switch_to.window(handles[1])
time.sleep(5)


# taking too much loding time



#scroll up it reach to applied section
element = drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div[2]/div[1]")
actions = ActionChains(drive)
actions.move_to_element(element).perform()
time.sleep(10)

# job apply
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div[1]/div/div[2]/div/div/div/div/div[9]/div[2]/div[2]/div/button").click()
time.sleep(2)

# Write to the Hiring Manager text field
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div/form/div/div[3]/div/div/textarea[1]").send_keys("fresher need to find job in link cxo ")
time.sleep(2)

# click on attchment
drive.find_element(By.XPATH,"//input[@id='icon-button-doc']").send_keys("C:/Users/GOWTHAM/Downloads/sample pdf.pdf")
time.sleep(2)

 # apply button
check=drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div/form/div/div[4]/div[2]/div/button")
print("check......click on apply button:",check)
check.click()
time.sleep(30)



# job apply card is not get close after  click on apply button