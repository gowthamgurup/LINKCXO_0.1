from project.Common.initial import *
drive = commonlogin()
time.sleep(2)

# click on rewards
drive.find_element(By.XPATH,"//div[@class='MuiBox-root css-zbtqym']//img[@alt='creditgold']").click()
time.sleep(5)

# click on members
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[2]/div/div/div/button[1]/div").click()
time.sleep(5)

# click on details lxr50
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[3]/div/div/div/div[2]/div/div[2]/div[5]/div/div[2]/div/button").click()
time.sleep(2)

#scroll up it reach to applied section
element = drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div/div[1]/div[3]/div[2]/div[1]")
actions = ActionChains(drive)
actions.move_to_element(element).perform()
time.sleep(5)

# click on view voucher
drive.find_element(By.XPATH,"(//div)[135]").click()
time.sleep(2)

#scroll up it reach to applied section till T & C
element = drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div/div[2]/div/div[7]")
actions = ActionChains(drive)
actions.move_to_element(element).perform()
time.sleep(10)
# click on link
drive.find_element(By.XPATH,"(//div[@class='css-1fkzjhu'])[1]").click()
time.sleep(10)

# switch to new window
handles = drive.window_handles
drive.switch_to.window(handles[0])
time.sleep(5)

drive.back()
time.sleep(10)

#
# #scroll up it reach to applied section
# element = drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div/div[1]/div[3]/div[2]/div[1]")
# actions = ActionChains(drive)
# actions.move_to_element(element).perform()
# time.sleep(5)
#
# # click on view voucher
# drive.find_element(By.XPATH,"(//div)[142]").click()
# time.sleep(2)
#
# #scroll up it reach to applied section till T & C
# element = drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div/div[2]/div/div[7]")
# actions = ActionChains(drive)
# actions.move_to_element(element).perform()
# time.sleep(10)
# # click on link
# drive.find_element(By.XPATH,"(//div[@class='css-1fkzjhu'])[1]").click()
# time.sleep(10)
#
# # switch to new window
# handles = drive.window_handles
# drive.switch_to.window(handles[0])
# time.sleep(5)
#
# drive.back()
# time.sleep(10)
#
