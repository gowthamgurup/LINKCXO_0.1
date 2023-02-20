from project.Common.initial import *
drive = commonlogin()
time.sleep(5)


# click on Network
drive.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/header/div/div/div[2]/div[3]/div[1]/div[2]/h2").click()
time.sleep(10)

# click on friend detail,view
drive.find_element(By.XPATH,"(//div[@class='MuiBox-root css-3v5xuz'])[1]").click()
time.sleep(5)


#scroll up it reach to applied section
element = drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div/div/div/div[4]/div[2]/div/p/div[11]/div/div[1]")
actions = ActionChains(drive)
actions.move_to_element(element).perform()

# click on skill
drive.find_element(By.XPATH,"(//div)[139]").click()
time.sleep(5)

# click on interest
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div/div/div/div[4]/div[2]/div/p/div[2]/div/div[1]/div[1]/div").click()
time.sleep(5)

# click on industry
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div/div/div/div[4]/div[2]/div/p/div[3]/div/div[1]/div[1]/div").click()
time.sleep(5)

# click on function
drive.find_element(By.XPATH,"(//div[@class='css-vfjav4'])[4]").click()
time.sleep(5)

# click on Experience
drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[8]").click()
time.sleep(5)

# click on Education
drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[9]").click()
time.sleep(5)

# click on Affiliations
drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[10]").click()
time.sleep(5)

# click on Awards & certification
drive.find_element(By.XPATH,"(//div[@class='css-vfjav4'])[8]").click()
time.sleep(5)

# click on Publaction
drive.find_element(By.XPATH,"(//div[@class='css-vfjav4'])[9]").click()
time.sleep(5)

# click on langauge
drive.find_element(By.XPATH,"(//div[@class='css-vfjav4'])[10]").click()
time.sleep(5)


# click on Addational Information
drive.find_element(By.XPATH,"(//div[@class='css-vfjav4'])[11]").click()
time.sleep(5)

drive.back()
time.sleep(10)

# click on connect  it is in upper side of discover
drive.find_element(By.XPATH,"(//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root css-5jo01e'][normalize-space()='Connect'])[1]").click()
time.sleep(5)


# # click on connect
# drive.find_element(By.XPATH,"(//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root css-5jo01e'][normalize-space()='Connect'])[1]").click()
# time.sleep(8)

# click on Existing
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[1]/div[1]/div[1]/div/button[3]/div/h5[1]").click()
time.sleep(5)

# click on remove
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[1]/div[1]/div[4]/div/div[3]/div/div/div[3]/div/div/button").click()
time.sleep(10)

drive.refresh()
time.sleep(5)


#scroll up it reach to applied section
element = drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div[2]/div/div/div/div[1]/div[3]/div")
actions = ActionChains(drive)
actions.move_to_element(element).perform()
time.sleep(5)


# click on connect
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div[2]/div/div/div/div[1]/div[1]/div/div/div[3]/div/div/button").click()
time.sleep(15)


# click on pending
drive.find_element(By.XPATH,"(//h5[@class='MuiTypography-root MuiTypography-h5 jss4 css-z8bhzf'][normalize-space()='Pending'])[1]").click()
time.sleep(5)




