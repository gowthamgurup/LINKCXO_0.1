from project.Common.initial import *
drive = commonlogin()
time.sleep(10)

# News
drive.find_element(By.XPATH,"(//*[name()='svg'])[7]").click()
time.sleep(6)



# # scroll up which we given requiested
element = drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div/div/div[2]/ul/li[3]/div/div/div/div/div/div/div[2]/div[2]")
actions = ActionChains(drive)
actions.move_to_element(element).perform()
time.sleep(5)



# click on book mark
drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[6]").click()
time.sleep(1)

# # click on right arrow
# drive.find_element(By.XPATH,"//button[@aria-label='Go to next slide']").click()
# time.sleep(1)
#
# # click on right arrow
# drive.find_element(By.XPATH,"//button[@aria-label='Go to next slide']").click()
# time.sleep(1)


# click on showing like 4 month ago
drive.find_element(By.XPATH,"(//h6[@class='MuiTypography-root MuiTypography-h6 css-uv0j9y'][normalize-space()='Money control'])[1]").click()
time.sleep(5)


# switch to new window
handles = drive.window_handles
drive.switch_to.window(handles[1])
time.sleep(5)

drive.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(5)

drive.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(5)

drive.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(5)


drive.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(5)

drive.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(5)

drive.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(5)


