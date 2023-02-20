from project.Common.initial import *
drive = commonlogin()
time.sleep(2)

# click on rewards
drive.find_element(By.XPATH,"//div[@class='MuiBox-root css-zbtqym']//img[@alt='creditgold']").click()
time.sleep(5)

# # click on members
# drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[2]/div/div/div/button[1]/div").click()
# time.sleep(5)

#scroll up it reach to applied section till T & C
element = drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[3]/div/div/div/div[5]/div/div/div[1]")
actions = ActionChains(drive)
actions.move_to_element(element).perform()
time.sleep(10)


# click on apperal
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[3]/div/div/div/div[4]/div/div/div[1]").click()
time.sleep(2)

# click on select an option
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[1]/div/div/div[1]").click()
time.sleep(2)

# click on view voucher
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[3]/div/div/div/div/div/img").click()
time.sleep(2)

#scroll up it reach to applied section till T & C
element = drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div/div[2]/div/div[7]")
actions = ActionChains(drive)
actions.move_to_element(element).perform()
time.sleep(10)


# click on link
drive.find_element(By.XPATH,"(//div[@class='css-1fkzjhu'])[1]").click()
time.sleep(10)

# switch to new window
handles = drive.window_handles
drive.switch_to.window(handles[0])
time.sleep(5)

# click on purchse
drive.find_element(By.XPATH,"(//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root css-1pi4f66'][normalize-space()='Purchase Now'])[1]").click()
time.sleep(10)

# click on purchse
drive.find_element(By.XPATH,"(//button[normalize-space()='Purchase'])[1]").click()
time.sleep(10)

# click on ok
drive.find_element(By.XPATH,"//button[normalize-space()='OK']").click()
time.sleep(10)


drive.back()
time.sleep(10)


drive.back()
time.sleep(10)
#
#