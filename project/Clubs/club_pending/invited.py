
from project.Common.initial import *
drive = commonlogin()
time.sleep(5)

# click on 3 line
drive.find_element(By.XPATH,"//button[@aria-label='account of current user']//*[name()='svg']//*[name()='path' and contains(@d,'M3 18h18v-')]").click()
time.sleep(2)

# click on club
drive.find_element(By.XPATH,"/html/body/div[2]/div[3]/ul/ul[1]/li[1]").click()
time.sleep(5)

# click on pending
drive.find_element(By.XPATH,"(//div[@class='css-1iegyem'])[2]").click()
time.sleep(10)

# click on share
drive.find_element(By.XPATH,"//body[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/button[1]/div[1]/img[1]").click()
time.sleep(5)


# click on img
drive.find_element(By.XPATH,"(//img[@alt='logo'])[2]").click()
time.sleep(5)

# click on drop down
drive.find_element(By.XPATH,"//div[@id='demo-simple-select']").click()
time.sleep(5)

#click on opend drop down full form
act_invite = drive.find_element(By.XPATH,"(//ul[@role='listbox'])[1]")

# select optaiton
drive.find_element(By.XPATH,"//li[1]//span[1]//input[1]").click()
# drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li[2]/span[1]/input").click()
# drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li[3]/span[1]/input").click()
#drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li[4]/span[1]/input").click()
time.sleep(2)

act_invite.send_keys(Keys.ESCAPE)
time.sleep(5)

# click on send
drive.find_element(By.XPATH,"(//button[normalize-space()='Share'])[1]").click()
time.sleep(5)


# click on club
drive.find_element(By.XPATH,"(//img[@class='MuiCardMedia-root MuiCardMedia-media MuiCardMedia-img css-y2tkt7'])[1]").click()
time.sleep(5)

# member=drive.find_element(By.XPATH,"(//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root css-1pi4f66'][normalize-space()='1 Members'])[1]")
# member.click()
# time.sleep(2)

# drive.back()
# time.sleep(2)

# click on 3 dot
drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[4]").click()
time.sleep(2)

report=drive.find_element(By.XPATH,"//span[normalize-space()='Report']")
report.click()
time.sleep(2)

# select optaiton
drive.find_element(By.XPATH,"//input[@name='Inappropriate']").click()
drive.find_element(By.XPATH,"//input[@name='Harassment']").click()
drive.find_element(By.XPATH,"//input[@name='False_Information']").click()
drive.find_element(By.XPATH,"//input[@name='Intellectual_Property']").click()
time.sleep(2)

# type here
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div[3]/div/div/textarea[1]").send_keys("It is a sequence of Latin words that, as they are positioned, do not form sentences with a complete sense, but give life to a test text useful to fill spaces that will subsequently be occupied from ad hoc texts composed by communication professionals.")
time.sleep(2)


# click on send
drive.find_element(By.XPATH,"//button[normalize-space()='Submit']").click()


# click on 3 dot
drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[4]").click()
time.sleep(2)

# click on bookmark
drive.find_element(By.XPATH,"(//*[name()='svg'])[20]").click()
time.sleep(2)



# click on accept
drive.find_element(By.XPATH,"(//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root css-1pi4f66'][normalize-space()='Accept'])[1]").click()
time.sleep(10)



member=drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div/div/button")
member.click()
time.sleep(2)

drive.refresh()
time.sleep(10)

drive.back()
time.sleep(15)

drive.refresh()
time.sleep(10)


# click on leave
drive.find_element(By.XPATH,"(//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root css-1pi4f66'][normalize-space()='Leave'])[1]").click()
time.sleep(10)


drive.refresh()
time.sleep(10)
# click on join
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[2]/div/div/button").click()
time.sleep(10)

#
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[2]/div/div/button").click()
time.sleep(10)

drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[2]/div/div/button").click()
time.sleep(10)

drive.refresh()
time.sleep(10)


# not done  cancle requiest is not working


drive.back()
time.sleep(15)








# scrool to  REQUISTED

