from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://thinkjubilee.com/cara-memperbaiki-cahaya-foto-digital-dengan-mudah/")

teks = driver.find_element(By.ID,"post-9216").text

print(teks)