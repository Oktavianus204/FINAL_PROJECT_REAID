# 📚 Aplikasi Rekomendasi Novel AI

## 1. Judul Project
**Novel Recommendation System - Aplikasi Rekomendasi Novel Berbasis Artificial Intelligence**

## 2. Deskripsi Singkat

### 📌 Latar Belakang Masalah
Dalam era digital saat ini, pembaca novel seringkali mengalami kesulitan dalam menemukan buku yang sesuai dengan preferensi dan selera mereka. Dengan ribuan judul novel yang tersedia, proses pencarian manual menjadi tidak efisien dan memakan waktu. Pembaca sering kali hanya memiliki deskripsi samar tentang jenis cerita yang ingin mereka baca, namun kesulitan menemukan rekomendasi yang tepat berdasarkan deskripsi tersebut.

### 🎯 Tujuan
Aplikasi ini dikembangkan dengan tujuan untuk:
- Memudahkan pembaca dalam menemukan novel yang sesuai dengan deskripsi atau preferensi mereka
- Menggunakan teknologi Artificial Intelligence untuk memberikan rekomendasi yang akurat dan relevan
- Menyediakan interface yang user-friendly dan responsif untuk pengalaman pengguna yang optimal
- Mengintegrasikan sistem validasi API Key untuk keamanan dan kontrol akses

## 3. Fitur-Fitur Utama
✨ Fitur Utama
🔐 Sistem Keamanan API
- Validasi API Key OpenRouter: Verifikasi otomatis kevalidan API Key sebelum mengakses layanan AI
- Kontrol Akses: Fitur utama hanya dapat diakses setelah API Key tervalidasi
- Status Real-time: Feedback langsung tentang status validasi API Key

🤖 Rekomendasi Berbasis AI
- Integrasi Mistral-7B-Instruct: Menggunakan model AI canggih via OpenRouter API
- Input Natural Language: Pengguna dapat mendeskripsikan novel yang dicari dalam bahasa natural
- 10 Rekomendasi Terstruktur: Menghasilkan daftar novel dengan judul, genre, dan rating

📊 Pemrosesan Data Otomatis
- Parser JSON Intelligent: Memproses response AI dan mengkonversi menjadi data terstruktur
- Validasi Data: Memastikan format data sesuai sebelum ditampilkan
- Error Handling: Penanganan error komprehensif untuk berbagai skenario

🎨 Interface Modern
- Card Layout Responsif: Tampilan hasil dalam bentuk card yang menarik dan terorganisir
- Design Interaktif: Hover effects dan styling modern untuk pengalaman pengguna optimal
- Reset Functionality: Fitur reset untuk pencarian baru dengan mudah


🛠️ Teknologi yang Digunakan
- Framework: Streamlit
- AI Model: Mistral-7B-Instruct (via OpenRouter API)
- Language: Python
- Styling: Custom CSS
- API Integration: RESTful API

## Instalasi
- Buat virtual environment (direkomendasikan):
```bash
python -m venv venv
source venv/bin/activate # Di macOS/Linux
# venv\Scripts\activate   # Di Windows
  ```

- Buka terminal anda, lalu masukan perintah perintah berikut ini, untuk menginstall library
```bash
pip install streamlit
pip install requests
  ```

## Menjalankan website
1. Dapatkan API KEY anda
- ini adalah website untuk membuat API KEY https://openrouter.ai
- login dan dapatkan API KEY anda
2. Cara masuk jalankan aplikasi
```bash
streamlit run app.py # Asumsikan nama file Anda adalah app.py
```

## Preview APlikasi(Screenshot)
1. Tampilan Awal
    <img width="1366" height="641" alt="1" src="https://github.com/user-attachments/assets/819ae8d7-2b71-41d2-baf5-9593e9370dfa" />

2. Masukan API key di bagian sidebar terlebih dahulu, berikut ini merupaka contoh cara memasukan dan validasi API KEY
   <img width="1366" height="641" alt="2" src="https://github.com/user-attachments/assets/21343946-6785-4148-afff-aed506d01fc0" />

3. Masukan sebuah deskripi di bagian input text area, lalu tekan tombol cari referensi,
   <img width="1366" height="641" alt="3" src="https://github.com/user-attachments/assets/49368359-c237-471c-a62c-506900613bd3" />
   
4. untuk mereset dan melakukan pencarian lain, tekan tombol reset
   <img width="1366" height="641" alt="4" src="https://github.com/user-attachments/assets/3a3637a5-8634-4578-a0e7-b426339298f7" />

## berikut ini merupakan link deploy website/Aplikasi





















