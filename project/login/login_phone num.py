
from project.Common.initial import *
drive = commonlogin()
time.sleep(5)
# job in home page
drive.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/header/div/div/div[2]/div[3]/div[2]/div[2]/h2").click()
time.sleep(5)

# Hiring in job
drive.find_element(By.XPATH,"(//div[@class='css-1iegyem'])[2]").click()
time.sleep(5)

# till job done

# click on see more
seemore=drive.find_element(By.XPATH,"(//h5[@class='MuiTypography-root MuiTypography-h5 css-15jga2m'][normalize-space()='See All'])[1]")
print("seemore.....",seemore)
seemore.click()
time.sleep(5)

# in hiring click share button
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[3]/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/button").click()
time.sleep(2)

# in that share click on image
drive.find_element(By.XPATH,"//*[@id='root']/div[2]/div/div/div/div/div[2]/div/div[1]/img").click()
time.sleep(2)

# in that click on drop down
drive.find_element(By.XPATH,"//*[@id='demo-simple-select']").click()
time.sleep(2)


#click on opend drop down full form
act_invite = drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul")

# select optaiton
drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li[1]/span[1]/input").click()
# drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li[2]/span[1]/input").click()
# drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li[3]/span[1]/input").click()
#drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li[4]/span[1]/input").click()
time.sleep(2)

act_invite.send_keys(Keys.ESCAPE)


# click on share button
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/button").click()
time.sleep(2)


