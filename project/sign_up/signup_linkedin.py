from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
drive=webdriver.Chrome(r"C:\Users\Gowtham p\Downloads\chromedriver_win32\chromedriver.exe")
url=r"http://linkcxo-frontend-testing.s3-website.ap-south-1.amazonaws.com"
drive.get(url)
time.sleep(5)
drive.maximize_window()
time.sleep(2)

#  Be a member
drive.find_element(By.XPATH,"/html/body/div/div/div[1]/div/header/div/div[3]/button/a").click()

# click on sign up
drive.find_element(By.XPATH,"//div[@class='MuiBox-root css-4g6ai3']/h5").click()

# click on linkedin
drive.find_element(By.XPATH,"//*[@id='root']/div/div/div[2]/div/div/div[4]/div/div/div[2]/h6").click()
time.sleep(5)

# switch to new window
handles = drive.window_handles
drive.switch_to.window(handles[1])

# linkedin email or phone num
linkedin = drive.find_element(By.XPATH,"//input[@id='username']")
print("linkedin......",linkedin)
linkedin.send_keys("gowthampl94@gmail.com")
time.sleep(2)

# linkedin password
drive.find_element(By.XPATH,"//div[@class='form__input--floating'][2]/input").send_keys("ab_TAK56@12")
time.sleep(2)

# linkedin signin
drive.find_element(By.XPATH,"//div[@class='login__form_action_container login__form_action_container--multiple-actions']/button").click()
handles = drive.window_handles
print(handles)

# linkedin allow button
# drive.find_element(By.XPATH,"//*[@id='oauth__auth-form__submit-btn']").click()



drive.switch_to.window(handles[0])

time.sleep(15)


# pending still
#1st name
Fname=drive.find_element(By.ID,"input-with-sx")
print("Fname......",Fname)
time.sleep(2)
# to select pre date and then we can pass    : send_keys("12/08/1994") if we didnot select means we cant type
Fname.send_keys(Keys.CONTROL+'a')
time.sleep(1)
Fname.send_keys("Gowtham")
time.sleep(2)
# last name
Lname=drive.find_element(By.XPATH," //div[@class='MuiInput-root MuiInput-underline MuiInputBase-root MuiInputBase-colorPrimary MuiInputBase-formControl MuiInputBase-sizeSmall css-6ct1tn']/input")
time.sleep(2)
Lname.send_keys(Keys.CONTROL+'a')
time.sleep(1)
Lname.send_keys("P")
time.sleep(7)

#company
drive.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/input[1]").send_keys("nanda group pvt ltd")
time.sleep(2)
# Designation
drive.find_element(By.XPATH,"//form/div[3]/div/div/div/div/div").click()
time.sleep(2)
# SELECT option in drop down
drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[7]").click()
time.sleep(2)

#Total Year of Experience

drive.find_element(By.XPATH,"//form/div[4]/div/div/div/div/div/input").send_keys("10 year")
time.sleep(2)

 #Industry Drop Down radio button
drive.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/form/div[5]/div/div[2]").click()
time.sleep(1)
act_ind = drive.find_element(By.XPATH,"//div[contains(@class,'MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx')]")
time.sleep(2)

#print("act_ind......",act_ind)

# selection multipal optation
drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[4]").click()
time.sleep(1)
drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[5]").click()
time.sleep(1)
drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[8]").click()
act_ind.send_keys(Keys.ESCAPE)


#function Drop Down radio button

drive.find_element(By.XPATH,"//div[6]/div/div/div/div/div").click()
time.sleep(2)
#click on opend drop down full form
act_fun=drive.find_element(By.XPATH,"//div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']")

# select option
drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[4]/span").click()
time.sleep(1)
drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[6]/span").click()
time.sleep(1)
drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[7]/span").click()

# passing escape key
act_fun.send_keys(Keys.ESCAPE)

# Email
drive.find_element(By.XPATH,"//div[@class='MuiBox-root css-111wug5']//input[@id='input-with-sx']").send_keys("7483331671")
time.sleep(2)
# location
drive.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[8]/div[1]/div[2]/div[1]/div[1]/div[1]/input[1]").send_keys("Hsr layout 5th main 23 cross bangalor")
time.sleep(2)

# date of birth
bday = drive.find_element(By.XPATH,"(//input[@id='standard-basic'])[1]")
print("bday.....",bday)
# to select pre date and then we can pass    : send_keys("12/08/1994") if we didnot select means we cant type
bday.send_keys(Keys.CONTROL+'a')
time.sleep(1)
bday.send_keys("12/08/1994")
time.sleep(2)

# linkedin url
drive.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/form/div[10]/div/div[2]/div[1]/div/div/input").send_keys("https://www.linkedin.com/in/gowtham-p-472683201/")
time.sleep(1)


#click on submit
drive.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/form/div[11]/div/button").click()
time.sleep(2)
# # add bio in that enter url
# drive.find_element(By.XPATH,"//*[@id='mui-2']").send_keys("https://www.linkedin.com/in/gowtham-p-472683201/")
# time.sleep(1)
#
# # click and write , start typing here
# drive.find_element(By.XPATH,"//*[@id='mui-3']").send_keys("Executive Courses Harvard Results from 6 Search Engines. Search Executive Courses Harvard. Search Quality Answers Now. Get The Best Result With ZapMeta About Quality Answers Now. Information 24/7. 100+ Million Visitors. ")
# time.sleep(1)
# #click on submit button
# drive.find_element(By.XPATH,"//*[@id='root']/div/div/div/div[4]/div[2]/div/div/button").click()
# time.sleep(1)
#
#
# # click on chooce your intrest
# drive.find_element(By.XPATH,"//div[@class='MuiBox-root css-1dcj1qe']/div[2]").click()
# time.sleep(1)
# drive.find_element(By.XPATH,"//div[@class='MuiBox-root css-1dcj1qe']/div[3]").click()
# time.sleep(1)
# drive.find_element(By.XPATH,"//div[@class='MuiBox-root css-1dcj1qe']/div[4]").click()
# time.sleep(2)
# # click on submit
# drive.find_element(By.XPATH,"//*[@id='root']/div/div/div/div[2]/div[4]/div/button").click()

# it reach home page done