

from project.Common.initial import *
drive = commonlogin()

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

# click on camera and add img   "C:\Users\GOWTHAM\Downloads\img5.jpg"
drive.find_element(By.XPATH,"//input[@id='icon-button-file']").send_keys("C:/Users/GOWTHAM/Downloads/img5.jpg")
time.sleep(2)

# Title
drive.find_element(By.XPATH,"(//input[@id='input-with-sx'])[1]").send_keys("Soul Foodies")
time.sleep(5)

# Detail
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div[2]/div/form/div[3]/div[2]/div/div[1]/div/textarea[1]").send_keys("images of Events Related Images: event party concert")
time.sleep(2)

# click on type radio button
drive.find_element(By.XPATH,"(//input[@name='row-radio-buttons-group'])[2]").click()
time.sleep(5)

# click on fee
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div[2]/div/form/div[5]/div[2]/div/div/div").click()
time.sleep(5)

# select inr
drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li").click()
time.sleep(5)

# click on amount
club1=drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div[2]/div/form/div[5]/div[3]/div/div[1]/div/div/input")
print("club......", club)
club1.send_keys("1000")

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
drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li[5]").click()
time.sleep(3)

# click on create button
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div[2]/div/form/div[9]/div/button").click()
time.sleep(5)

time.sleep(20)
# drive.back()

# click on delet button
drive.find_element(By.XPATH,"(//button[@aria-label='share'])[1]").click()
time.sleep(3)

# click on yes
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[2]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/button").click()
time.sleep(20)



