from project.Common.initial import *
drive = commonlogin()
time.sleep(2)

# click on rewards
drive.find_element(By.XPATH,"//div[@class='MuiBox-root css-zbtqym']//img[@alt='creditgold']").click()
time.sleep(5)

# click on members
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[2]/div/div/div/button[1]/div").click()
time.sleep(5)

# click on details lxr50
drive.find_element(By.XPATH,"(//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root css-1wqdewz'][normalize-space()='Details'])[2]").click()
time.sleep(2)

#scroll up it reach to applied section
element = drive.find_element(By.XPATH,"(//div[@class='MuiBox-root css-1v7j4ud'])[1]")
actions = ActionChains(drive)
actions.move_to_element(element).perform()
time.sleep(5)

# click on view voucher
drive.find_element(By.XPATH,"(//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root css-1pi4f66'][normalize-space()='Buy Now'])[1]").click()
time.sleep(2)

# qr code is not visibal or payment page is not dispaying
