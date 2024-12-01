from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time

class FunctionalTestBankIndonesia(unittest.TestCase):
    def setUp(self):
        # Inisialisasi WebDriver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.base_url = "https://www.bi.go.id/"  # URL situs Bank Indonesia

    def test_homepage_load(self):
        # Memastikan halaman utama situs dapat diakses
        driver = self.driver
        driver.get(self.base_url)

        # Verifikasi judul halaman
        self.assertIn("Bank Indonesia", driver.title, "Judul halaman tidak sesuai")

        # Verifikasi keberadaan logo
        logo = driver.find_element(By.ID, "ctl00_onetidHeadbnnr2")  # Ganti dengan class logo sebenarnya
        self.assertTrue(logo.is_displayed(), "Logo Bank Indonesia tidak ditemukan")

        # Verifikasi menu navigasi utama
        nav_menu = driver.find_element(By.ID, "ctl00_g_9675ef44_8939_42e2_aefd_df1b1e975487")  # Ganti dengan ID atau class navigasi sebenarnya
        self.assertTrue(nav_menu.is_displayed(), "Menu navigasi utama tidak tampil")

    def test_search_function(self):
        # Memastikan fitur pencarian bekerja dengan benar
        driver = self.driver
        driver.get(self.base_url)

        # Interaksi dengan kotak pencarian
        search_box = driver.find_element(By.ID,"ctl00_PlaceHolderSearchArea_SmallSearchInputBox1_csr_sbox")
        search_box.send_keys("kebijakan moneter")
        search_box.send_keys(Keys.RETURN)
        time.sleep(10)

        # Verifikasi judul halaman
        self.assertIn("Bank Indonesia", driver.title, "Judul halaman tidak sesuai")
        time.sleep(5)
        
    def tearDown(self):
        # Tutup browser setelah pengujian selesai
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()