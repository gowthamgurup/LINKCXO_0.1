

from project.Common.initial import *
drive = commonlogin()
time.sleep(7)

# click on 3 line
drive.find_element(By.XPATH,"//button[@aria-label='account of current user']//*[name()='svg']//*[name()='path' and contains(@d,'M3 18h18v-')]").click()
time.sleep(2)

# click on club
drive.find_element(By.XPATH,"/html/body/div[2]/div[3]/ul/ul[1]/li[1]").click()
time.sleep(5)

# click on creat
club=drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[1]/div/button[4]/div/div/h5")
print("club......",club)
club.click()
time.sleep(5)

# click on camera and add img
drive.find_element(By.XPATH,"//input[@id='icon-button-file']").send_keys("C:/Users/GOWTHAM/Downloads/img8.jpg")
time.sleep(2)

# Title
drive.find_element(By.XPATH,"(//input[@id='input-with-sx'])[1]").send_keys("Green Monsters")
time.sleep(5)

# Detail
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div[2]/div/form/div[3]/div[2]/div/div[1]/div/textarea[1]").send_keys("images of Events Related Images: event party concert")
time.sleep(2)

# click on type radio button
drive.find_element(By.XPATH,"(//input[@name='row-radio-buttons-group'])[1]").click()
time.sleep(5)

# click on fee
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div[2]/div/form/div[5]/div[4]/label/span[1]/input").click()
time.sleep(5)

 #Industry Drop Down radio button
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div[2]/div/form/div[6]/div[2]/div/div/div").click()
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

drive.find_element(By.XPATH,"(//div[@role='button'])[4]").click()
time.sleep(2)

#click on opend drop down full form
act_fun=drive.find_element(By.XPATH,"//ul[@role='listbox']")

# select option
drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[4]/span").click()
time.sleep(1)
drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[6]/span").click()
time.sleep(1)
# drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[7]/span").click()
# passing escape key
act_fun.send_keys(Keys.ESCAPE)

time.sleep(5)

# click on category
drive.find_element(By.XPATH,"(//div[@role='button'])[5]").click()
time.sleep(5)

# select an optation
drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li[2]").click()
time.sleep(3)

# click on create button
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div[2]/div/form/div[9]/div/button").click()
time.sleep(20)
#
# drive.back()
# time.sleep(10)

# click on invite
drive.find_element(By.XPATH,"(//img[@alt='Comment'])[1]").click()
time.sleep(5)

# than click on drop down
drive.find_element(By.XPATH,"//div[@id='demo-simple-select']").click()
time.sleep(8)

#click on opend drop down full form
act_share = drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul")

#select a option
drive.find_element(By.XPATH,"(//input[@type='checkbox'])[1]").click()
time.sleep(2)
# drive.find_element(By.XPATH,"(//input[@type='checkbox'])[3]").click()
# time.sleep(2)
# drive.find_element(By.XPATH,"(//input[@type='checkbox'])[4]").click()
# time.sleep(2)
act_share.send_keys(Keys.ESCAPE)

#click on share button
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/button").click()
time.sleep(8)


# Edit
#click on Edit
drive.find_element(By.XPATH,"(//*[name()='svg'])[23]").click()
time.sleep(8)

# click on camera and add img
drive.find_element(By.XPATH,"//input[@id='icon-button-file']").send_keys("C:/Users/GOWTHAM/Downloads/img4.jpg")
time.sleep(2)

# Title
title=drive.find_element(By.XPATH,"(//input[@id='input-with-sx'])[1]")
title.send_keys(Keys.CONTROL+'a')
title.send_keys("Timeless Fashionistas")
time.sleep(5)


# Detail
detail=drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div[2]/div/form/div[3]/div[2]/div/div[1]/div/textarea[1]")
detail.send_keys(Keys.CONTROL+'a')
detail.send_keys("Disclosure: Some of the links on this website might be affiliate links,")
time.sleep(2)



# click on type radio button
drive.find_element(By.XPATH,"(//input[@name='row-radio-buttons-group'])[1]").click()
time.sleep(5)

# fee inr
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div[2]/div/form/div[5]/div[2]/div/div/div").click()
time.sleep(5)

# click on inr
drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li").click()
time.sleep(5)

# click on fee
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div[2]/div/form/div[5]/div[4]/label/span[1]/input").click()
time.sleep(5)

 #Industry Drop Down radio button
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div[2]/div/form/div[6]/div[2]/div/div/div").click()
time.sleep(6)

#click on opend drop down full form
act_ind = drive.find_element(By.XPATH,"(//div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx'])[2]")


#print("act_ind......",act_ind)

# selection multipal optation
drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[4]").click()
time.sleep(1)
# drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[5]").click()
# time.sleep(1)
# drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[8]").click()
act_ind.send_keys(Keys.ESCAPE)

#function Drop Down radio button

drive.find_element(By.XPATH,"(//div[@role='button'])[4]").click()
time.sleep(2)

#click on opend drop down full form
act_fun=drive.find_element(By.XPATH,"//ul[@role='listbox']")

# select option
# drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[4]/span").click()
# time.sleep(1)
# drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[6]/span").click()
# time.sleep(1)
drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[7]/span").click()
# passing escape key
act_fun.send_keys(Keys.ESCAPE)

time.sleep(5)

# click on category
drive.find_element(By.XPATH,"(//div[@role='button'])[5]").click()
time.sleep(5)

# select an optation
drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li[7]").click()
time.sleep(3)



# BUG IS THERE  UN ABLE TO UPDATE ITS THROUGH ERROR MESSAGE (ALL FEILDS ARE MANDETRY)

# click on create button
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div[2]/div/form/div[9]/div/button").click()
time.sleep(20)