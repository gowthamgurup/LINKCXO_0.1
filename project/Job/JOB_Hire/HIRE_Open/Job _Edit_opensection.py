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

# click on JOB EDIT
drive.find_element(By.XPATH,"(//button[contains(text(),'Edit')])[2]").click()
time.sleep(20)

#job status drop down
drive.find_element(By.XPATH,"(//div[@id='demo-simple-select'])[1]").click()
time.sleep(2)
# click on option
drive.find_element(By.XPATH,"//li[normalize-space()='Inactive']").click()
time.sleep(5)

# in side job , job title
bday =drive.find_element(By.XPATH,"//div[@class='MuiFormControl-root MuiTextField-root css-15s6nwh']/div/input")
# to select pre data and then we can pass
bday.send_keys(Keys.CONTROL+'a')
time.sleep(1)
bday.send_keys("developer")
time.sleep(2)

# # company
# company=drive.find_element(By.XPATH,"(//input[@id='input-with-sx'])[2]")
# company.send_keys(Keys.CONTROL+'a')
# time.sleep(1)
# company.send_keys("Exo talent")
# time.sleep(2)
#
#  #Industry Drop Down radio button
# drive.find_element(By.XPATH,"(//div[@id='demo-simple-select'])[2]").click()
# time.sleep(1)
#
# #click on opend drop down full form
# act_ind = drive.find_element(By.XPATH,"/html/body/div[3]/div[3]")
#
# #print("act_ind......",act_ind)
#
# # select multipal optation // in this it will unmark
# drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[4]").click()
# time.sleep(1)
# drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[5]").click()
# time.sleep(1)
# drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[8]").click()
# # again i'm select
# drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[2]").click()
# time.sleep(1)
# drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[5]").click()
# time.sleep(1)
# drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[6]").click()
# act_ind.send_keys(Keys.ESCAPE)
#
# #function Drop Down radio button
#
# drive.find_element(By.CSS_SELECTOR,"body > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > main:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > form:nth-child(1) > div:nth-child(5) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)").click()
# time.sleep(2)
#
# #click on opend drop down full form
# act_fun=drive.find_element(By.XPATH,"/html/body/div[3]/div[3]")
#
# # select option now its unmarking
# drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[4]/span").click()
# time.sleep(1)
# drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[6]/span").click()
# time.sleep(1)
# drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[7]/span").click()
# # select option again i'm selecting
# drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[1]/span").click()
# time.sleep(1)
# drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[3]/span").click()
# time.sleep(1)
# drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[5]/span").click()
#
# # passing escape key
# act_fun.send_keys(Keys.ESCAPE)
#
# #salary min drop down
# drive.find_element(By.XPATH,"//body//div//div//div//main//div//div//div//div//div//div//form//div//div//div//div//div//div//div[@role='button'][normalize-space()='50 lacs']").click()
# time.sleep(1)
#
# #click on opend drop down full form
# act_sal1=drive.find_element(By.XPATH,"//ul[@role='listbox']")
#
# #select option
# drive.find_element(By.XPATH,"//li[normalize-space()='70 lacs']").click()
# # passing escape key
# act_sal1.send_keys(Keys.ESCAPE)
#
# #salary Max drop down
# drive.find_element(By.XPATH,"//body//div//div//div//main//div//div//div//div//div//div//form//div//div//div//div//div//div//div[@role='button'][normalize-space()='80 lacs']").click()
# time.sleep(1)
#
# #click on opend drop down full form
# act_sal=drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul")
#
# #select option
# drive.find_element(By.XPATH,"//li[normalize-space()='1 Cr']").click()
# # passing escape key
# act_sal.send_keys(Keys.ESCAPE)
#
# # location
# loc=drive.find_element(By.XPATH,"//body//div//div//div//main//div//div//div//div//div//div//form//div//div//div//div//div//div//input[@value='Hsr layout 5th main 23 cross bangalor']")
# loc.send_keys(Keys.CONTROL+'a')
# loc.send_keys("BTM layout 5th main 23 cross bangalor")
# time.sleep(2)
#
# #job type drop down
# drive.find_element(By.XPATH,"(//div[@id='demo-simple-select'])[6]").click()
# time.sleep(1)
# # click on option
# drive.find_element(By.XPATH,"//li[normalize-space()='Consulting']").click()
# time.sleep(2)
#
# #Experince min drop down
# drive.find_element(By.XPATH,"//body//div//div//div//main//div//div//div//div//div//div//form//div//div//div//div//div//div//div[@role='button'][normalize-space()='10 years']").click()
# time.sleep(1)
#
# #click on opend drop down full form
# act_sal2=drive.find_element(By.XPATH,"//ul[@role='listbox']")
#
# #select option
# drive.find_element(By.XPATH,"//li[normalize-space()='13 years']").click()
# # passing escape key
# act_sal2.send_keys(Keys.ESCAPE)
#
# #Experince max drop down
# drive.find_element(By.XPATH,"//body//div//div//div//main//div//div//div//div//div//div//form//div//div//div//div//div//div//div[@role='button'][normalize-space()='16 years']").click()
# time.sleep(1)
#
# #click on opend drop down full form
# act_sal3=drive.find_element(By.XPATH,"//ul[@role='listbox']")
#
# #select option
# drive.find_element(By.XPATH,"//li[normalize-space()='22 years']").click()
# # passing escape key
# act_sal3.send_keys(Keys.ESCAPE)

# hiring for
drive.find_element(By.XPATH,"(//input[@name='row-radio-buttons-group'])[1]").click()

# qualification
qualification=drive.find_element(By.XPATH,"//*[@id='input-with-sx']")
qualification.send_keys(Keys.CONTROL+'a')
qualification.send_keys("BE,Btac,Mtac")
time.sleep(2)

# SKILL
skill=drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div/div/form/div[12]/div[2]/div/div[1]/div/div/input")
skill.send_keys(Keys.CONTROL+'a')
skill.send_keys("API testing,Web techonology ,manual testing")

time.sleep(2)

# #job detail  edit with text detail
# drive.find_element(By.XPATH,"//div[@class='MuiFormControl-root MuiFormControl-fullWidth MuiTextField-root css-1cqlo4s']/div/textarea").send_keys("Bond/Agreement/Shifts/Certificate submission : No Bond, Day Shift")
# # create button


#job detail edit with document detail
 #  switch to attachment
drive.find_element(By.XPATH,"//span[@class='MuiSwitch-root MuiSwitch-sizeMedium css-1561xr6']").click()
time.sleep(3)
# click on attachment
attach=drive.find_element(By.XPATH,"//input[@id='icon-button-doc']")
print("attach.....",attach)
attach.send_keys("E:/gotham_1.pdf")

time.sleep(5)
# UPDATE button
# drive.find_element(By.XPATH,"(//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root css-1pi4f66'][normalize-space()='Update'])[1]").click()

# done
