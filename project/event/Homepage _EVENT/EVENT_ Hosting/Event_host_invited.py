from project.Common.initial import *
drive = commonlogin()
time.sleep(2)

# Event in home page
drive.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/header/div/div/div[2]/div[3]/div[3]/div[2]/h2").click()
time.sleep(10)

# click on event img
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[2]/div/div[1]/div/div[1]/div/div/div[2]/div/div/div[1]/div/img").click()
time.sleep(10)

# click on 3 dot
drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[4]").click()
time.sleep(2)

# click on manage invitation
drive.find_element(By.XPATH,"//span[normalize-space()='Manage Invitations']").click()
time.sleep(10)

# click on event invited
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[1]/div/button[2]/div/h5[1]").click()
time.sleep(10)

# # click on Unsend
# drive.find_element(By.XPATH,"(//button[contains(text(),'Unsend')])[1]").click()
# time.sleep(20)

# click on attending
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[1]/div/button[3]/div/div/h5[1]").click()
time.sleep(2)
#done

drive.back()
time.sleep(10)


# click on 3 dot
drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[4]").click()
time.sleep(2)


# click on manage invitation
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/ul/li[1]/div/span").click()
time.sleep(10)


# drive.back()
# time.sleep(10)




# # click on edit
# drive.find_element(By.XPATH,"(//h6[@class='MuiTypography-root MuiTypography-h6 css-152tusv'][normalize-space()='Edit'])[1]").click()
# time.sleep(10)
#
# # click on camera and add img
# drive.find_element(By.XPATH,"//input[@id='icon-button-file']").send_keys("E:/new imgs.jpg")
# time.sleep(2)


# click on camera and add img
drive.find_element(By.XPATH,"//input[@id='icon-button-file']").send_keys("C:/Users/GOWTHAM/Downloads/img8.jpg")
time.sleep(2)

# # Title
fee=drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div[2]/div/form/div[1]/div[2]/div/div[1]/div/div/input")
fee.send_keys(Keys.CONTROL+'a')
fee.send_keys("Investor Desertlicious")
time.sleep(5)

# # Detail
# drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div[2]/div/form/div[3]/div[2]/div/div[1]/div/textarea[1]").send_keys("images of Events Related Images: event party concert")
# time.sleep(2)
#
#  #Industry Drop Down radio button
# drive.find_element(By.XPATH,"(//div[@id='demo-simple-select'])[1]").click()
# time.sleep(6)
#
# #click on opend drop down full form
# act_ind = drive.find_element(By.XPATH,"(//div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx'])[2]")
#
#
# #print("act_ind......",act_ind)
#
# # selection multipal optation
# # drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[4]").click()
# # time.sleep(1)
# drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[5]").click()
# time.sleep(1)
# drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[8]").click()
# act_ind.send_keys(Keys.ESCAPE)
#
# #function Drop Down radio button
#
# drive.find_element(By.XPATH,"(//div[@role='button'])[3]").click()
# time.sleep(2)
#
# #click on opend drop down full form
# act_fun=drive.find_element(By.XPATH,"//ul[@role='listbox']")
#
# # select option
# drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[4]/span").click()
# time.sleep(1)
# drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[6]/span").click()
# time.sleep(1)
# drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[7]/span").click()
# # passing escape key
# act_fun.send_keys(Keys.ESCAPE)

# time.sleep(5)
#
# # click on category
# drive.find_element(By.XPATH,"(//div[@role='button'])[4]").click()
# time.sleep(5)
#
# #click on opend drop down full form
# act_category=drive.find_element(By.XPATH,"//ul[@role='listbox']")
#
# # select an optation
# drive.find_element(By.XPATH,"//li[1]//span[1]//input[1]").click()
# time.sleep(3)
# drive.find_element(By.XPATH,"(//input[@type='checkbox'])[7]").click()
# time.sleep(3)
# # passing escape key
# act_category.send_keys(Keys.ESCAPE)



# way to scroll to page

element = drive.find_element(By.XPATH,"(//div[@class='css-1gnfpfi'])[1]")
actions = ActionChains(drive)
actions.move_to_element(element).perform()
time.sleep(2)

# click on Host
drive.find_element(By.XPATH,"//body[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/form[1]/div[7]/div[2]/div[1]/div[1]/div[1]").click()
time.sleep(5)
# select an option
drive.find_element(By.XPATH,"//li[normalize-space()='Individual']").click()
time.sleep(5)

# select mode radio button offline
drive.find_element(By.XPATH,"(//input[@name='row-radio-buttons-group'])[4]").click()
time.sleep(5)

# Event address
address=drive.find_element(By.XPATH,"(//input[@id='input-with-sx'])[2]")
address.send_keys(Keys.CONTROL+'a')
address.send_keys("Hsr layout bangalore")
time.sleep(5)

# enter fee amount
fee=drive.find_element(By.XPATH,"(//input[@id='input-with-sx'])[3]")
fee.send_keys(Keys.CONTROL+'a')
fee.send_keys("1500")
time.sleep(5)

# event start_date
start_date=drive.find_element(By.XPATH,"//*[@id='standard-basic']")
start_date.send_keys(Keys.CONTROL+'a')
start_date.send_keys("11/01/2023")
time.sleep(2)

# event start_time
start_time=drive.find_element(By.XPATH,"(//input[@id='standard-basic'])[2]")
start_time.send_keys(Keys.CONTROL+'a')
start_time.send_keys("10:00 AM")
time.sleep(2)

# event End_date
End_date=drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div[2]/div/form/div[12]/div[2]/div/div/div/input")
End_date.send_keys(Keys.CONTROL+'a')
End_date.send_keys("12/31/2024")
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


# click on submit button
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div[2]/div/form/div[14]/div/button").click()
time.sleep(5)

