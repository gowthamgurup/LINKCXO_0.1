

from project.Common.initial import *
drive = commonlogin()
time.sleep(5)

# click on 3 line
drive.find_element(By.XPATH,"//button[@aria-label='account of current user']//*[name()='svg']//*[name()='path' and contains(@d,'M3 18h18v-')]").click()
time.sleep(2)

# click on club
drive.find_element(By.XPATH,"/html/body/div[2]/div[3]/ul/ul[1]/li[1]").click()
time.sleep(10)


# click on member
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[1]/div/button[3]/div/div/h5[1]").click()
time.sleep(10)



# click on share
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[4]/div/div/div/div[1]/div[2]/div/div/div/div/div[2]/div/div[2]/div/button/div/img").click()
time.sleep(5)


# click on img
drive.find_element(By.XPATH,"(//img[@alt='logo'])[2]").click()
time.sleep(5)

# click on drop down
drive.find_element(By.XPATH,"//div[@id='demo-simple-select']").click()
time.sleep(5)

#click on opend drop down full form
act_invite = drive.find_element(By.XPATH,"(//ul[@role='listbox'])[1]")

# select optaiton
drive.find_element(By.XPATH,"//li[1]//span[1]//input[1]").click()
# drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li[2]/span[1]/input").click()
# drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li[3]/span[1]/input").click()
#drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li[4]/span[1]/input").click()
time.sleep(2)

act_invite.send_keys(Keys.ESCAPE)
time.sleep(5)

# click on send
drive.find_element(By.XPATH,"(//button[normalize-space()='Share'])[1]").click()
time.sleep(5)




# click on img
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div/div[4]/div/div/div/div[1]/div[2]/div/div[2]/div/div/div[1]/div/img").click()
time.sleep(5)


# click on 3 dot
drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[4]").click()
time.sleep(2)

report=drive.find_element(By.XPATH,"//span[normalize-space()='Report']")
report.click()
time.sleep(2)

# select optaiton
drive.find_element(By.XPATH,"//input[@name='Inappropriate']").click()
drive.find_element(By.XPATH,"//input[@name='Harassment']").click()
drive.find_element(By.XPATH,"//input[@name='False_Information']").click()
drive.find_element(By.XPATH,"//input[@name='Intellectual_Property']").click()
time.sleep(2)

# type here
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div[3]/div/div/textarea[1]").send_keys("It is a sequence of Latin words that, as they are positioned, do not form sentences with a complete sense, but give life to a test text useful to fill spaces that will subsequently be occupied from ad hoc texts composed by communication professionals.")
time.sleep(8)


# click on send
drive.find_element(By.XPATH,"//*[@id='root']/div[2]/div/div/div/div[4]/div/button").click()
time.sleep(10)

# click on 3 dot
drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[4]").click()
time.sleep(2)

# click on bookmark
drive.find_element(By.XPATH,"(//*[name()='svg'])[20]").click()
time.sleep(10)


# click on member
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div/div/button").click()
time.sleep(10)


drive.refresh()
time.sleep(5)

drive.back()
time.sleep(10)




# click no create event
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div/div/button").click()
time.sleep(5)


# click on camera and add img
drive.find_element(By.XPATH,"//input[@id='icon-button-file']").send_keys("C:/Users/GOWTHAM/Downloads/img2.jpg")
time.sleep(2)

# Title
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div[2]/div/form/div[1]/div[2]/div/div[1]/div/div/input").send_keys("The Proud Nerds")
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
start_date.send_keys("01/11/2023")
time.sleep(2)

# event start_time
start_time=drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div[2]/div/form/div[10]/div[4]/div/div/div/input")
start_time.send_keys(Keys.CONTROL+'a')
start_time.send_keys("10:00 AM")
time.sleep(2)

# event End_date
End_date=drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div[2]/div/div[2]/div/form/div[11]/div[2]/div/div/div/input")
End_date.send_keys(Keys.CONTROL+'a')
End_date.send_keys("12/31/2024")
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
time.sleep(5)








# click  on create post
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div[1]/div/div[3]/div/div[2]/div/div/button").click()
time.sleep(5)

# click on create a post
drive.find_element(By.XPATH,"(//h6[normalize-space()='Create a post'])[1]").click()
time.sleep(3)

# Detail
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div[2]/div/div/textarea[1]").send_keys("STATE POWER  tender for Supply of MedicinesCroad the document.")
time.sleep(2)


# click on add img
drive.find_element(By.XPATH,"//input[@id='icon-button-image']").send_keys("C:/Users/GOWTHAM/Downloads/img4.jpg")
time.sleep(2)


