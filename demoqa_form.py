from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/automation-practice-form")

firstName = driver.find_element(By.ID,"firstName")
firstName.send_keys("Rival")

lastName = driver.find_element(By.ID,"lastName")
lastName.send_keys("Muhammad")

email = driver.find_element(By.ID,"userEmail")
email.send_keys("rival@gmail.com")

gender = driver.find_element(By.XPATH,"//label[contains(text(),'Male')]")
gender.click()

mobileNumber = driver.find_element(By.ID,"userNumber")
mobileNumber.send_keys("08998512223")

datePicker = driver.find_element(By.ID,"dateOfBirthInput")
datePicker.send_keys(Keys.CONTROL + "a")
datePicker.send_keys("31 Jul 1999" + Keys.ENTER)
time.sleep(2)


subject_input = driver.find_element(By.ID, "subjectsInput")
subject_input.click()
subject_input.send_keys("M")
subject_options = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'subjects-auto-complete__option')]"))
)

for option in subject_options:
    if "Maths" in option.text:
        driver.execute_script("arguments[0].click();", option)  # Klik dengan JavaScript

        break

sports_checkbox = driver.find_element(By.XPATH, "//label[normalize-space()='Sports']").click()

upload = driver.find_element(By.ID,"uploadPicture").send_keys("D:/Repository/pythonselenium/tokped.png")

currentAddress = driver.find_element(By.ID,"currentAddress")
currentAddress.send_keys("Silicon Valley")

stateCity = driver.find_element(By.XPATH,"(//div[@class=' css-1hwfws3'])[1]")

state_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "react-select-3-input")))
state_field.send_keys("NCR")
state_field.send_keys(Keys.ENTER)

city_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "react-select-4-input")))
city_field.send_keys("Delhi")
city_field.send_keys(Keys.ENTER)

submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "submit")))
submit_button.click()

dialog = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "modal-title")))
print("Form submitted. Modal Title:", dialog.text)
time.sleep(10)
driver.quit() 