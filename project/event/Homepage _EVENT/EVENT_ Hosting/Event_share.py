

from project.Common.initial import *
drive = commonlogin()
time.sleep(9)

# Event in home page
drive.find_element(By.XPATH,"//div[@class='MuiBox-root css-bxbpje']//div[3]").click()
time.sleep(10)

# click on invite
drive.find_element(By.XPATH,"(//h6[contains(text(),'Invite')])[1]").click()
time.sleep(5)

# Send invite
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

# click on verify
drive.find_element(By.XPATH,"(//button[normalize-space()='Send'])[1]").click()
time.sleep(10)

# done
