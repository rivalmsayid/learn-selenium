#Step 1 Mengimport modul
from selenium import webdriver  #untuk mengimport modul Webdriver dari paket selenium
from selenium.webdriver.common.by import By  #untuk menentukan cara pencarian elemen di halaman web, seperti ID, XPath, NAME, dan lainnya. Contoh: By.ID("username")
from selenium.webdriver.common.keys import Keys  #untuk mengirimkan input berupa tombol keyboard, seperti Keys.ENTER atau Keys.TAB.
from selenium.webdriver.support.ui import WebDriverWait  #untuk menunggu hingga kondisi tertentu tercapai pada elemen, seperti menunggu elemen muncul atau bisa diklik.
from selenium.webdriver.support import expected_conditions as EC  #untuk mendefinisikan kondisi yang harus dipenuhi sebelum berinteraksi dengan elemen, misalnya menunggu elemen menjadi terlihat (visibility_of_element_located).
import time  #untuk menambahkan jeda waktu dalam eksekusi program, biasanya menggunakan time.sleep() untuk menunggu beberapa detik.

#Step 2 Membuka browser. contoh: Google Chrome.
driver = webdriver.Chrome()

#Step 3 Memaksimalkan/maximize ukuran jendela browser
driver.maximize_window()

#Step 4 Menavigasikan ke URL yang diberikan.
driver.get("https://www.google.com/")

#Step 5 Menargetkan elemen yang akan digunakan sebagai locater/penanda di kolom pencarian google. 
# Mencari elemen locater : Klik kanan pada halaman browser> Inspect> arahkan kursor pada search bar google.
# Klik CTRL + F (find) masukkan pada kolom //textarea[@name="q"] sebagai penanda.
searchBar = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//textarea[@name="q"]'))
)
searchBar.send_keys("Selenium") #untuk memberi perintah input di kolom pencarian

#Step 6 Menargetkan elemen yang akan digunakan sebagai locater/penanda pada tombol penelusuran google.
# Klik kananan> Inspect> arahkan kursor pada tombol penelusuran google.
# Klik CTRL + F (find) masukkan pada kolom //input[@type='submit'] sebagai penanda.
buttonPenelusuran = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, 'btnK'))
)
#Step 7 Mengklik tombol penelusuran
buttonPenelusuran.click() #untuk memberi perintah klik tombol

time.sleep(3) # Memberikan waktu tunggu sebelum browser tertutup

 
#Jalankan program di terminal dengan perintah pytest nama_file.py. contoh : pytest demo_google.py (enter)