#scroll up it reach to applied section
element = drive.find_element(By.XPATH,"(//div[@class='MuiBox-root css-1kl4okd'])[1]")
actions = ActionChains(drive)
actions.move_to_element(element).perform()


# click on share
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[3]/div/div[2]/div/div[1]/div[2]/div/div/div/div/div[2]/div/div[2]/div/button/div/img").click()
time.sleep(5)


# click on img
drive.find_element(By.XPATH,"(//img[@alt='logo'])[2]").click()
time.sleep(5)

# click on drop down
drive.find_element(By.XPATH,"//div[@id='demo-simple-select']").click()
time.sleep(5)

#click on opend drop down full form
act_invite = drive.find_element(By.XPATH,"(//ul[@role='listbox'])[1]")

# select optaiton
drive.find_element(By.XPATH,"//li[1]//span[1]//input[1]").click()
# drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li[2]/span[1]/input").click()
# drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li[3]/span[1]/input").click()
#drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li[4]/span[1]/input").click()
time.sleep(2)

act_invite.send_keys(Keys.ESCAPE)
time.sleep(5)

# click on send
drive.find_element(By.XPATH,"(//button[normalize-space()='Share'])[1]").click()
time.sleep(5)




# click on club
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[3]/div/div[2]/div/div[1]/div[2]/div/div/div/div/div[1]/div/img").click()
time.sleep(5)

# member=drive.find_element(By.XPATH,"(//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root css-1pi4f66'][normalize-space()='1 Members'])[1]")
# member.click()
# time.sleep(2)

# drive.back()
# time.sleep(2)

# click on 3 dot
drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[4]").click()
time.sleep(2)

report=drive.find_element(By.XPATH,"//span[normalize-space()='Report']")
report.click()
time.sleep(2)

# select optaiton
drive.find_element(By.XPATH,"//input[@name='Inappropriate']").click()
drive.find_element(By.XPATH,"//input[@name='Harassment']").click()
drive.find_element(By.XPATH,"//input[@name='False_Information']").click()
drive.find_element(By.XPATH,"//input[@name='Intellectual_Property']").click()
time.sleep(2)

# type here
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div[3]/div/div/textarea[1]").send_keys("It is a sequence of Latin words that, as they are positioned, do not form sentences with a complete sense, but give life to a test text useful to fill spaces that will subsequently be occupied from ad hoc texts composed by communication professionals.")
time.sleep(8)


# click on send
drive.find_element(By.XPATH,"//*[@id='root']/div[2]/div/div/div/div[4]/div/button").click()
time.sleep(10)

# click on 3 dot
drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[4]").click()
time.sleep(2)

# click on bookmark
drive.find_element(By.XPATH,"(//*[name()='svg'])[20]").click()
time.sleep(10)



# click on canclerequiest
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div/button").click()
time.sleep(8)

# click on JOIN
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div/button").click()
time.sleep(8)

# click on cancle request
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div/button").click()
time.sleep(8)


drive.refresh()
time.sleep(5)


# click on 3 dot
drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[4]").click()
time.sleep(2)

report=drive.find_element(By.XPATH,"//span[normalize-space()='Report']")
report.click()
time.sleep(2)

# select optaiton
drive.find_element(By.XPATH,"//input[@name='Inappropriate']").click()
drive.find_element(By.XPATH,"//input[@name='Harassment']").click()
drive.find_element(By.XPATH,"//input[@name='False_Information']").click()
drive.find_element(By.XPATH,"//input[@name='Intellectual_Property']").click()
time.sleep(2)

# type here
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div[3]/div/div/textarea[1]").send_keys("It is a sequence of Latin words that, as they are positioned, do not form sentences with a complete sense, but give life to a test text useful to fill spaces that will subsequently be occupied from ad hoc texts composed by communication professionals.")
time.sleep(8)


# click on send
drive.find_element(By.XPATH,"//*[@id='root']/div[2]/div/div/div/div[4]/div/button").click()
time.sleep(10)


# click on bookmark
drive.find_element(By.XPATH,"(//*[name()='svg'])[20]").click()
time.sleep(10)


drive.back()
time.sleep(8)

# click on cancle request
drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[6]").click()
time.sleep(10)




