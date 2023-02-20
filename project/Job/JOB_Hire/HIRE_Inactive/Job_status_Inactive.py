
from project.Common.initial import *
drive = commonlogin()
time.sleep(2)

# job in home page
drive.find_element(By.XPATH,"//*[@id='root']/div[1]/div/header/div/div/div[2]/div[3]/div[2]").click()
time.sleep(8)

# Hiring in job
drive.find_element(By.XPATH,"(//div[@class='css-1iegyem'])[2]").click()
time.sleep(20)

# click on JOB STATUS of post man
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[3]/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div[3]/div/button").click()
time.sleep(10)

#job status drop down
drive.find_element(By.XPATH,"(//div[@id='demo-simple-select'])[1]").click()
time.sleep(2)

# click on option as open
drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li[2]").click()
time.sleep(2)

# UPDATE button
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div/div/form/div[15]/div/button").click()
time.sleep(5)

drive.back()
time.sleep(7)

drive.back()
time.sleep(5)

drive.refresh()
time.sleep(5)

# click on JOB STATUS
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[3]/div/div[5]/div/div[4]/div/div[2]/div/div[2]/div[3]/div/button").click()
time.sleep(10)

#job status drop down
drive.find_element(By.XPATH,"(//div[@id='demo-simple-select'])[1]").click()
time.sleep(2)

# click on option as open
drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li[1]").click()
time.sleep(2)

 #  switch to attachment
drive.find_element(By.XPATH,"//span[@class='MuiSwitch-root MuiSwitch-sizeMedium css-1561xr6']").click()
time.sleep(3)


# click on attachment
attach=drive.find_element(By.XPATH,"//input[@id='icon-button-doc']")
# to check element is locating or not
print("attach.....",attach)
attach.send_keys("E:/gotham_1.pdf")

time.sleep(5)
# UPDATE button
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div/div/form/div[15]/div/button").click()


#  DONE  if i click on  update it will update