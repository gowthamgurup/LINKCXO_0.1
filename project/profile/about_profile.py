from project.Common.initial import *
drive = commonlogin()
time.sleep(2)


# click on profile
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/aside[1]/div/div[1]/div/div[1]/div/img").click()
time.sleep(2)

#scroll down about
element = drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div/div/div/div[4]/div[1]")
actions = ActionChains(drive)
actions.move_to_element(element).perform()
time.sleep(5)


# click on skill
drive.find_element(By.XPATH,"(//div[@class='css-vfjav4'])[1]").click()
time.sleep(2)

# click on add slill
drive.find_element(By.XPATH," (//div[@class='css-vb6e92'])[1]").click()
time.sleep(2)


# click on add
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div/div[2]/div[1]/div/div[1]/div/input").send_keys("Django")
time.sleep(2)

# click on save
drive.find_element(By.XPATH,"(//button[normalize-space()='Save'])[1]").click()
time.sleep(2)

# click on skill
drive.find_element(By.XPATH,"(//div[@class='css-vfjav4'])[1]").click()
time.sleep(2)

# click on interest
drive.find_element(By.XPATH,"(//div[@class='css-vfjav4'])[2]").click()
time.sleep(2)

# click on add  interest
drive.find_element(By.XPATH,"(//div[contains(@class,'css-vb6e92')])[2]").click()
time.sleep(2)


# click on add
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div/div[2]/div[1]/div/div/input").send_keys("Fund Raise")
time.sleep(2)


# click on save
drive.find_element(By.XPATH,"(//button[normalize-space()='Submit'])[1]").click()
time.sleep(2)

#  Again click on interest
drive.find_element(By.XPATH,"(//div[@class='css-vfjav4'])[2]").click()
time.sleep(2)


# click on industry
drive.find_element(By.XPATH,"(//div[@class='css-vfjav4'])[3]").click()
time.sleep(2)



 #Industry
drive.find_element(By.XPATH,"(//div[contains(@class,'css-vb6e92')])[3]").click()
time.sleep(5)

# click on drop down
drive.find_element(By.XPATH,"//div[@id='demo-simple-select']").click()
time.sleep(2)

#click on opend drop down full form
act_ind = drive.find_element(By.XPATH,"/html/body/div[3]/div[3]")


#print("act_ind......",act_ind)

# selection multipal optation
# drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[4]").click()
# time.sleep(1)
drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[2]").click()
time.sleep(1)
drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[3]").click()
act_ind.send_keys(Keys.ESCAPE)

# click on save
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div/div[2]/div[2]/div/div/div/button").click()
time.sleep(5)

# click on *
drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-m4t9js'])[1]").click()
time.sleep(5)

#  again click on industry
drive.find_element(By.XPATH,"(//div[@class='css-vfjav4'])[3]").click()
time.sleep(2)



#function
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div/div/div/div[4]/div[2]/div/p/div[4]/div/div[1]/div[1]/div").click()
time.sleep(3)

# click on add
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div/div/div/div[4]/div[2]/div/p/div[4]/div/div[1]/div[1]/div/div[2]").click()
time.sleep(2)

# click on click on drop down
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div/div[2]/div[1]/div/div/div[2]/div/div/div").click()
time.sleep(2)

#click on opend drop down full form
act_fun=drive.find_element(By.XPATH,"/html/body/div[3]/div[3]")

# select option
drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[1]/span").click()
time.sleep(1)
drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[3]/span").click()
time.sleep(1)
drive.find_element(By.XPATH,"//div[@id='menu-']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-zzhupx']/ul/li[4]/span").click()
# passing escape key
act_fun.send_keys(Keys.ESCAPE)

# click on save
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div/div[2]/div[3]/div/div/div/button").click()
time.sleep(3)

# click on *
drive.find_element(By.XPATH,"(//*[name()='svg'][contains(@class,'MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-m4t9js')])[1]").click()
time.sleep(5)

