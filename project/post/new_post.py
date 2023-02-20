#

from project.Common.initial import *
drive = commonlogin()
time.sleep(7)

# click on post
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div/div[3]/button[1]").click()
time.sleep(5)

# click on text
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div[2]/div/div/textarea[1]").send_keys("Lorem Ipsum is simply dummy text of the printing and typesetting industry.")
time.sleep(2)

# click on camera and add img
drive.find_element(By.XPATH,"//input[@id='icon-button-image']").send_keys("C:/Users/GOWTHAM/Downloads/img12.jpg")
time.sleep(2)

drive.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_UP)
time.sleep(5)
y = drive.title
print("The title of the current page is :" + y)


# click on post
drive.find_element(By.XPATH,"//button[normalize-space()='Post']").click()
x = drive.title
print("The title of the current page is :" + x)

time.sleep(20)



# click on 3 dot
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div/button").click()
time.sleep(10)

# click on edit
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div/div/div/div/ul/li[1]/div/span").click()
time.sleep(10)


# in side job , job title
bday =drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div[2]/div/div/textarea[1]")
# to select pre data and then we can pass
bday.send_keys(Keys.CONTROL+'a')
time.sleep(1)
bday.send_keys("CHHATTISGARH STATE POWER .")
time.sleep(2)

# # click on *
# drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[4]/div/div/div[2]/div[1]/div[2]/div/div/div/textarea[1]").send_keys("CHHATTISGARH STATE POWER .")
# time.sleep(2)
#
# # click on camera and add img
# drive.find_element(By.XPATH,"//input[@id='icon-button-image']").send_keys("C:/Users/GOWTHAM/Downloads/img5.jpg")
# time.sleep(2)



# click on add post
drive.find_element(By.XPATH,"//button[normalize-space()='Add Post']").click()
time.sleep(10)


##scroll up it reach msg other post
element = drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[2]/div/div[1]")
actions = ActionChains(drive)
actions.move_to_element(element).perform()
time.sleep(10)


# click  on like
drive.find_element(By.XPATH,"(//*[name()='path'][@class='cls-1'])[23]").click()
time.sleep(10)
#
# click on comment
drive.find_element(By.XPATH,"(//img[@alt='Comment'])[1]").click()
time.sleep(10)

##scroll up it reach msg other post
element = drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[2]/div/div[1]")
actions = ActionChains(drive)
actions.move_to_element(element).perform()
time.sleep(10)

# type here msg
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/textarea[1]").send_keys("CHHATTISGARH STATE POWER  a tender for  of cost to get .")
time.sleep(2)


# click on post msg
drive.find_element(By.XPATH,"//button[normalize-space()='Post']").click()
time.sleep(10)


##scroll up it reach msg
element = drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[4]/div/div/div[2]")
actions = ActionChains(drive)
actions.move_to_element(element).perform()
time.sleep(10)


# click on 3 dot
drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[9]").click()
time.sleep(10)

# click on edit
drive.find_element(By.XPATH,"//span[normalize-space()='Edit']").click()
time.sleep(10)


# selet artical msg
bday =drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[4]/div/div/div[2]/div[1]/div[2]/div/div/div/textarea[1]")
# to select pre data and then we can pass
bday.send_keys(Keys.CONTROL+'a')
time.sleep(1)
bday.send_keys("Please email us with details if you can help.")
time.sleep(2)

# # type here msg
# drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[4]/div/div/div[2]/div[1]/div[2]/div/div/div/textarea[1]").send_keys("CHHATTISGARH STATE POWER .")
# time.sleep(2)

# click on save
drive.find_element(By.XPATH,"//button[normalize-space()='Save']").click()
time.sleep(10)


# click on 3 dot
drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[9]").click()
time.sleep(10)

# click on delet comment
drive.find_element(By.XPATH,"//span[normalize-space()='Delete']").click()
time.sleep(10)


##scroll up it reach
element = drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[1]")
actions = ActionChains(drive)
actions.move_to_element(element).perform()
time.sleep(10)


# click on share
drive.find_element(By.XPATH,"//body[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[3]/div[1]/button[1]/div[1]/img[1]").click()
time.sleep(10)

# type here msg share
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div[2]/div/div/textarea[1]").send_keys("Where can I get some?")
time.sleep(2)


# click on post
drive.find_element(By.XPATH,"(//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root css-1pi4f66'])[1]").click()
time.sleep(10)

drive.refresh()
time.sleep(10)

##scroll up it reach poll
element = drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[1]")
actions = ActionChains(drive)
actions.move_to_element(element).perform()
time.sleep(10)



# click on 3 dot
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div/button").click()
time.sleep(10)

# click on edit
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div/div/div/div/ul/li[1]/div/span").click()
time.sleep(10)


# in side job , job title
bday =drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div[2]/div/div/textarea[1]")
# to select pre data and then we can pass
bday.send_keys(Keys.CONTROL+'a')
time.sleep(1)
bday.send_keys("making it over 2000 years old")
time.sleep(2)



# click on camera and add img
drive.find_element(By.XPATH,"//input[@id='icon-button-file']").send_keys("C:/Users/GOWTHAM/Downloads/img3.jpg")
time.sleep(2)

# # type here msg
# drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[4]/div/div/div[2]/div[1]/div[2]/div/div/div/textarea[1]").send_keys("CHHATTISGARH STATE POWER .")
# time.sleep(2)

# click on add post
drive.find_element(By.XPATH,"//button[normalize-space()='Add Post']").click()
time.sleep(10)



# click on 3 dot
drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[7]").click()
time.sleep(10)

# click on delet
drive.find_element(By.XPATH,"(//span[@class='MuiTypography-root MuiTypography-body1 MuiListItemText-primary css-2w5ikc'][normalize-space()='Delete'])[1]").click()
time.sleep(10)


# click on yes delet
drive.find_element(By.XPATH,"//button[normalize-space()='Yes']").click()
time.sleep(2)

drive.refresh()
time.sleep(10)
#
# click on 3 dot
drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[40]").click()
time.sleep(10)

# click on delet
drive.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div/div/div/div/ul/li[2]/div/span").click()
time.sleep(10)


# click on yes delet
drive.find_element(By.XPATH,"//button[normalize-space()='Yes']").click()
time.sleep(2)

drive.refresh()
time.sleep(10)

