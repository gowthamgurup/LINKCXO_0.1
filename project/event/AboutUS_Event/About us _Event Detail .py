from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
drive=webdriver.Chrome(r"C:\Users\Gowtham p\Downloads\chromedriver_win32\chromedriver.exe")
url=r"http://linkcxo-frontend-testing.s3-website.ap-south-1.amazonaws.com/#events"
drive.get(url)
drive.maximize_window()
time.sleep(5)


# click on home
drive.find_element(By.XPATH,"/html/body/div/div/div[1]/div/header/div/div[2]/a/img").click()
time.sleep(2)

# Event
drive.find_element(By.CSS_SELECTOR,"a[href='/#events']").click()
time.sleep(2)
# arrow button
drive.find_element(By.XPATH,"//button[@class='event-Right-Arrow']").click()
time.sleep(2)

# detail button
drive.find_element(By.CSS_SELECTOR,"li[class='react-multi-carousel-item react-multi-carousel-item--active carousel-item-padding-40-px'] button[class='btn-event-details']").click()
time.sleep(2)
# in that attend button
drive.find_element(By.CSS_SELECTOR,".btn-event-details").click()
time.sleep(2)

#login with
# phone number
drive.find_element(By.ID,"outlined-basic").send_keys("9162849798")
time.sleep(2)

# click on arrow
drive.find_element(By.XPATH,"//button[@aria-label='next']//*[name()='svg']").click()
time.sleep(2)

# otp box
drive.find_element(By.XPATH,"//div[@class='MuiBox-root css-19igzj1']/div/div").click()
drive.implicitly_wait(2)

##otp box
drive.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/form/div[1]/div/div[1]/input").send_keys("198989")
drive.implicitly_wait(2)

# click on verify

drive.find_element(By.XPATH,"//div[@class='css-1t62lt9']/button").click()
time.sleep(30)







# it will reach to the home page done