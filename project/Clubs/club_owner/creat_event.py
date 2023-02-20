

from project.Common.initial import *
drive = commonlogin()
time.sleep(5)

# click on 3 line
drive.find_element(By.XPATH,"//button[@aria-label='account of current user']//*[name()='svg']//*[name()='path' and contains(@d,'M3 18h18v-')]").click()
time.sleep(2)

# click on club
drive.find_element(By.XPATH,"/html/body/div[2]/div[3]/ul/ul[1]/li[1]").click()
time.sleep(5)


# click on see more
drive.find_element(By.XPATH,"(//h5[@class='MuiTypography-root MuiTypography-h5 css-15jga2m'][normalize-space()='See All'])[1]").click()
time.sleep(5)



#
# # click on invite
# drive.find_element(By.XPATH,"(//img[@alt='Comment'])[4]").click()
# time.sleep(7)
#
# # then click on drop down
# drive.find_element(By.XPATH,"//div[@id='demo-simple-select']").click()
# time.sleep(8)
#
# #click on opend drop down full form
# act_category=drive.find_element(By.XPATH,"//ul[@role='listbox']")
#
#
# #select a option
# drive.find_element(By.XPATH,"//li[1]//span[1]//input[1]").click()
# time.sleep(4)
#
# act_category.send_keys(Keys.ESCAPE)
#
# #click on share button
# drive.find_element(By.XPATH,"(//button[normalize-space()='Send'])[1]").click()
# time.sleep(10)

# click on edit
drive.find_element(By.XPATH,"//body[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/button[1]").click()
time.sleep(10)




# click on camera and add img
drive.find_element(By.XPATH,"//input[@id='icon-button-file']").send_keys("C:/Users/GOWTHAM/Downloads/img3.jpg")
time.sleep(2)

# Title
Title=drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div[2]/div/form/div[1]/div[2]/div/div[1]/div/div/input")
Title.send_keys(Keys.CONTROL+'a')
Title.send_keys("Sugar Chasers")
time.sleep(2)

time.sleep(5)

# Detail
Detail=drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div[2]/div/form/div[3]/div[2]/div/div[1]/div/textarea[1]")
Detail.send_keys(Keys.CONTROL+'a')
Detail.send_keys("CHHATTISGARH STATE POWER pply of Medicines (Indented" )
time.sleep(2)
#
# #  click on online
# drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div[2]/div/form/div[7]/div[2]/div/div/div/label[1]/span[1]/input").click()
# time.sleep(5)


 #Industry Drop Down radio button
drive.find_element(By.XPATH,"(//div[@id='demo-simple-select'])[2]").click()
time.sleep(6)

#click on opend drop down full form
act_ind = drive.find_element(By.XPATH,"(//div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx'])[2]")


#print("act_ind......",act_ind)

# selection multipal optation
# drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[4]").click()
# time.sleep(1)
drive.find_element(By.XPATH,"//li[1]//span[1]//input[1]").click()
time.sleep(1)
drive.find_element(By.XPATH,"//li[1]//span[1]//input[1]").click()
act_ind.send_keys(Keys.ESCAPE)

#function Drop Down radio button

drive.find_element(By.XPATH,"(//div[@id='demo-simple-select'])[3]").click()
time.sleep(2)

#click on opend drop down full form
act_fun=drive.find_element(By.XPATH,"//ul[@role='listbox']")

# select option
drive.find_element(By.XPATH,"//li[1]//span[1]//input[1]").click()
time.sleep(1)
drive.find_element(By.XPATH,"(//input[@type='checkbox'])[6]").click()
time.sleep(1)
drive.find_element(By.XPATH,"(//input[@type='checkbox'])[9]").click()
# passing escape key
act_fun.send_keys(Keys.ESCAPE)

time.sleep(5)

# click on category
drive.find_element(By.XPATH,"(//div[@id='demo-simple-select'])[4]").click()
time.sleep(5)

