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
drive.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/header/div/div/div[2]/div[3]/div[2]/div[2]/h2").click()
time.sleep(2)

# Hiring in job
drive.find_element(By.XPATH,"(//div[@class='css-1iegyem'])[2]").click()
time.sleep(2)


# creat job
drive.find_element(By.XPATH,"(//div[@class='css-1iegyem'])[3]").click()
time.sleep(2)

# in side job , job title
drive.find_element(By.XPATH,"//div[@class='MuiFormControl-root MuiTextField-root css-15s6nwh']/div/input").send_keys("Software Test Engineer")
time.sleep(2)

# company
drive.find_element(By.XPATH,"//form/div[2]/div/div/div/div/div/div/input").send_keys("linkcxo")
time.sleep(2)

 #Industry Drop Down radio button
drive.find_element(By.XPATH,"//*[@id='root']/div[2]/div/main/div/div/div[2]/div/div/div/form/div[3]/div[2]/div/div").click()
time.sleep(5)

#click on opend drop down full form
act_ind = drive.find_element(By.XPATH,"/html/body/div[3]/div[3]")


#print("act_ind......",act_ind)

# selection multipal optation
# drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[4]").click()
# time.sleep(1)
drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[2]").click()
time.sleep(1)
drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[3]").click()
act_ind.send_keys(Keys.ESCAPE)

#function Drop Down radio button

drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div/div/form/div[4]/div[2]/div").click()
time.sleep(10)

#click on opend drop down full form
act_fun=drive.find_element(By.XPATH,"/html/body/div[3]/div[3]")

# select option
drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[1]/span").click()
time.sleep(1)
drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[3]/span").click()
time.sleep(1)
drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[4]/span").click()
# passing escape key
act_fun.send_keys(Keys.ESCAPE)

#salary min drop down
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div/div/form/div[5]/div[2]/div[2]/div[1]/div/div/div").click()
time.sleep(5)

#click on opend drop down full form
act_sal=drive.find_element(By.XPATH,"//*[@id='menu-']/div[3]")

#select option
drive.find_element(By.XPATH,"//li[normalize-space()='50 lacs']").click()
# passing escape key
act_sal.send_keys(Keys.ESCAPE)

#salary Max drop down
drive.find_element(By.XPATH,"//body[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[5]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]").click()
time.sleep(5)

#click on opend drop down full form
act_sal=drive.find_element(By.XPATH,"/html/body/div[3]/div[3]")

#select option
drive.find_element(By.XPATH,"//li[normalize-space()='80 lacs']").click()
# passing escape key
act_sal.send_keys(Keys.ESCAPE)

# location
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div/div/form/div[6]/div[2]/div/div[1]/div/div/input").send_keys("Hsr layout 5th main 23 cross .parangi palya near hanuman temple bangalor")
time.sleep(2)

#job type drop down
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div/div/form/div[7]/div[2]/div/div/div").click()
time.sleep(3)
# click on option
drive.find_element(By.XPATH,"//div[@class='MuiModal-root MuiPopover-root MuiMenu-root css-1sucic7']//div/ul/li[3]").click()
time.sleep(2)

#Experince min drop down
drive.find_element(By.XPATH,"//body[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[8]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]").click()
time.sleep(1)

#click on opend drop down full form
act_sal=drive.find_element(By.XPATH,"//div[@id='menu-']//div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']")

#select option
drive.find_element(By.XPATH,"//li[normalize-space()='10 years']").click()
# passing escape key
act_sal.send_keys(Keys.ESCAPE)

#Experince max drop down
drive.find_element(By.XPATH,"//body[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[8]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]").click()
time.sleep(1)

#click on opend drop down full form
act_sal=drive.find_element(By.XPATH,"(//div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx'])[2]")

#select option
drive.find_element(By.XPATH,"//div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[8]").click()
# passing escape key
act_sal.send_keys(Keys.ESCAPE)

# hiring for
drive.find_element(By.XPATH,"(//input[@name='row-radio-buttons-group'])[2]").click()

# qualification
drive.find_element(By.XPATH,"//body[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[10]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]").send_keys("MBA,BCA,MCA,BAC,Excepe MECANICAL")
time.sleep(2)
# SKILL
drive.find_element(By.XPATH,"(//input[@type='text'])[6]").send_keys("Java ,Python,spl,Manual,selenium")
time.sleep(2)

#job detail
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div/div/form/div[14]/div[2]/div/div/div/textarea[1]").send_keys("Bond/Agreement/Shifts/Certificate submission : No Bond, Day Shift")
time.sleep(2)

# create button
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div/div/form/div[15]/div/button").click()
time.sleep(20)

# DONE