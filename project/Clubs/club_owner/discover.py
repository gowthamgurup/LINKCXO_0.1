
from project.Common.initial import *
drive = commonlogin()
time.sleep(5)

# click on 3 line
drive.find_element(By.XPATH,"//button[@aria-label='account of current user']//*[name()='svg']//*[name()='path' and contains(@d,'M3 18h18v-')]").click()
time.sleep(2)

# click on club
drive.find_element(By.XPATH,"/html/body/div[2]/div[3]/ul/ul[1]/li[1]").click()
time.sleep(5)

# open 1 one share
drive.find_element(By.XPATH,"(//img[@alt='Share'])[1]").click()
time.sleep(9)

# in that share click on img
drive.find_element(By.XPATH,"(//img[@alt='logo'])[2]").click()
time.sleep(7)

# than click on drop down
drive.find_element(By.XPATH,"//div[@id='demo-simple-select']").click()
time.sleep(8)

#click on opend drop down full form
act_category=drive.find_element(By.XPATH,"//ul[@role='listbox']")

#select a option
drive.find_element(By.XPATH,"(//input[@type='checkbox'])[1]").click()
time.sleep(4)
drive.find_element(By.XPATH,"(//input[@type='checkbox'])[5]").click()
time.sleep(4)

act_category.send_keys(Keys.ESCAPE)

#click on share button
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/button").click()
time.sleep(10)

# # click on bookmark
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/h6").click()
time.sleep(4)

# click on club detail
drive.find_element(By.XPATH,"(//img[@class='MuiCardMedia-root MuiCardMedia-media MuiCardMedia-img css-y2tkt7'])[3]").click()
time.sleep(10)


