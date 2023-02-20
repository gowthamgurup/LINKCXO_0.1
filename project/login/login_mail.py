from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
drive=webdriver.Chrome(r"C:\Users\Gowtham p\Downloads\chromedriver_win32\chromedriver.exe")
url=r"http://linkcxo-frontend-testing.s3-website.ap-south-1.amazonaws.com"
drive.get(url)
drive.maximize_window()
time.sleep(2)

#  Be a member
drive.find_element(By.XPATH,"/html/body/div/div/div[1]/div/header/div/div[3]/button/a").click()

# switch to mail button
drive.find_element(By.XPATH,"//div/span/span/input").click()
time.sleep(5)
#mail text field
drive.find_element(By.ID,"outlined-basic").send_keys("kprabhat956@gmail.com")
time.sleep(5)

# arrow button
drive.find_element(By.XPATH,"//button[@aria-label='next']//*[name()='svg']").click()
time.sleep(5)

# otp box
drive.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/form/div[1]/div/div[1]/input").send_keys("198989")
time.sleep(2)

#click to verify
drive.find_element(By.XPATH,"//div[@class='css-1t62lt9']/button").click()

#  it reach done