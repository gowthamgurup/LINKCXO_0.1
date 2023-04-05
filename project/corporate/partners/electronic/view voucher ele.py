from project.Common.initial import *
drive = commonlogin()
time.sleep(2)


# clink on corporate
drive.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/header/div/div/div[2]/div[3]/div[4]").click()
time.sleep(2)



#click on corporate membership
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div[1]/div/img").click()
time.sleep(5)

# click on partners
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[1]/div/div/div/button[2]/div/h5[1]").click()
time.sleep(5)

#scroll up it reach
element = drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[2]/div/div/div/div[5]/div/div/div[2]")
actions = ActionChains(drive)
actions.move_to_element(element).perform()
time.sleep(10)

# click on electronic
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[2]/div/div/div/div[5]/div/div/div[1]").click()
time.sleep(2)
#
# click on img to view card
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div/div[1]").click()
time.sleep(5)

# click on view voucher
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[2]/div/div/div/div/div/img").click()
time.sleep(10)

# click on link
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div/div[2]/div/div[3]/div[2]/div[1]/div[3]").click()
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





