
from project.Common.initial import *
drive = commonlogin()
time.sleep(9)

# Event in home page
drive.find_element(By.XPATH,"//div[@class='MuiBox-root css-bxbpje']//div[3]").click()
time.sleep(10)


   #PENDING SECTION

#click on pending
drive.find_element(By.XPATH," /html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[1]/div/button[2]/div/h5[1]").click()
time.sleep(5)

# # open 1 one share
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[3]/div/div[1]/div/div[1]/div[2]/div/div/div/div/div[2]/div/div/div/button/div/img").click()
time.sleep(9)

# in that share click on img
drive.find_element(By.XPATH,"(//img[@alt='logo'])[2]").click()
time.sleep(7)

# than click on drop down
drive.find_element(By.XPATH,"//div[@id='demo-simple-select']").click()
time.sleep(8)

#click on opend drop down full form
act_share = drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul")

#select a option
drive.find_element(By.XPATH,"(//input[@type='checkbox'])[1]").click()
time.sleep(2)  #now  not getting any option
drive.find_element(By.XPATH,"(//input[@type='checkbox'])[3]").click()
time.sleep(2)
# drive.find_element(By.XPATH,"(//input[@type='checkbox'])[4]").click()
# time.sleep(2)
act_share.send_keys(Keys.ESCAPE)

#click on share button
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/button").click()
time.sleep(8)

# # click on ignor
# drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[5]").click()
# time.sleep(8)
#
# #click on accept
# drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[4]").click()
# time.sleep(8)


# click on img
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[3]/div/div[1]/div/div[1]/div[2]/div/div[2]/div/div/div[1]/div/img").click()
time.sleep(8)

# #click on event  img in pending
# drive.find_element(By.XPATH,"//*[@id='mui-6-P-1']/div/div[1]/div/div[1]/div[2]/div/div[3]/div/div/div[1]/div/img").click()
# time.sleep(8)

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

# click on ATTEND in side of profile
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/button").click()
time.sleep(5)

drive.back()
time.sleep(5)

# # scroll up which we given requiested
element = drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[3]/div/div[2]/div/div[1]/div[1]/div")
actions = ActionChains(drive)
actions.move_to_element(element).perform()
time.sleep(5)
# click on cancle request
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[3]/div/div[2]/div/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/h6").click()
time.sleep(5)
