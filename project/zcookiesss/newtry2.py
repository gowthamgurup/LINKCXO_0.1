# import pickle
#
# import selenium
# # import undetected_chromedriver as uc
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
#
# if __name__ == '__main__':
#
#     driver = selenium.webdriver.Chrome(r"C:\Users\Gowtham p\Downloads\chromedriver_win32\chromedriver.exe")
#     driver.get("http://linkcxo-frontend-testing.s3-website.ap-south-1.amazonaws.com")
#
#     # http://linkcxo-frontend-testing.s3-website.ap-south-1.amazonaws.com/login
#
#     cookies = pickle.load(open("cookies.pkl", "rb"))
#
#     for cookie in cookies:
#         cookie['domain'] = ".linkcxo-frontend-testing.s3-website.ap-south-1.amazonaws.com"
#
#         try:
#             driver.add_cookie(cookie)
#         except Exception as e:
#             print(e)
#
#     driver.get('http://linkcxo-frontend-testing.s3-website.ap-south-1.amazonaws.com/feed')
#
#     time.sleep(120)
#