# # click on  document
# drive.find_element(By.XPATH,"//input[@id='icon-button-image']").send_keys("C:/Users/GOWTHAM/Downloads/sample pdf.pdf")
# time.sleep(2)


# click on post
drive.find_element(By.XPATH,"//button[normalize-space()='Post']").click()
time.sleep(5)


# click  on like
drive.find_element(By.XPATH,"(//*[name()='svg'][@fill='#ffffff'])[13]").click()
time.sleep(5)

# click on comment
drive.find_element(By.XPATH,"(//img[@alt='Comment'])[1]").click()
time.sleep(5)

# type here msg
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div[2]/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/textarea[1]").send_keys("CHHATTISGARH STATE POWER DISTRIBUTION COMPANYesd the document.")
time.sleep(2)


# click on post msg
drive.find_element(By.XPATH,"(//button[normalize-space()='Post'])[1]").click()
time.sleep(5)

drive.refresh()
time.sleep(10)

# click on comment
drive.find_element(By.XPATH,"(//img[@alt='Comment'])[1]").click()
time.sleep(5)


# # scroll up which we given requiested
element = drive.find_element(By.XPATH,"(//div[@class='MuiCardContent-root css-1qw96cp'])[1]")
time.sleep(2)
actions = ActionChains(drive)
time.sleep(2)
actions.move_to_element(element).perform()
time.sleep(5)




# click on 3 dot
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div[2]/div/div/div[4]/div/div/div[2]/div[1]/div[1]/div[3]/div/button").click()
time.sleep(5)

# click on edit
drive.find_element(By.XPATH,"//span[normalize-space()='Edit']").click()
time.sleep(5)

# type here msg
End_date =drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div[2]/div[1]/div/div[4]/div/div/div[2]/div/div[2]/div/div/div/textarea[1]")
End_date.send_keys(Keys.CONTROL+'a')
End_date.send_keys("Dummy text consisting of lorem ipsum is useful when as a placeholder text in UI design, web design.")
time.sleep(2)


# click on save
drive.find_element(By.XPATH,"//button[normalize-space()='Save']").click()
time.sleep(5)


# click on 3 dot
drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[7]").click()
time.sleep(5)


# delet the comment
drive.find_element(By.XPATH,"//span[normalize-space()='Delete']").click()
time.sleep(5)

# # click on yes
# drive.find_element(By.XPATH,"//button[normalize-space()='Yes']").click()
# time.sleep(10)



# click on 3 dot
drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[5]").click()
time.sleep(5)


# delet the post
drive.find_element(By.XPATH,"(//span[@class='MuiTypography-root MuiTypography-body1 MuiListItemText-primary css-2w5ikc'][normalize-space()='Delete'])[1]").click()
time.sleep(5)

# click on yes
drive.find_element(By.XPATH,"//button[normalize-space()='Yes']").click()
time.sleep(5)

drive.refresh()
time.sleep(5)




# click  on create post
drive.find_element(By.XPATH,"(//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root css-1pi4f66'][normalize-space()='Create Post'])[1]").click()
time.sleep(5)



# click on compose artical
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div[1]/div/div/div/div[2]/div[2]/div[2]").click()
time.sleep(3)

# write artical name
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div[2]/div/div/textarea[1]").send_keys("CHHATTISGARH STATE .")
time.sleep(2)

# write artical detail
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div[3]/div/div/textarea[1]").send_keys("CHHATTISGARH STATE POWER DISTRIBUTION COMPANY LIMITED (CSPDCL) has floated a tender for Supply of Medicines (Indented with Generic Names) for Day to Day Requirement of Cspdcl Dispensary at Gudhiyari Raipur for the Year 2022-23. The project location is Raipur, Chhattisgarh, India. The reference number is - and it is closing on 19 Oct 2022. Suppliers can request Register free of cost to get the complete Tender details and download the document.")
time.sleep(2)

# click on post
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div[4]/div/button").click()
time.sleep(5)


# # scroll up which we given requiested
element = drive.find_element(By.XPATH,"(//div[@class='MuiCardActions-root css-p0pzb2'])[1]")
actions = ActionChains(drive)
actions.move_to_element(element).perform()
time.sleep(5)




# click  on like  (//button[@aria-label='applause'])[1]
drive.find_element(By.XPATH,"(//*[name()='path'][@class='cls-1'])[32]").click()
time.sleep(5)

# click on comment
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div[2]/div[1]/div/div[4]/div/div[2]/div/button/div/img").click()
time.sleep(5)

