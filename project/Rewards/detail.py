from project.Common.initial import *
drive = commonlogin()
time.sleep(2)

# click on rewards
drive.find_element(By.XPATH,"//div[@class='MuiBox-root css-zbtqym']//img[@alt='creditgold']").click()
time.sleep(2)


# click on details
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[1]/div/div[2]/div/button").click()
time.sleep(2)


# click on all times box
drive.find_element(By.XPATH,"(//div[@id='demo-select-small'])[1]").click()
time.sleep(2)

# click on all times
drive.find_element(By.XPATH,"//li[normalize-space()='All Time']").click()
time.sleep(2)

# click on how to earn?
drive.find_element(By.XPATH,"(//button[normalize-space()='How to earn?'])[1]").click()
time.sleep(2)


drive.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(5)

drive.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(5)

# drive.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
# time.sleep(5)

# drive.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_UP)
# time.sleep(5)

drive.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_UP)
time.sleep(5)

drive.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_UP)
time.sleep(5)

# drive.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_UP)
# time.sleep(5)

# click on MY cridets
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[1]/div/div[2]/div/button").click()
time.sleep(2)


drive.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(5)

drive.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(5)


drive.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_UP)
time.sleep(5)

drive.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_UP)
time.sleep(5)
