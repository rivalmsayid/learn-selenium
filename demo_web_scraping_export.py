from selenium import webdriver
from selenium.webdriver.common.by import By
from fpdf import FPDF  # Pustaka untuk membuat PDF
import time

# Inisialisasi WebDriver
driver = webdriver.Chrome()

try:
    # Buka situs target
    driver.get("https://thinkjubilee.com/blog/")

    # Tunggu beberapa detik untuk memastikan halaman selesai dimuat
    time.sleep(3)

    # Ambil semua elemen judul artikel
    articles = driver.find_elements(By.CSS_SELECTOR, ".entry-title a")

    # Buat daftar untuk menyimpan data
    data = []

    # Loop untuk mendapatkan teks dari setiap elemen
    for article in articles:
        title = article.text
        link = article.get_attribute("href")
        data.append((title, link))

    # Cetak data untuk verifikasi
    for title, link in data:
        print(f"{title}: {link}")

    # Ekspor data ke PDF
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Scraped Data", ln=True, align='C')
    pdf.ln(10)  # Tambahkan jarak

    for i, (title, link) in enumerate(data, start=1):
        pdf.multi_cell(0, 10, txt=f"{i}. {title}\n{link}", border=0)

    # Simpan PDF ke file
    pdf.output("scraped_data.pdf")
    print("Data berhasil diekspor ke 'scraped_data.pdf'.")

finally:
    # Tutup browser
    driver.quit()

