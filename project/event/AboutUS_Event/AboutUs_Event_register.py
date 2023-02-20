from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.devtools.v104 import browser
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
import time


drive=webdriver.Chrome(r"C:\Users\Gowtham p\Downloads\chromedriver_win32\chromedriver.exe")
url=r"http://linkcxo-frontend-testing.s3-website.ap-south-1.amazonaws.com"
drive.get(url)
drive.maximize_window()
time.sleep(5)

# click on home
drive.find_element(By.XPATH,"/html/body/div/div/div[1]/div/header/div/div[2]/a/img").click()
time.sleep(10)

# # click on partnear
# drive.find_element(By.CSS_SELECTOR,"body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > header:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(4)").click()
# time.sleep(2)



# click on corporat B2B
drive.find_element(By.XPATH,"//a[normalize-space()='Corporate B2B']").click()
time.sleep(10)



# click on partnear
drive.find_element(By.CSS_SELECTOR,"body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > header:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(4)").click()
time.sleep(2)

# click on content
drive.find_element(By.XPATH,"//li[normalize-space()='Content']").click()
time.sleep(10)


# click on partnear
drive.find_element(By.CSS_SELECTOR,"body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > header:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(4)").click()
time.sleep(2)


# click on brand
drive.find_element(By.XPATH,"//li[normalize-space()='Brand']").click()
time.sleep(1)

# click on partnear
drive.find_element(By.CSS_SELECTOR,"body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > header:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(4)").click()
time.sleep(2)

# click on event
drive.find_element(By.XPATH,"//li[normalize-space()='Event']").click()
time.sleep(1)

# scroll up which we given
element = drive.find_element(By.XPATH,"//div[contains(@class,'nl-footer row')]")
actions = ActionChains(drive)
actions.move_to_element(element).perform()


# frist name
drive.find_element(By.XPATH,"//input[@placeholder='First Name*']").send_keys("gowtham")
time.sleep(1)

# last name
drive.find_element(By.XPATH,"//input[@placeholder='Last Name*']").send_keys("p")
time.sleep(1)

# Email
drive.find_element(By.XPATH,"//input[@placeholder='Email ID*']").send_keys("gowthampl94@gmail.com")
time.sleep(1)

# mobile number
drive.find_element(By.XPATH,"//input[@placeholder='Mobile No*']").send_keys("8494842743")
time.sleep(1)

#company
drive.find_element(By.XPATH,"//input[@placeholder='Company*']").send_keys("linkcxo")
time.sleep(1)

# write here
drive.find_element(By.XPATH,"//textarea[@placeholder='Write here...']").send_keys("Together we can do so much, Success is when it is shared. Partner with us now to achieve more!")
time.sleep(5)

# submit
drive.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(10)

# alart click on (ok)
# Alert(drive).accept()
# time.sleep(10)
# another way

alert = Alert(drive)
# get alert text
print(alert.text)
# accept the alert
alert.accept()

time.sleep(20)
# Not  complet  bcoz bug is there







