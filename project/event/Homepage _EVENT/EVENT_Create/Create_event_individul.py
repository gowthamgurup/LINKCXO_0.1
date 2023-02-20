from project.Common.initial import *
drive = commonlogin()
time.sleep(2)


# Event in home page
drive.find_element(By.XPATH,"//div[@class='MuiBox-root css-bxbpje']//div[3]").click()
time.sleep(10)

# click on create Event
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[1]/div/button[4]/div/div/h5").click()
time.sleep(2)

# click on camera and add img
drive.find_element(By.XPATH,"//input[@id='icon-button-file']").send_keys("C:/Users/GOWTHAM/Downloads/img8.jpg")
time.sleep(2)

# Title
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div[2]/div/form/div[1]/div[2]/div/div[1]/div/div/input").send_keys("WHITEFIELD'S BIGGEST NEW YEAR EVE 2023")
time.sleep(5)

# Detail
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div[2]/div/form/div[3]/div[2]/div/div[1]/div/textarea[1]").send_keys("images of Events Related Images: event party concert")
time.sleep(2)

 #Industry Drop Down radio button
drive.find_element(By.XPATH,"(//div[@id='demo-simple-select'])[1]").click()
time.sleep(6)

#click on opend drop down full form
act_ind = drive.find_element(By.XPATH,"(//div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx'])[2]")


#print("act_ind......",act_ind)

# selection multipal optation
# drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[4]").click()
# time.sleep(1)
drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[5]").click()
time.sleep(1)
drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[8]").click()
act_ind.send_keys(Keys.ESCAPE)

#function Drop Down radio button

drive.find_element(By.XPATH,"(//div[@role='button'])[3]").click()
time.sleep(2)

#click on opend drop down full form
act_fun=drive.find_element(By.XPATH,"//ul[@role='listbox']")

# select option
drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[4]/span").click()
time.sleep(1)
drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[6]/span").click()
time.sleep(1)
drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[7]/span").click()
# passing escape key
act_fun.send_keys(Keys.ESCAPE)

time.sleep(5)

# click on category
drive.find_element(By.XPATH,"(//div[@role='button'])[4]").click()
time.sleep(5)

#click on opend drop down full form
act_category=drive.find_element(By.XPATH,"//ul[@role='listbox']")

# select an optation
drive.find_element(By.XPATH,"//li[1]//span[1]//input[1]").click()
time.sleep(3)
drive.find_element(By.XPATH,"(//input[@type='checkbox'])[7]").click()
time.sleep(3)
# passing escape key
act_category.send_keys(Keys.ESCAPE)

# click on Host
drive.find_element(By.XPATH,"(//div[@role='button'][normalize-space()='Individual'])[1]").click()
time.sleep(5)
# select an option
drive.find_element(By.XPATH,"//li[normalize-space()='Individual']").click()
time.sleep(5)

# select mode radio button offline
drive.find_element(By.XPATH,"(//input[@name='row-radio-buttons-group'])[4]").click()
time.sleep(5)

# Event address
drive.find_element(By.XPATH,"(//input[@id='input-with-sx'])[2]").send_keys("Hsr layout bangalore")
time.sleep(5)

# enter fee amount
drive.find_element(By.XPATH,"(//input[@id='input-with-sx'])[3]").send_keys("1500")
time.sleep(5)

# event start_date
start_date=drive.find_element(By.XPATH,"//*[@id='standard-basic']")
start_date.send_keys(Keys.CONTROL+'a')
start_date.send_keys("01/20/2023")
time.sleep(2)

# event start_time
start_time=drive.find_element(By.XPATH,"(//input[@id='standard-basic'])[2]")
start_time.send_keys(Keys.CONTROL+'a')
start_time.send_keys("10:00 AM")
time.sleep(2)

# event End_date
End_date=drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div[2]/div/form/div[12]/div[2]/div/div/div/input")
End_date.send_keys(Keys.CONTROL+'a')
End_date.send_keys("12/31/2023")
time.sleep(2)

# event End_time
End_time=drive.find_element(By.XPATH,"(//input[@placeholder='hh:mm (a|p)m'])[2]")
End_time.send_keys(Keys.CONTROL+'a')
End_time.send_keys("04:00 PM")
time.sleep(2)

# Email
Email=drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div[2]/div/form/div[13]/div[2]/div/div[1]/div/div/input")
Email.send_keys(Keys.CONTROL+'a')
Email.send_keys("kprabhat956@gmail.com")
time.sleep(2)

# select invitees radio button
drive.find_element(By.XPATH,"(//input[@name='row-radio-buttons-group'])[6]").click()
time.sleep(5)

# Send invite
drive.find_element(By.XPATH,"(//div[@id='demo-simple-select'])[1]").click()
time.sleep(5)

#click on opend drop down full form
act_invite = drive.find_element(By.XPATH,"(//ul[@role='listbox'])[1]")

# select optaiton
drive.find_element(By.XPATH,"//li[1]//span[1]//input[1]").click()
drive.find_element(By.XPATH,"(//input[@type='checkbox'])[4]").click()
# drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li[3]/span[1]/input").click()
# drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li[4]/span[1]/input").click()
time.sleep(2)

act_invite.send_keys(Keys.ESCAPE)

#close
drive.find_element(By.XPATH,"//*[name()='path' and contains(@d,'M19 6.41 1')]").click()
time.sleep(5)

# click on submit button
drive.find_element(By.XPATH,"(//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root css-1pi4f66'][normalize-space()='Create'])[1]").click()
time.sleep(5)