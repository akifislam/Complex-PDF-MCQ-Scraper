import glob
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

USERNAME = 's1910776135@ru.ac.bd'
PASSWORD = 'a1k2i3f4@akif'
driver = webdriver.Firefox(executable_path='/Users/akifislam/SeleniumEngines/geckodriver')

driver.get("https://contacts.google.com/u/1/directory")
driver.find_element(By.ID,'identifierId').send_keys(Keys.RETURN)

# driver.find_element(By.ID,'password').send_keys(PASSWORD)
# print("Trying to Press Enter")
# driver.find_element(By.ID,'password').send_keys(Keys.TAB)
# driver.find_element(By.ID,'password').send_keys(Keys.RETURN)
# time.sleep(2)
# driver.get("http://rurfid.ru.ac.bd/ru_services/public/formfillup/index")
# driver.get("http://rurfid.ru.ac.bd/ru_services/public/formfillup/available_exams");



#     print(f"{counter}. Uploaded: {fileName}")
# driver.close()
# else:
#     print(f"{counter}. Already Uploaded !")
#
# if(cur_path.__contains__(".png")):
#     counter+=1

