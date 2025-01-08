# Pencari Kata Kunci dalam Domain

## Pengenalan
Skrip ini membolehkan anda mencari pautan yang berkaitan dengan kata kunci tertentu dalam senarai domain yang diberikan. Contohnya untuk semakan SEO Poisoning. Hasil carian akan disimpan dalam fail log dengan tarikh semasa sebagai sebahagian daripada nama fail.

## Fungsi Skrip
Skrip ini berfungsi untuk:
- Membaca senarai domain dari fail `domains.txt` atau `domains.csv`.
- Membuat carian Google untuk kata kunci yang diberikan dalam domain tersebut.
- Menyimpan hasil carian dalam fail log yang dinamakan berdasarkan tarikh semasa (contoh: `search_results_2025-01-08.log`).

## Keperluan
1. **Selenium WebDriver** - Pastikan anda telah memasang Selenium dan ChromeDriver.
2. **Fail Input Domain** - Anda perlu menyediakan fail `domains.txt` atau `domains.csv` yang mengandungi senarai domain untuk dicari. Contoh:
   - `domains.txt` (untuk fail teks biasa):
     ```
     example.com
     anotherdomain.com
     ```
   - `domains.csv` (untuk fail CSV):
     ```csv
     example.com
     anotherdomain.com
     ```

## Cara Menggunakan Skrip
1. Pastikan semua keperluan telah dipenuhi.
2. Simpan senarai domain dalam fail `domains.txt` atau `domains.csv`.
3. Jalankan skrip dengan perintah berikut, menggantikan `<keyword1>`, `<keyword2>`, dll. dengan kata kunci yang ingin dicari:
   ```bash
   python check.py <keyword1> <keyword2> ... <keywordN>
