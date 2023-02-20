

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
time.sleep(20)



# click on club detail
drive.find_element(By.XPATH,"(//img[@class='MuiCardMedia-root MuiCardMedia-media MuiCardMedia-img css-y2tkt7'])[2]").click()
time.sleep(10)

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


# click  on like
drive.find_element(By.XPATH,"(//*[name()='svg'][@fill='#ffffff'])[12]").click()
time.sleep(10)

# click on comment
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div[2]/div[1]/div/div[4]/div/div[2]/div/button/div/img").click()
time.sleep(10)

# type here msg
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div[2]/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/textarea[1]").send_keys("CHHATTISGARH STATE POWER DISTRIBUTION COMPANY LIMITED (CSPDCL) has floated a tender for Supply of Medicines (Indented with Generic Names) for Day to Day Requirement of Cspdcl Dispensary at Gudhiyari Raipur for the Year 2022-23. The project location is Raipur, Chhattisgarh, India. The reference number is - and it is closing on 19 Oct 2022. Suppliers can request Register free of cost to get the complete Tender details and download the document.")
time.sleep(2)


# click on post msg
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div[2]/div[1]/div/div[5]/div/div/div[1]/div/div[3]/div/div/button").click()
time.sleep(10)

# click on 3 dot
drive.find_element(By.XPATH,"(//*[name()='path'])[38]").click()
time.sleep(10)

# click on delet
drive.find_element(By.XPATH,"//span[normalize-space()='Delete']").click()
time.sleep(10)


# click on yes delet
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div[2]/div[2]/div[2]/div/button").click()
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
time.sleep(10)

# write a option 2
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/form/div[2]/div/div[2]/div/div/div/input").send_keys("No")
time.sleep(10)

# click on add another option
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/form/div[3]/div[1]/h6").click()
time.sleep(3)


# write a option 3
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/form/div[3]/div/div[2]/div/div/div/input").send_keys("Nor")
time.sleep(10)

# click on add another option
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/form/div[4]/div[1]/h6").click()
time.sleep(3)

# write a option 4
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/form/div[4]/div/div[2]/div/div/div/input").send_keys("Both")
time.sleep(10)


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
time.sleep(10)

drive.refresh()
time.sleep(10)


# click  on like
drive.find_element(By.XPATH,"(//div[@class='MuiBox-root css-1jx63vg'])[1]").click()
time.sleep(10)
#
# click on comment
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div[2]/div[1]/div/div[3]/div/div[2]/div/button/div/img").click()
time.sleep(10)

# type here msg
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div[2]/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/textarea[1]").send_keys("CHHATTISGARH STATE POWER DISTRIBUTION COMPANY LIMITED (CSPDCL) has floated a tender for Supply of Medicines (Indented with Generic Names) for Day to Day Requirement of Cspdcl Dispensary at Gudhiyari Raipur for the Year 2022-23. The project location is Raipur, Chhattisgarh, India. The reference number is - and it is closing on 19 Oct 2022. Suppliers can request Register free of cost to get the complete Tender details and download the document.")
time.sleep(2)


# click on post msg
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div[2]/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div/div/button").click()
time.sleep(10)

# click on vote
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[1]/div/div[2]/div[1]/div/div[2]/div/div/div[1]/div[3]/label/span/input").click()
time.sleep(10)

# click on 3 dot
drive.find_element(By.XPATH,"(//*[name()='path'])[38]").click()
time.sleep(10)

# click on delet
drive.find_element(By.XPATH,"//span[normalize-space()='Delete']").click()
time.sleep(10)

# drive.find_element(By.CLASS_NAME)

# click on yes delet
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div[2]/div[2]/div[2]/div/button").click()
time.sleep(2)

drive.refresh()
time.sleep(10)