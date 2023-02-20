from project.Common.initial import *
drive = commonlogin()
time.sleep(2)


# click on profile
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/aside[1]/div/div[1]/div/div[1]/div/img").click()
time.sleep(2)

#scroll up it reach to applied section
element = drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div/div/div/div[4]/div[1]")
actions = ActionChains(drive)
actions.move_to_element(element).perform()
time.sleep(5)


#scroll up it reach to applied section
element = drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div/div/div/div[4]/div[2]/div/p/div[11]/div/div[1]/div[1]")
actions = ActionChains(drive)
actions.move_to_element(element).perform()
time.sleep(3)


#scroll up it reach to profile
element = drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div/div/div/div[1]")
actions = ActionChains(drive)
actions.move_to_element(element).perform()
time.sleep(3)

# click on profile
drive.find_element(By.XPATH,"(//*[name()='circle'])[4]").click()
time.sleep(2)

#click on first name
first =drive.find_element(By.XPATH,"(//input[@id='input-with-sx'])[1]")
first.send_keys(Keys.CONTROL+'a')
first.send_keys("Prabhat")
time.sleep(2)


#click on last name
last =drive.find_element(By.XPATH,"(//input[@id='input-with-sx'])[2]")
last.send_keys(Keys.CONTROL+'a')
last.send_keys("Kumar")
time.sleep(2)


# click on Designation
drive.find_element(By.XPATH,"(//span[@class='MuiTypography-root MuiTypography-body1 MuiListItemText-primary css-2w5ikc'][normalize-space()='Senior Vice President'])[1]").click()
time.sleep(2)

# click on select an option
drive.find_element(By.XPATH,"(//li[@class='MuiMenuItem-root MuiMenuItem-gutters Mui-selected MuiButtonBase-root css-1lhnbki'])[1]").click()
time.sleep(2)


#click on company name
company =drive.find_element(By.XPATH,"(//input[@id='input-with-sx'])[3]")
company.send_keys(Keys.CONTROL+'a')
company.send_keys("samsung")
time.sleep(2)

#
#click on address name
address =drive.find_element(By.XPATH,"//body//div//div//div//main//div//div//div//div//div//div//form//div//div//div//div//div//input[@value='Bihar']")
address.send_keys(Keys.CONTROL+'a')
address.send_keys("MP")
time.sleep(2)

#click on Profile Headline*
Headline =drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div/div/div/div[3]/form/div[5]/div/div[2]/div/textarea[1]")
Headline.send_keys(Keys.CONTROL+'a')
Headline.send_keys("Testing")
time.sleep(2)

#click on Bio
Bio=drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div/div/div/div[3]/form/div[6]/div/div[2]/div/textarea[1]")
Bio.send_keys(Keys.CONTROL+'a')
Bio.send_keys("Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget ")
time.sleep(2)

#click on Website
Website =drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div/div/div/div[3]/form/div[7]/div/div[2]/div/div/input")
Website.send_keys(Keys.CONTROL+'a')
Website.send_keys("www.alfatecprivate.com")
time.sleep(2)

#click on bios
bios =drive.find_element(By.XPATH,"//body//div//div//div//main//div//div//div//div//div//div//form//div//div//div//div//div//input[contains(@value,'my first blog')]")
bios.send_keys(Keys.CONTROL+'a')
bios.send_keys("my first testing")
time.sleep(2)


#click on Birthday

Birthday =drive.find_element(By.XPATH,"(//input[@id='standard-basic'])[1]")
Birthday.send_keys(Keys.CONTROL+'a')
Birthday.send_keys("02/17/1990")
time.sleep(2)

# click on save
drive.find_element(By.XPATH,"(//button[@type='submit'][normalize-space()='Save'])[1]").click()


# Done
