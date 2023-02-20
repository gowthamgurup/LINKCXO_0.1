from project.Common.initial import *
drive = commonlogin()
time.sleep(2)

# Event in home page
drive.find_element(By.XPATH,"//div[@class='MuiBox-root css-bxbpje']//div[3]").click()
time.sleep(10)

# # click on  Event img for cancle event
# drive.find_element(By.XPATH,"//span[normalize-space()='Cancel this event']").click()
# time.sleep(2)

# click on event img
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[2]/div/div[1]/div/div[1]/div/div/div[2]/div/div/div[1]/div/img").click()
time.sleep(10)

# click on 3 dot
drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[4]").click()
time.sleep(2)





# click on manage invitation
drive.find_element(By.XPATH,"//span[normalize-space()='Manage Invitations']").click()
time.sleep(10)


# # click on accept
# drive.find_element(By.XPATH,"(//button[contains(text(),'Accept')])[1]").click()
# time.sleep(10)
#
# # click on ignor
# drive.find_element(By.XPATH,"(//button[contains(text(),'Ignore')])[2]").click()
# time.sleep(5)


# click on invited
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[1]/div/button[2]/div/h5[1]").click()
time.sleep(5)

# click on attending
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[1]/div/button[3]/div/div/h5[1]").click()
time.sleep(5)


## elem =drive.find_element(By.XPATH,"(//button[contains(text(),'Accept')])[1]")
## if elem.is_displayed():
##     elem.click() # this will click the element if it is there
##     print("FOUND THE LINK CREATE ACTIVITY! and Clicked it!")
## except NoSuchElementException:
##     print("..."):






drive.back()
time.sleep(5)

# # click on copy link
# drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div/div[2]/div[5]/div/div[2]/div/div[1]/button").click()
# time.sleep(5)

# click on copy link after cancle the event
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div/div[2]/div[6]/div/div[2]/div/div[1]/button").click()
time.sleep(5)



# # click on join
# drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div/div[2]/div[5]/div/div[2]/div/div[2]/button").click()
# time.sleep(5)


# click on join after cancel the event
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div/div[2]/div[6]/div/div[2]/div/div[2]/button").click()
time.sleep(5)



# # click on 3 dot
# drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[4]").click()
# time.sleep(2)

# # click on cancle event
# drive.find_element(By.XPATH,"//span[normalize-space()='Cancel this event']").click()
# time.sleep(10)