



from project.Common.initial import *
drive = commonlogin()
time.sleep(5)


# click on Network
drive.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/header/div/div/div[2]/div[3]/div[1]/div[2]/h2").click()
time.sleep(10)

# click on search
drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[4]").click()
time.sleep(5)

# write or search an friends
drive.find_element(By.XPATH,"//input[@placeholder='Search...']").send_keys("prabhat")
time.sleep(1)

# click on search
drive.find_element(By.XPATH,"//div[@class='MuiBox-root css-vrldor']//button[@type='button']").click()
time.sleep(5)

# click connect
drive.find_element(By.XPATH,"(//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root css-1wqdewz'][normalize-space()='Connect'])[1]").click()
time.sleep(5)




