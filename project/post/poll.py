# open
from project.Common.initial import *
drive = commonlogin()
time.sleep(7)

# click on poll
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div/div[3]/button[3]").click()
time.sleep(5)

# write a poll question
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div[2]/div[1]/div/textarea[1]").send_keys("will it rain today")
time.sleep(3)


# write a option 1
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/form/div[1]/div/div[2]/div/div/div/input").send_keys("Yes")
time.sleep(10)

# write a option 2
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/form/div[2]/div/div[2]/div/div/div/input").send_keys("No")
time.sleep(10)

# click on add another option
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/form/div[3]/div[1]/h6").click()
time.sleep(3)


# write a option 3
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/form/div[3]/div/div[2]/div/div/div/input").send_keys("Nor")
time.sleep(10)

# click on add another option
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/form/div[4]/div[1]/h6").click()
time.sleep(3)

# write a option 4
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/form/div[4]/div/div[2]/div/div/div/input").send_keys("Both")
time.sleep(10)


# click on add Remove option
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/form/div[5]/div[2]/h6").click()
time.sleep(3)


# click on select day or week
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/form/div[5]/div/div[2]/div/div/div").click()
time.sleep(3)

# click on select 1 week
drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li[3]").click()
time.sleep(3)


# click on post
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/form/div[6]/div[2]/div/div[1]/div/button").click()
time.sleep(15)

drive.refresh()
time.sleep(15)


# click on vote
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[2]/div/div/div[1]/div[3]/label/span/input").click()
time.sleep(10)


# click  on like
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[3]/div/div[1]/div/button").click()
time.sleep(10)
#
# click on comment
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[3]/div/div[2]/div/button").click()
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
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div/div/button").click()
time.sleep(10)


##scroll up it reach msg
element = drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[4]/div/div/div[2]")
actions = ActionChains(drive)
actions.move_to_element(element).perform()
time.sleep(10)


# click on 3 dot
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[4]/div/div/div[2]/div[1]/div[1]/div[3]/div/button").click()
time.sleep(10)

# click on edit
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[4]/div/div/div[2]/div[1]/div[1]/div[3]/div/div/div/div/ul/li[1]/div/span").click()
time.sleep(10)




# in side job , job title
bday =drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[4]/div/div/div[2]/div[1]/div[2]/div/div/div/textarea[1]")
# to select pre data and then we can pass
bday.send_keys(Keys.CONTROL+'a')
time.sleep(1)
bday.send_keys("CHHATTISGARH STATE POWER .")
time.sleep(2)

# # type here msg
# drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[4]/div/div/div[2]/div[1]/div[2]/div/div/div/textarea[1]").send_keys("CHHATTISGARH STATE POWER .")
# time.sleep(2)

# click on save
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[4]/div/div/div[2]/div[1]/div[3]/div/div/button").click()
time.sleep(10)

# click on 3 dot
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[4]/div/div/div[2]/div[1]/div[1]/div[3]/div/button").click()
time.sleep(10)

# click on delet comment
drive.find_element(By.XPATH,"//span[normalize-space()='Delete']").click()
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
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div/div/div/div/ul/li/div/span").click()
time.sleep(10)


# click on yes delet
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div[2]/div[2]/div[2]/div/button").click()
time.sleep(2)

drive.refresh()
time.sleep(10)

# not done it is confusition need to clarfy after sharing artical it is creating new post and if i got edit share its showing post card