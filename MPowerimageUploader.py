import glob
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

path = "/Users/akifislam/Downloads/auto images"
counter = 1
for cur_path in glob.glob(path+"/**", recursive = True):
    if(cur_path.__contains__(".png") and counter>=379):
        fileName = (cur_path.split("/")[-1])[:-4] # to avoid double .png extension
        driver = webdriver.Firefox(executable_path='/Users/akifislam/SeleniumEngines/geckodriver')

        driver.get("http://moodle.mpower-social.com/converter/pix/upload.php")
        driver.maximize_window()
        driver.find_element(By.ID,'imgfile').send_keys(cur_path)
        driver.find_element(By.ID,'imgname').send_keys(fileName)
        driver.find_element(By.NAME,'submit').send_keys(Keys.RETURN)
        time.sleep(1)
        print(f"{counter}. Uploaded: {fileName}")
        driver.close()

    else:
        print(f"{counter}. Already Uploaded !")

    if(cur_path.__contains__(".png")):
        counter+=1
