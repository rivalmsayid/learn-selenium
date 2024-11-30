from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://demoqa.com/alerts")
driver.maximize_window()
driver.implicitly_wait(10) 

#Alert 1
driver.find_element(By.ID,"alertButton").click()
time.sleep(10)

alert = Alert(driver)
alert.accept()

#Alert 2
driver.execute_script("window.scrollTo(0, 500);")  # Scroll ke 500 piksel secara vertikal
driver.find_element(By.XPATH,"//*[@id='timerAlertButton']").click()
time.sleep(10)

alert = Alert(driver)
alert.accept()

#Alert 3
driver.find_element(By.ID,"confirmButton").click()
time.sleep(10)

alert = Alert(driver)
alert.dismiss()

#Alert 4
promt = driver.find_element(By.ID,"promtButton").click()
time.sleep(5)

alert = Alert(driver)

alert.send_keys("Rival Muhammad")
alert.accept()
time.sleep(5)


driver.quit()