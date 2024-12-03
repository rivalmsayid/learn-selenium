from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time

class FunctionalTestSaucelabs(unittest.TestCase):
    def setUp(self):
        # Inisialisasi WebDriver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.base_url = ("https://opensource-demo.orangehrmlive.com/web/index.php")
        driver = self.driver
        driver.get(self.base_url)
        #'return super().setUp()

    def test_login_page(self):
        #' Test Case Positif : Berhasil Login dengan kredensial valid
        driver = self.driver
        driver.implicitly_wait(10)
        
        username = driver.find_element(By.NAME, "username")
        username.send_keys("Admin")

        password = driver.find_element(By.NAME, "password")
        password.send_keys("admin123")

        btn_submit = driver.find_element(By.XPATH, "//button[@type='submit']")
        btn_submit.click()
        time.sleep(10)
        driver.quit()