from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
import time

def commonlogin():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.select import Select
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.alert import Alert
    import time

    drive = webdriver.Chrome(r"C:\Users\Gowtham p\Downloads\chromedriver_win32\chromedriver.exe")
    drive.get("http://linkcxo-frontend-testing.s3-website.ap-south-1.amazonaws.com/")
    drive.maximize_window()
    time.sleep(2)

    #  Be a member
    drive.find_element(By.XPATH,"/html/body/div/div/div[1]/div/header/div/div[3]/button/a").click()

    # switch to mail or mobile numver
    # drive.find_element(By.XPATH,"//div/span/span/input").click()

    # phone number
    drive.find_element(By.ID,"outlined-basic").send_keys("9162849798")
    time.sleep(2)

    # click on arrow
    drive.find_element(By.XPATH,"//button[@aria-label='next']//*[name()='svg']").click()
    time.sleep(10)

    ##otp box
    drive.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/form/div[1]/div/div[1]/input").send_keys("198989")
    drive.implicitly_wait(2)

    # click on verify

    drive.find_element(By.XPATH,"//div[@class='css-1t62lt9']/button").click()
    time.sleep(20)
    x = drive.title
    print("The title of the current page is :" + x)

    return drive



