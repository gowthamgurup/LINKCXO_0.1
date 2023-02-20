from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time
drive=webdriver.Chrome(r"C:\Users\Gowtham p\Downloads\chromedriver_win32\chromedriver.exe")
url=r"http://linkcxo-frontend-testing.s3-website.ap-south-1.amazonaws.com"
drive.get(url)
drive.maximize_window()
time.sleep(5)

# About us
drive.find_element(By.LINK_TEXT,"About Us").click()
time.sleep(2)
element = drive.find_element(By.XPATH,"//div[@class='nl-footer row']")
actions = ActionChains(drive)
actions.move_to_element(element).perform()
#home
drive.find_element(By.XPATH,"/html/body/div/div/div[1]/div/header/div/div[2]/a/img").click()
time.sleep(10)

# job
drive.find_element(By.LINK_TEXT,"Jobs").click()
time.sleep(5)

# click on arrow
arrow=drive.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div[13]/div/div/div[2]/div/div/button[1]/img")
print("arrow......",arrow)
arrow.click()
time.sleep(2)

# click on arrow
arrow1=drive.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div[13]/div/div/div[2]/div/div/button[1]/img")
print("arrow1......",arrow1)
arrow1.click()
time.sleep(3)
#
arrow2=drive.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div[13]/div/div/div[2]/div/div/button[1]/img")
print("arrow2......",arrow2)
arrow2.click()
time.sleep(5)


# arrow3=drive.find_element(By.XPATH,"//*[@id='jobs']/div/div[2]/div/div/button[2]/img")
# print("arrow3......",arrow3)
# arrow3.click()
# time.sleep(12)


# click on job apply
drive.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div[13]/div/div/div[2]/div/div/ul/li[6]/div/div/div[3]/a/button").click()
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
time.sleep(8)

# job apply
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div[1]/div/div[2]/div/div/div/div/div[9]/div[2]/div[2]/div/button").click()
time.sleep(2)

# Write to the Hiring Manager text field
drive.find_element(By.XPATH,"//*[@id='mui-1']").send_keys("fresher need to find job in link cxo ")
time.sleep(2)

# click on attchment
drive.find_element(By.XPATH,"//input[@id='icon-button-doc']").send_keys("C:/Users/GOWTHAM/Downloads/img13.jpg")
time.sleep(2)

 # click on   apply
drive.find_element(By.XPATH,"//*[@id='root']/div[2]/div/div/div/div/form/div/div[4]/div[2]/div/button").click()
time.sleep(8)


drive.refresh()
time.sleep(8)

# click on * to close
drive.find_element(By.XPATH,"//*[name()='path' and contains(@d,'M19 6.41 1')]").click()
time.sleep(2)


# type here
drive.find_element(By.XPATH,"//div[@class='MuiInput-root MuiInputBase-root MuiInputBase-colorPrimary MuiInputBase-fullWidth MuiInputBase-formControl MuiInputBase-multiline css-y5jr6g']/textarea").send_keys("fresher need to find job in link cxo ")
time.sleep(2)

# click on submit button
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div[2]/div[2]/div/button").click()
time.sleep(2)


# click on delet
drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-74elj8'])[1]").click()
time.sleep(8)


# share button
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div[1]/div/div[2]/div/div/div/div/div[9]/div[2]/div[2]/div/button").click()
time.sleep(5)


# click on share  image
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/img").click()
time.sleep(2)

# Click on drop down
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div/div").click()
time.sleep(2)

#click on opend drop down full form
act_ind = drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul")

# select optation
drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li[2]/span[1]/input").click()
time.sleep(1)

drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li[3]/span[1]/input").click()

act_ind.send_keys(Keys.ESCAPE)


# click on submit button
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/button").click()
time.sleep(8)

#withdow
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div[1]/div/div[2]/div/div/div/div/div[9]/div[2]/div[1]/div/button").click()

# it will reach to job section done if we continue it will apply the job