# type here msg
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div[2]/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/textarea[1]").send_keys("CHHATTISGARH STATE POWER DISTRIBUTION COMPANY LIMITED (CSPDCL) has floated a tender for Supply of Medicines (Indented with Generic Names) for Day to Day Requirement of Cspdcl Dispensary at Gudhiyari Raipur for the Year 2022-23. The project location is Raipur, Chhattisgarh, India. The reference number is - and it is closing on 19 Oct 2022. Suppliers can request Register free of cost to get the complete Tender details and download the document.")
time.sleep(2)


# click on post msg
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div[2]/div[1]/div/div[5]/div/div/div[1]/div/div[3]/div/div/button").click()
time.sleep(5)

drive.refresh()
time.sleep(5)

# click on 3 dot
drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[5]").click()
time.sleep(5)

# click on delet
drive.find_element(By.XPATH,"//span[normalize-space()='Delete']").click()
time.sleep(5)


# click on yes delet
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div[2]/div[2]/div[2]/div/button").click()
time.sleep(5)

drive.refresh()
time.sleep(10)



# click  on create post
drive.find_element(By.XPATH,"(//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root css-1pi4f66'][normalize-space()='Create Post'])[1]").click()
time.sleep(5)




# click on poll
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div[1]/div/div/div/div[2]/div[3]/div[2]/h6").click()
time.sleep(3)

# write a poll question
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div[2]/div[1]/div/textarea[1]").send_keys("will it rain today")
time.sleep(3)


# write a option 1
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/form/div[1]/div/div[2]/div/div/div/input").send_keys("Yes")
time.sleep(3)

# write a option 2
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/form/div[2]/div/div[2]/div/div/div/input").send_keys("No")
time.sleep(3)

# click on add another option
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/form/div[3]/div[1]/h6").click()
time.sleep(3)


# write a option 3
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/form/div[3]/div/div[2]/div/div/div/input").send_keys("Nor")
time.sleep(3)

# click on add another option
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/form/div[4]/div[1]/h6").click()
time.sleep(3)

# write a option 4
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/form/div[4]/div/div[2]/div/div/div/input").send_keys("Both")
time.sleep(5)


# click on add Remove option
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/form/div[5]/div[2]/h6").click()
time.sleep(3)


# click on select day or week
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/form/div[5]/div/div[2]/div/div/div").click()
time.sleep(3)

# click on select 1 week
drive.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li[3]").click()
time.sleep(3)


# click on post
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/form/div[6]/div[2]/div/div[1]/div/button").click()
time.sleep(5)


# click  on like
drive.find_element(By.XPATH,"(//*[name()='svg'][@fill='#ffffff'])[12]").click()
time.sleep(5)
#
# click on comment
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div[2]/div[1]/div/div[3]/div/div[2]/div/button/div/img").click()
time.sleep(5)

# type here msg
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div[2]/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/textarea[1]").send_keys("CHHATTISGARH STATE POWER DISTRIBUTION COMPANY LIMITED (CSPDCL) has floated a tender for Supply of Medicines (Indented with Generic Names) for Day to Day Requirement of Cspdcl Dispensary at Gudhiyari Raipur for the Year 2022-23. The project location is Raipur, Chhattisgarh, India. The reference number is - and it is closing on 19 Oct 2022. Suppliers can request Register free of cost to get the complete Tender details and download the document.")
time.sleep(2)


# click on post msg
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div[2]/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div/div/button").click()
time.sleep(5)

# click on vote
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div[2]/div[1]/div/div[2]/div/div/div[1]/div/label/span/input").click()
time.sleep(5)

# click on like
drive.find_element(By.XPATH,"(//*[name()='svg'][@fill='#ffffff'])[13]").click()
time.sleep(2)


# click on 3 dot
drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[5]").click()
time.sleep(5)

# click on delet
drive.find_element(By.XPATH,"//span[normalize-space()='Delete']").click()
time.sleep(5)

# drive.find_element(By.CLASS_NAME)

# click on yes delet
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div[2]/div[2]/div[2]/div/button").click()
time.sleep(2)

drive.refresh()
time.sleep(5)






# ## its not completed because bug is there in  cancel requiest ,and need to add remove button in member
# #
# # click on member
# drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div/div/button").click()
# time.sleep(10)
#
#
# # click on remove
# drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div/div/button").click()
# time.sleep(10)
#
#
# drive.refresh()
# time.sleep(5)

# drive.back()
# time.sleep(10)



# click on leave club
drive.find_element(By.XPATH,"(//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root css-1pi4f66'][normalize-space()='Leave'])[1]").click()
time.sleep(10)