# select an optation
drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li[3]").click()
time.sleep(3)



# click on uppdate button
drive.find_element(By.XPATH,"(//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root css-1pi4f66'][normalize-space()='Update'])[1]").click()
time.sleep(20)


# click on see more
drive.find_element(By.XPATH,"(//h5[@class='MuiTypography-root MuiTypography-h5 css-15jga2m'][normalize-space()='See All'])[1]").click()
time.sleep(20)



# click on club detail
drive.find_element(By.XPATH,"//body[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/img[1]").click()
time.sleep(10)

# click on members
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div[1]/div/div[2]/div[1]/div[3]/div[1]/div/div/button").click()
time.sleep(10)

# click no invited
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[1]/div/button[2]/div/h5[1]").click()
time.sleep(5)

# click no  unsend
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div[3]/div/div/div[3]/div/div/div/button").click()
time.sleep(5)

drive.refresh()
time.sleep(5)



# click no requiested
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[1]/div/button[1]/div/h5[1]").click()
time.sleep(2)

# click no accept
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/div/div[1]/div/div/div[3]/div/div[1]/div/button").click()
time.sleep(10)

# click no ignor
drive.find_element(By.XPATH,"//*[@id='mui-1-P-0]'/div/div/div/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/button").click()
time.sleep(10)



drive.back()
time.sleep(7)


drive.refresh()
time.sleep(10)

# click no create event
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div/div/button").click()
time.sleep(10)





# click on camera and add img
drive.find_element(By.XPATH,"//input[@id='icon-button-file']").send_keys("E:/event 2img.jpg")
time.sleep(2)

# Title
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div[2]/div/form/div[1]/div[2]/div/div[1]/div/div/input").send_keys("Coffee Obsession")
time.sleep(5)

# Detail
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div[2]/div/form/div[3]/div[2]/div/div[1]/div/textarea[1]").send_keys("CHHATTISGARH STATE POWER DISTRIBUTION COMPANY LIMITED (CSPDCL) has floated a tender for Supply of Medicines (Indented with Generic Names) for Day to Day Requirement of Cspdcl Dispensary at Gudhiyari Raipur for the Year 2022-23. The project location is Raipur, Chhattisgarh, India. The reference number is - and it is closing on 19 Oct 2022. Suppliers can request Register free of cost to get the complete Tender details and download the document.")
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



#  click on online
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div[2]/div/form/div[7]/div[2]/div/div/div/label[1]/span[1]/input").click()
time.sleep(5)


# click on event  link
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div[2]/div/form/div[8]/div[2]/div/div[1]/div/div/input").send_keys("https://allevents.in/bangalore")
time.sleep(5)



# click on free radio button
drive.find_element(By.XPATH,"//*[@id='root']/div[2]/div/main/div/div/div[2]/div/div[2]/div/form/div[9]/div[4]/label/span[1]/input").click()
time.sleep(5)


# event start_date
start_date=drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div[2]/div/form/div[10]/div[2]/div/div/div/input")
start_date.send_keys(Keys.CONTROL+'a')
start_date.send_keys("11/11/2022")
time.sleep(2)

# event start_time
start_time=drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div[2]/div/form/div[10]/div[4]/div/div/div/input")
start_time.send_keys(Keys.CONTROL+'a')
start_time.send_keys("10:00 AM")
time.sleep(2)

# event End_date
End_date=drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div[2]/div/form/div[11]/div[2]/div/div/div/input")
End_date.send_keys(Keys.CONTROL+'a')
End_date.send_keys("12/31/2022")
time.sleep(2)

# event End_time
End_time=drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div[2]/div/form/div[11]/div[4]/div/div/div/input")
End_time.send_keys(Keys.CONTROL+'a')
End_time.send_keys("04:00 PM")
time.sleep(2)

