from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

driver = webdriver.Chrome()

try:
    driver.get("https://www.instagram.com/")
    driver.maximize_window()

    # Tunggu halaman termuat
    time.sleep(5)

    # Temukan dan isi username
    username_field = driver.find_element(By.NAME, "username")
    username_field.send_keys("stefanivero777")  # Ganti dengan username Instagram Anda

    # Temukan dan isi password
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("Algoritma!2")  # Ganti dengan password Instagram Anda

    # Klik tombol login
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    # Tunggu halaman utama termuat
    time.sleep(10)
        
    # Verifikasi apakah login berhasil
    if "instagram.com" in driver.current_url:
        print("Login berhasil!")
    else:
        print("Login gagal. Periksa username dan password Anda.")
    
finally:
    # Tutup browser
    driver.quit()
    