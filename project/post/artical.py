#

from project.Common.initial import *
drive = commonlogin()
time.sleep(7)

# click on articl
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div/div[3]/button[2]").click()
time.sleep(5)

# click on text
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div[2]/div/div/textarea[1]").send_keys("Lorem Ipsum articl")
time.sleep(2)

# click on add text
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div[3]/div/div/textarea[1]").send_keys("Lorem Ipsum is simply dummy text of the printing and typesetting industry.")
time.sleep(2)
#
# drive.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_UP)
# time.sleep(5)

# click on post
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div[4]/div/button").click()
time.sleep(2)


drive.refresh()
time.sleep(15)

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
bday.send_keys("Research encourages a comprehensive redesign of Blue Nun packaging  ARTICAL .")
time.sleep(2)

# # type here msg
# drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[4]/div/div/div[2]/div[1]/div[2]/div/div/div/textarea[1]").send_keys("CHHATTISGARH STATE POWER .")
# time.sleep(2)

# click on post
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div[4]/div/button").click()
time.sleep(2)








# click  on like
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[4]/div/div[1]/div/button").click()
time.sleep(10)
#
# click on comment
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[4]/div/div[2]/div/button").click()
time.sleep(10)

##scroll up it reach msg other post
element = drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[2]/div/div[1]")
actions = ActionChains(drive)
actions.move_to_element(element).perform()
time.sleep(10)

# type here msg
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/textarea[1]").send_keys("CHHATTISGARH STATE POWER  a tender for  of cost to get .")
time.sleep(2)


# click on post msg
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[5]/div/div/div[1]/div/div[3]/div/div/button").click()
time.sleep(10)


##scroll up it reach msg
element = drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]")
actions = ActionChains(drive)
actions.move_to_element(element).perform()
time.sleep(10)


# click on 3 dot
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[1]/div[3]/div/button").click()
time.sleep(10)

# click on edit
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[1]/div[3]/div/div/div/div/ul/li[1]/div/span").click()
time.sleep(10)


# selet artical msg
bday =drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[2]/div/div/div/textarea[1]")
# to select pre data and then we can pass
bday.send_keys(Keys.CONTROL+'a')
time.sleep(1)
bday.send_keys("CHHATTISGARH STATE POWER .")
time.sleep(2)

# # type here msg
# drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[4]/div/div/div[2]/div[1]/div[2]/div/div/div/textarea[1]").send_keys("CHHATTISGARH STATE POWER .")
# time.sleep(2)

# click on save
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[3]/div/div/button").click()
time.sleep(10)


# click on 3 dot
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[1]/div[3]/div/button").click()
time.sleep(10)

# click on delet comment
drive.find_element(By.XPATH,"//span[normalize-space()='Delete']").click()
time.sleep(10)


##scroll up it reach poll
element = drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[1]")
actions = ActionChains(drive)
actions.move_to_element(element).perform()
time.sleep(10)


# click on share
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[4]/div/div[3]/div/button").click()
time.sleep(10)

# type here msg share
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div[2]/div/div/textarea[1]").send_keys("Where can I get some?")
time.sleep(2)


# click on post
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div[4]/div[2]/div/div/button").click()
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
bday.send_keys("CHHATTISGARH STATE POWER .")
time.sleep(2)



# click on camera and add img
drive.find_element(By.XPATH,"//input[@id='icon-button-file']").send_keys("C:/Users/GOWTHAM/Downloads/img5.jpg")
time.sleep(2)

# # type here msg
# drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[4]/div/div/div[2]/div[1]/div[2]/div/div/div/textarea[1]").send_keys("CHHATTISGARH STATE POWER .")
# time.sleep(2)

# click on add post
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div[5]/div[2]/div/div/button").click()
time.sleep(10)




##scroll up it reach poll
element = drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[1]")
actions = ActionChains(drive)
actions.move_to_element(element).perform()
time.sleep(10)


# click on 3 dot
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div/button").click()
time.sleep(10)

# click on delet
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div/div/div/div/ul/li[2]/div/span").click()
time.sleep(10)


# click on yes delet
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div[2]/div[2]/div[2]/div/button").click()
time.sleep(2)

drive.refresh()
time.sleep(10)

# click on 3 dot
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[2]/div/div[1]/div[3]/div/button").click()
time.sleep(10)

# click on delet
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div/div/div/div/ul/li[2]/div/span").click()
time.sleep(10)


# click on yes delet
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div[2]/div[2]/div[2]/div/button").click()
time.sleep(2)

drive.refresh()
time.sleep(20)