# Email
Email=drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div[2]/div/form/div[12]/div[2]/div/div[1]/div/div/input")
Email.send_keys(Keys.CONTROL+'a')
Email.send_keys("kprabhat956@gmail.com")
time.sleep(2)


# click on submit button
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div[2]/div/form/div[14]/div/button").click()
time.sleep(10)



# click  on create post
drive.find_element(By.XPATH,"(//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root css-1pi4f66'][normalize-space()='Create Post'])[1]").click()
time.sleep(5)

# click on create a post
drive.find_element(By.XPATH,"(//h6[normalize-space()='Create a post'])[1]").click()
time.sleep(3)

# Detail
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div[2]/div/div/textarea[1]").send_keys("CHHATTISGARH STATE POWER DISTRIBUTION COMPANY LIMITED (CSPDCL) has floated a tender for Supply of Medicines (Indented with Generic Names) for Day to Day Requirement of Cspdcl Dispensary at Gudhiyari Raipur for the Year 2022-23. The project location is Raipur, Chhattisgarh, India. The reference number is - and it is closing on 19 Oct 2022. Suppliers can request Register free of cost to get the complete Tender details and download the document.")
time.sleep(2)


# click on add img
drive.find_element(By.XPATH,"//input[@id='icon-button-image']").send_keys("E:/event 2img.jpg")
time.sleep(2)


# click on  document
drive.find_element(By.XPATH,"//input[@id='icon-button-image']").send_keys("E:/th (4).jpg")
time.sleep(2)


# click on post
drive.find_element(By.XPATH,"//button[normalize-space()='Post']").click()
time.sleep(10)


# click  on like
drive.find_element(By.XPATH,"(//*[name()='svg'][@fill='#ffffff'])[12]").click()
time.sleep(10)

# click on comment
drive.find_element(By.XPATH,"(//img[@alt='Comment'])[1]").click()
time.sleep(10)

# type here msg
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div[2]/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/textarea[1]").send_keys("CHHATTISGARH STATE POWER DISTRIBUTION COMPANY LIMITED (CSPDCL) has floated a tender for Supply of Medicines (Indented with Generic Names) for Day to Day Requirement of Cspdcl Dispensary at Gudhiyari Raipur for the Year 2022-23. The project location is Raipur, Chhattisgarh, India. The reference number is - and it is closing on 19 Oct 2022. Suppliers can request Register free of cost to get the complete Tender details and download the document.")
time.sleep(2)


# click on post msg
drive.find_element(By.XPATH,"(//button[normalize-space()='Post'])[1]").click()
time.sleep(10)

# click on 3 dot
drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[7]").click()
time.sleep(10)

# click on edit
drive.find_element(By.XPATH,"//span[normalize-space()='Edit']").click()
time.sleep(10)

# type here msg
End_date =drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div[2]/div[1]/div/div[4]/div/div/div[2]/div/div[2]/div/div/div/textarea[1]")
End_date.send_keys(Keys.CONTROL+'a')
End_date.send_keys("Dummy text consisting of lorem ipsum is useful when as a placeholder text in UI design, web design.")
time.sleep(2)


# click on save
drive.find_element(By.XPATH,"//button[normalize-space()='Save']").click()
time.sleep(10)


# click on 3 dot
drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[7]").click()
time.sleep(10)


# delet the comment
drive.find_element(By.XPATH,"//span[normalize-space()='Delete']").click()
time.sleep(10)

# # click on yes
# drive.find_element(By.XPATH,"//button[normalize-space()='Yes']").click()
# time.sleep(10)



# click on 3 dot
drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[5]").click()
time.sleep(10)


# delet the post
drive.find_element(By.XPATH,"(//span[@class='MuiTypography-root MuiTypography-body1 MuiListItemText-primary css-2w5ikc'][normalize-space()='Delete'])[1]").click()
time.sleep(10)

# click on yes
drive.find_element(By.XPATH,"//button[normalize-space()='Yes']").click()
time.sleep(10)

drive.refresh()