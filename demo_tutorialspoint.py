from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")

firstName = driver.find_element(By.ID,"name")
firstName.send_keys("Rival Muhammad Sayid")

email = driver.find_element(By.ID,"email")
email.send_keys("rivalms@gmail.com")

gender = driver.find_element(By.ID,"gender")
gender.click()

mobile = driver.find_element(By.ID,"mobile")
mobile.send_keys("08772000100")

dob = driver.find_element(By.ID,"dob")
dob.send_keys("31/07/1999")
dob.send_keys(Keys.ENTER)

subjects = driver.find_element(By.ID,"subjects")
subjects.send_keys("Quality Assurance")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

hobbies = driver.find_element(By.XPATH,"(//input[@id='hobbies'])[1]").click()

picture = driver.find_element(By.ID,"picture")
picture.send_keys("D:/Repository/pythonselenium/tokped.png")

address = driver.find_element(By.XPATH,"(//textarea[@id='picture'])[1]")
address.send_keys("Cimahi")

state = driver.find_element(By.XPATH,"//*[@id='state']/option[2]").click()
time.sleep(10)
city = driver.find_element(By.XPATH,"//*[@id='city']/option[2]").click()
time.sleep(10)
login = driver.find_element(By.XPATH,"//input[@value='Login']").click()
time.sleep(10)

driver.quit()