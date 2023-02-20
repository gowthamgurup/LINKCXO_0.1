from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
import time

import pytest

# global drive

class TestSample():
    @pytest.fixture()
    def test_setup(self):
        global drive
        drive = webdriver.Chrome(executable_path="C:/Users/Gowtham p/Downloads/chromedriver_win32/chromedriver.exe")
        drive.implicitly_wait(2)
        drive.maximize_window()
        time.sleep(2)
        yield
        drive.close()
        drive.quit()
        print("Test completed")
        time.sleep(20)

    @pytest.fixture()
    def test_login(self,test_setup):
        drive.get("http://linkcxo-frontend-testing.s3-website.ap-south-1.amazonaws.com/")
        #  Be a member
        drive.find_element(By.XPATH,"/html/body/div/div/div[1]/div/header/div/div[3]/button/a").click()
        time.sleep(2)

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
        print("The title of the current page is :"+x)
        assert x == "LinkCxO - Exclusive CxO Networking"
        time.sleep(40)
#    def test_teardown():
    #     drive.close()
    #     drive.quit()
    #     print("Test completed")
    #     time.sleep(20)
    #     return drive
    def test_post(self,test_login):
        drive.refresh()
        time.sleep(5)

        # click on post
        drive.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div/div[3]/button[1]").click()
        time.sleep(5)

        # click on text
        drive.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div[2]/div/div/textarea[1]").send_keys("Lorem Ipsum is simply dummy text of the printing and typesetting industry.")
        time.sleep(2)

        # click on camera and add img
        drive.find_element(By.XPATH, "//input[@id='icon-button-image']").send_keys("C:/Users/GOWTHAM/Downloads/img12.jpg")
        time.sleep(2)

        drive.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_UP)
        time.sleep(5)

        # click on post
        drive.find_element(By.XPATH, "//button[normalize-space()='Post']").click()
        y = drive.title
        print("The title of the current page is :" + y)
        assert y == "LinkCxO - Exclusive CxO Networking"

        time.sleep(30)