#  again  function
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div/div/div/div/div[4]/div[2]/div/p/div[4]/div/div[1]/div[1]/div").click()
time.sleep(3)


# click on experince
drive.find_element(By.XPATH,"//body[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/p[1]/div[5]/div[1]/div[1]/div[1]/div[1]").click()
time.sleep(3)


# click on add experince
drive.find_element(By.XPATH,"//body[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/p[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]").click()
time.sleep(2)

# click on company
drive.find_element(By.XPATH,"(//input[@id='input-with-sx'])[1]").send_keys("Linkcxo")
time.sleep(2)

# click on designation
drive.find_element(By.XPATH,"//div[@class='MuiBox-root css-zxiogw']//div[@class='MuiFormControl-root MuiFormControl-fullWidth css-tzsjye']//div[1]//div[1]").click()
time.sleep(2)

# click on raduo button
drive.find_element(By.XPATH,"//li[1]//span[1]//input[1]").click()
time.sleep(2)

# click on industry
drive.find_element(By.XPATH,"//body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
time.sleep(2)

# click on raduo button
drive.find_element(By.XPATH,"//li[@name='Startup / VCs/ PEs']//input[@type='checkbox']").click()
time.sleep(2)

# click on function
drive.find_element(By.XPATH,"//body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
time.sleep(2)

# click on raduo button
drive.find_element(By.XPATH,"//li[1]//span[1]//input[1]").click()
time.sleep(2)


# click on address
drive.find_element(By.XPATH,"(//input[@id='input-with-sx'])[2]").send_keys("Hsr layout ")
time.sleep(2)




#click on address name
address =drive.find_element(By.XPATH,"//body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[6]/div[1]/div[2]/div[1]/input[1]")
address.send_keys(Keys.CONTROL+'a')
address.send_keys("02/10/2019")
time.sleep(2)

#click on address name
address =drive.find_element(By.XPATH,"//body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[7]/div[1]/div[2]/div[1]/input[1]")
address.send_keys(Keys.CONTROL+'a')
address.send_keys("10/10/2021")
time.sleep(2)


# click on raduo button still working  ( NO )
drive.find_element(By.XPATH,"(//input[contains(@name,'row-radio-buttons-group')])[2]").click()
time.sleep(2)

# click on address
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div/div[2]/div/div/div/div/div/form/div[9]/div/div[2]/div/textarea[1]").send_keys("Lorem Ipsum is simply dummy text of the printing and typesetting industry. ")
time.sleep(2)


# click on ADD
drive.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(2)

# click on delet
drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-colorSecondary MuiSvgIcon-fontSizeMedium css-1m9optw'])[1]").click()
time.sleep(2)

# click on experince
drive.find_element(By.XPATH,"//body[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/p[1]/div[5]/div[1]/div[1]/div[1]/div[1]").click()
time.sleep(3)


# click on Education
drive.find_element(By.XPATH,"(//div[@class='css-vfjav4'])[6]").click()
time.sleep(2)


# click on add Education
drive.find_element(By.XPATH,"//body[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/p[1]/div[6]/div[1]/div[1]/div[1]/div[1]/div[2]").click()
time.sleep(2)

# click on board
drive.find_element(By.XPATH,"(//input[@id='input-with-sx'])[1]").send_keys("bihar")
time.sleep(2)


# click on degree
drive.find_element(By.XPATH,"(//input[@id='input-with-sx'])[2]").send_keys("MCA")
time.sleep(2)


#click on address name
address =drive.find_element(By.XPATH,"//input[@id='standard-basic']")
address.send_keys(Keys.CONTROL+'a')
address.send_keys("2021")
time.sleep(2)


# click on DEAIL
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div/div[2]/div/div/div/div/form/div[4]/div/div[2]/div/textarea[1]").send_keys("It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.")
time.sleep(2)


# click on ADD
drive.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(2)

# click on delet
drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-colorSecondary MuiSvgIcon-fontSizeMedium css-1m9optw'])[2]").click()
time.sleep(2)


# click on affiliation
drive.find_element(By.XPATH,"(//div[@class='css-vfjav4'])[7]").click()
time.sleep(2)

# click on ADD affiliation
drive.find_element(By.XPATH,"//body[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/p[1]/div[7]/div[1]/div[1]/div[1]/div[1]/div[2]").click()
time.sleep(2)


# click on name
drive.find_element(By.XPATH,"(//input[@id='input-with-sx'])[1]").send_keys("prabath")
time.sleep(2)

# click on role
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div/div[2]/div/div/div/div/form/div[2]/div/div[2]/div/div/input").send_keys("test Engineer")
time.sleep(2)

#click on address name
address =drive.find_element(By.XPATH,"//body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/form[1]/div[3]/div[1]/div[2]/div[1]/input[1]")
address.send_keys(Keys.CONTROL+'a')
address.send_keys("02/10/2017")
time.sleep(2)

#click on address name
address =drive.find_element(By.XPATH,"//body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/form[1]/div[4]/div[1]/div[2]/div[1]/input[1]")
address.send_keys(Keys.CONTROL+'a')
address.send_keys("10/10/2019")
time.sleep(2)


# click on role
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div/div[2]/div/div/div/div/form/div[5]/div/div[2]/div/textarea[1]").send_keys("Lorem Ipsum is simply dummy text of the printing and typesetting industry")
time.sleep(2)


# click on ADD
drive.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(2)


# click on delet
drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-colorSecondary MuiSvgIcon-fontSizeMedium css-1m9optw'])[4]").click()
time.sleep(2)

# click on award and certification
drive.find_element(By.XPATH,"(//div[@class='css-vfjav4'])[8]").click()
time.sleep(2)

# click on ADD
drive.find_element(By.XPATH,"//body[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/p[1]/div[8]/div[1]/div[1]/div[1]/div[1]/div[2]").click()
time.sleep(2)

# click on name
drive.find_element(By.XPATH,"(//input[@id='input-with-sx'])[1]").send_keys("national")
time.sleep(2)

# click on by
drive.find_element(By.XPATH,"(//input[@id='input-with-sx'])[2]").send_keys("bihar")
time.sleep(2)

# click on detail
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div/div[2]/div/div/div/div/form/div[3]/div/div[2]/div/textarea[1]").send_keys("Contrary to popular belief, Lorem Ipsum is not simply random text")
time.sleep(2)

# click on add
drive.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(2)


# click on delet
drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-colorSecondary MuiSvgIcon-fontSizeMedium css-1m9optw'])[5]").click()
time.sleep(2)


# click on publication
drive.find_element(By.XPATH,"(//div[@class='css-vfjav4'])[9]").click()
time.sleep(2)

# click on add
drive.find_element(By.XPATH,"//body[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/p[1]/div[9]/div[1]/div[1]/div[1]/div[1]/div[2]").click()
time.sleep(2)

# click on name
drive.find_element(By.XPATH,"(//input[@id='input-with-sx'])[1]").send_keys("publaction institute")
time.sleep(2)

#click on address name
address =drive.find_element(By.XPATH,"//input[@id='standard-basic']")
address.send_keys(Keys.CONTROL+'a')
address.send_keys("09/05/2002")
time.sleep(2)



# click on link
drive.find_element(By.XPATH,"(//input[@id='input-with-sx'])[2]").send_keys("https://www.lipsum.com/")
time.sleep(2)

# click on description
drive.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div/div[2]/div/div/div/div/form/div[4]/div/div[2]/div/textarea[1]").send_keys("There are many variations of passages of Lorem Ipsum available,")
time.sleep(2)

# click on add
drive.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(2)


# click on delet
drive.find_element(By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-colorSecondary MuiSvgIcon-fontSizeMedium css-1m9optw'])[8]").click()
time.sleep(2)


