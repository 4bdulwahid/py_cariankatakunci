import sys
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Semak argumen untuk keyword
if len(sys.argv) < 2:
    print("Penggunaan: python check.py <keyword1> <keyword2> ... <keywordN>")
    sys.exit(1)

# Baca kata kunci dari argumen
keywords = sys.argv[1:]
query_keywords = " OR ".join(keywords)  # Gabungkan dengan "OR"

# Fail input domain
input_file = "domains.txt"  # Tukar ke 'domains.csv' jika fail berbentuk CSV

# Baca senarai domain dari fail
domains = []
try:
    if input_file.endswith(".csv"):
        with open(input_file, "r") as file:
            reader = csv.reader(file)
            domains = [row[0] for row in reader]
    elif input_file.endswith(".txt"):
        with open(input_file, "r") as file:
            domains = [line.strip() for line in file]
except FileNotFoundError:
    print(f"Fail '{input_file}' tidak ditemui.")
    sys.exit(1)

# Setup Selenium
driver = webdriver.Chrome()  # Install ChromeDriver jika perlu
results = {}

# Fail log untuk simpan hasil
current_date = datetime.datetime.now().strftime("%Y-%m-%d")  # Format YYYY-MM-DD
log_file = f"search_results_{current_date}.log"

# # Bersihkan atau buat fail log baru
# with open(log_file, "w") as file:
    # file.write("Search Results Log\n")
    # file.write("=" * 50 + "\n\n")

for domain in domains:
    query = f"site:{domain} ({query_keywords})"
    url = f"https://www.google.com/search?q={query}"
    driver.get(url)
    time.sleep(random.uniform(5, 10))  # Tunggu Google load

    # Cari elemen hasil carian
    try:
        # Cari elemen dengan XPath
        links = driver.find_elements(By.XPATH, "//a[@jsname='UWckNb']")
        domain_results = [link.get_attribute("href") for link in links if link.get_attribute("href")]

        # Simpan hasil ke dictionary
        results[domain] = domain_results

        # Debug di terminal
        print(f"Domain: {domain}, Links found: {len(domain_results)}")
        for link in domain_results:
            print(f" - {link}")

        # Tulis hasil ke fail log
        with open(log_file, "a") as file:
            file.write(f"Domain: {domain}\n")
            if domain_results:
                for link in domain_results:
                    file.write(f" - {link}\n")
            else:
                file.write(" - No results found\n")
            file.write("\n")

    except Exception as e:
        print(f"Error processing {domain}: {e}")

# Tutup browser
driver.quit()

# Cetak mesej siap
print(f"Hasil carian telah disimpan dalam fail '{log_file}'.")
