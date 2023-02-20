
from project.Common.initial import *
drive = commonlogin()
time.sleep(9)

# Event in home page
drive.find_element(By.XPATH,"//div[@class='MuiBox-root css-bxbpje']//div[3]").click()
time.sleep(10)

# participting

# click on participting
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[1]/div/button[3]/div/div/h5[1]").click()
time.sleep(5)




# #click on see more
# drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[4]/div/div[1]/div/div[1]/div[1]/div/div[2]/h5").click()
# time.sleep(5)


# click on img
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[4]/div/div[1]/div/div[1]/div[2]/div/div[2]/div/div/div[1]/div/img").click()
time.sleep(5)


drive.refresh()
time.sleep(5)

# click on 3 dot
drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[4]").click()
time.sleep(2)

# click on report
drive.find_element(By.XPATH,"//span[normalize-space()='Report']").click()
time.sleep(10)

# select optation
drive.find_element(By.XPATH,"//input[@name='Explicit_Content']").click()
time.sleep(1)
drive.find_element(By.XPATH,"(//input[@name='Harassment'])[1]").click()
time.sleep(1)
drive.find_element(By.XPATH,"//input[@name='False_Information']").click()
time.sleep(1)
drive.find_element(By.XPATH,"//input[@name='Intellectual_Property']").click()
time.sleep(1)


# click on type here
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div[3]/div/div/textarea[1]").send_keys("Some. We use some when there is an unspecified amount. We don’t know (or can’t count) the ")
time.sleep(10)

# click on submit
drive.find_element(By.XPATH,"//button[normalize-space()='Submit']").click()
time.sleep(5)

# # click on 3 dot
# drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[4]").click()
# time.sleep(2)


# #click on with drown
#
# drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div/div[2]/div[4]/div/div/div/button").click()
# time.sleep(50)

drive.refresh()
time.sleep(5)

#click on with drown

drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div/div[2]/div[4]/div/div/div/button").click()
time.sleep(5)


drive.back()
time.sleep(10)

# # scroll up
element = drive.find_element(By.XPATH,"(//div[@class='css-1xhj18k'])[22]")
actions = ActionChains(drive)
actions.move_to_element(element).perform()
time.sleep(5)


#click on  img in past
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[4]/div/div[2]/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div/img").click()
time.sleep(50)