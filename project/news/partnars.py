from project.Common.initial import *
drive = commonlogin()
time.sleep(2)

# click on rewards
drive.find_element(By.XPATH,"//div[@class='MuiBox-root css-zbtqym']//img[@alt='creditgold']").click()
time.sleep(2)

# click on details
drive.find_element(By.XPATH,"(//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root css-1pi4f66'][normalize-space()='Details'])[1]").click()
time.sleep(2)

drive.refresh()
time.sleep(2)

# # click on
# drive.find_element(By.XPATH,"(//img[@class='MuiCardMedia-root MuiCardMedia-media MuiCardMedia-img css-1aoh6b1'])[1]").click()
# time.sleep(2)

drive.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(5)

# # click on visit web sit
# drive.find_element(By.XPATH,"(//div[@class='css-1jmg9e3'])[1]").click()
# time.sleep(2)


# # switch to new window
# handles = drive.window_handles
# drive.switch_to.window(handles[1])

drive.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(2)

drive.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_UP)
time.sleep(2)



# click on how to earn
drive.find_element(By.XPATH,"//button[normalize-space()='How to earn?']").click()
time.sleep(2)



drive.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(2)

drive.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(2)

drive.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(2)

drive.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(2)

drive.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(2)

drive.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(2)

drive.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(2)

drive.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(2)


#
# # switch to new window
# handles = drive.window_handles
# drive.switch_to.window(handles[0])
#
#
# #
#
# # click on purches
# drive.find_element(By.XPATH,"(//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root css-1pi4f66'][normalize-space()='Purchase Now'])[1]").click()
# time.sleep(2)
#
# # click on drop down
# drive.find_element(By.XPATH,"//select[@id='demo-simple-select']").click()
# time.sleep(2)
#
# # # click on select 1
# # drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div[1]/div/div/div/div[3]/div[4]/div[1]/div/div/div/select/option[1]").click()
# # time.sleep(2)
#
# # click on purchase
# drive.find_element(By.XPATH,"//button[normalize-space()='Purchase']").click()
# time.sleep(2)
#
# # click on ok
# drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div[1]/div/div/div/div/div[2]/div/div/button").click()
# time.sleep(2)






