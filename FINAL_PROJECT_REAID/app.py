import streamlit as st
import requests
import uuid
import json
import os

# Fungsi validasi API Key
def validate_api_key(api_key):
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": "mistralai/mistral-7b-instruct",
                "messages": [{"role": "user", "content": "Halo"}],
            },
            timeout=10
        )
        return response.status_code == 200
    except:
        return False

# Fungsi rekomendasi
def get_rekomendasi(api_key, prompt):
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": "mistralai/mistral-7b-instruct",
                "messages": [{
                    "role": "user",
                    "content": (
                        f"{prompt}\n"
                        "Berikan hasil dalam format JSON murni (tanpa penjelasan) sebagai list berisi 10 objek "
                        "dengan kunci: 'judul', 'genre', dan 'rating_rata_rata'. Jangan beri teks lain selain JSON."
                    )
                }],
            },
            timeout=30
        )
        hasil = response.json()
        return hasil['choices'][0]['message']['content']
    except Exception as e:
        st.error(f"Gagal merekomendasikan novel: {e}")
        return None

# Parse JSON
def parse_hasil(teks):
    try:
        data = json.loads(teks)
        if isinstance(data, list):
            return data
        else:
            raise ValueError("Format JSON bukan list")
    except Exception:
        st.error("❌ Format JSON yang diterima tidak valid.")
        return []

# Tampilkan horizontal card
def tampilkan_hasil(data):
    st.markdown("<br>", unsafe_allow_html=True)
    rows = [data[i:i+5] for i in range(0, len(data), 5)]
    for row_data in rows:
        st.markdown("<div class='container-grid'>", unsafe_allow_html=True)
        for row in row_data:
            st.markdown(f"""
                <div class='novel-card'>
                    <h4>{row.get('judul', '')}</h4>
                    <p><i>{row.get('genre', '')}</i></p>
                    <p>Rating: {row.get('rating_rata_rata', '')}</p>
                </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# Load CSS
if "style.css" in os.listdir():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
else:
    st.markdown("""
    <style>
    .novel-card {
        background-color: #5d4037;
        color: white;
        padding: 16px;
        border-radius: 12px;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
        width: 100%;
        height: 100%;
        text-align: center;
    }
    .container-row {
        display: flex;
        justify-content: space-between;
        flex-wrap: nowrap;
        gap: 12px;
        margin-bottom: 16px;
    }
    .novel-card h4, .novel-card p {
        margin: 0;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Inisialisasi session state
if "hasil_desc" not in st.session_state:
    st.session_state.hasil_desc = None
if "deskripsi" not in st.session_state:
    st.session_state.deskripsi = ""
if "textarea_key" not in st.session_state:
    st.session_state.textarea_key = str(uuid.uuid4())
if "api_valid" not in st.session_state:
    st.session_state.api_valid = False

# Sidebar
st.sidebar.image("logo.png")
st.sidebar.title("📚 Rekomendasi Novel AI")
st.sidebar.info("Masukkan API Key Anda untuk mendapatkan rekomendasi novel berdasarkan deskripsi yang Anda berikan. "
                  "Pastikan API Key Anda valid agar dapat digunakan.")
st.sidebar.markdown("<br>"*1, unsafe_allow_html=True)
api_key = st.sidebar.text_input("🔐 Masukkan API Key Anda", type="password")

if st.sidebar.button("✅ Validasi"):
    if validate_api_key(api_key):
        st.sidebar.success("API Key valid!")
        st.session_state.api_valid = True
    else:
        st.sidebar.error("API Key tidak valid!")
        st.session_state.api_valid = False

# Halaman utama
st.title("✨ Temukan Novel Berdasarkan Deskripsi")

if st.session_state.api_valid:
    deskripsi_input = st.text_area(
        "Masukkan deskripsi singkat novel yang Anda cari:",
        key=st.session_state.textarea_key
    )
    st.session_state.deskripsi = deskripsi_input

    col1, col2 = st.columns([1, 1])

    with col1:
        if st.button("🔍 Cari Rekomendasi"):
            if st.session_state.deskripsi.strip():
                prompt = f"Berdasarkan deskripsi berikut: '{st.session_state.deskripsi}'"
                hasil = get_rekomendasi(api_key, prompt)
                st.session_state.hasil_desc = parse_hasil(hasil)
            else:
                st.warning("Masukkan deskripsi terlebih dahulu.")

    with col2:
        def reset_form():
            st.session_state.hasil_desc = None
            st.session_state.deskripsi = ""
            st.session_state.textarea_key = str(uuid.uuid4())

        st.button("🔄 Reset", on_click=reset_form)

    if st.session_state.hasil_desc:
        tampilkan_hasil(st.session_state.hasil_desc)
