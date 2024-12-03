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
        self.base_url = ("https://saucedemo.com/")
        driver = self.driver
        driver.get(self.base_url)
        #'return super().setUp()

    def test_login_page(self):
        #' Test Case Positif : Berhasil Login dengan kredensial valid
        driver = self.driver
        driver.implicitly_wait(10)
        
        username = driver.find_element(By.ID, "user-name")
        username.send_keys("standard_user")

        password = driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")

        btn_login = driver.find_element(By.ID, "login-button")
        btn_login.click()
        time.sleep(10)
        driver.quit()
