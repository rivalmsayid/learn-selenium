from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.tokopedia.com/")
driver.get_screenshot_as_file("tokped.png")

