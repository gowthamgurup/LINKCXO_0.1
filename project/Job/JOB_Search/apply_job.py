from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time


# this is how we call the function in same project in other files
from project.Common.initial import *
drive = commonlogin()
time.sleep(10)

# job in home page
drive.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/header/div/div/div[2]/div[3]/div[2]/div[2]/h2").click()
time.sleep(2)



#click on 3 dot
drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[6]").click()
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



# share button
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[3]/div/div[2]/div/div/div/div[1]/div[1]/div/div[2]/div/div[2]/div[3]/div/button").click()
time.sleep(2)

# in that share click on img
drive.find_element(By.XPATH,"(//img[@alt='logo'])[2]").click()
time.sleep(2)

# then click on drop down
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

# taking too much loding time

# job apply
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[3]/div/div[2]/div/div/div/div[1]/div[1]/div/div[2]/div/div[2]/div[1]/div/button").click()
time.sleep(2)
try:
    # Write to the Hiring Manager text field
    drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div/form/div/div[3]/div/div/textarea[1]").send_keys("fresher need to find job in link cxo ")
    time.sleep(2)

    # click on attchment
    drive.find_element(By.XPATH,"//input[@id='icon-button-doc']").send_keys("C:/Users/GOWTHAM/Downloads/sample pdf.pdf")
    time.sleep(2)

     # apply button
    check=drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div/form/div/div[4]/div[2]/div/button")
    print("check......",check)
    check.click()
    time.sleep(30)


    # drive.refresh()
    # time.sleep(10)
except:

    # click on your plan
    drive.find_element(By.XPATH, "//button[normalize-space()='View Plans']").click()
    time.sleep(5)

    # click on detail reward
    drive.find_element(By.XPATH, "(//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root css-1wqdewz'][normalize-space()='Details'])[2]").click()
    time.sleep(5)

    # scroll up to buy
    element = drive.find_element(By.XPATH, "(//div[@class='MuiBox-root css-1v7j4ud'])[1]")
    actions = ActionChains(drive)
    actions.move_to_element(element).perform()
    time.sleep(3)


    # click on buy
    drive.find_element(By.XPATH,"(//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root css-1pi4f66'][normalize-space()='Buy Now'])[1]").click()
    time.sleep(5)



    alert = Alert(drive)
    print(alert.text)
    alert.accept()

    print("chech your plan")

