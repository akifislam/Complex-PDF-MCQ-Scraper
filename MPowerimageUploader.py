from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Firefox(executable_path='/Users/akifislam/SeleniumEngines/geckodriver')
driver.get("http://moodle.mpower-social.com/converter/pix/upload.php")
driver.maximize_window()
driver.find_element(By.ID,'imgfile').send_keys("/Users/akifislam/PycharmProjects/PlumberTest/TestBioImage.png")
driver.find_element(By.ID,'imgname').send_keys("TestBioImage")
driver.find_element(By.NAME,'submit').send_keys(Keys.RETURN)
# driver.close()