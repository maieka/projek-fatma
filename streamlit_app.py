import streamlit as st

# Data cuaca statis
data_cuaca = {
    "Jakarta": {"suhu": 31, "kelembapan": 75, "cuaca": "Cerah Berawan"},
    "Bandung": {"suhu": 24, "kelembapan": 85, "cuaca": "Hujan Ringan"},
    "Surabaya": {"suhu": 34, "kelembapan": 70, "cuaca": "Cerah"},
    "Medan": {"suhu": 30, "kelembapan": 80, "cuaca": "Berawan"},
    "Yogyakarta": {"suhu": 29, "kelembapan": 78, "cuaca": "Berawan Tebal"},
}

st.set_page_config(page_title="Cuaca Tanpa API", page_icon="🌤️", layout="centered")

st.markdown("""
    <h1 style='text-align: center; color: #2196F3;'>🌤️ Info Cuaca (Data Statis)</h1>
    <p style='text-align: center; color: grey;'>Lihat prakiraan cuaca berdasarkan data lokal sederhana</p>
    <hr style='border-top: 3px solid #2196F3;'>
""", unsafe_allow_html=True)

# Pilih kota
kota = st.selectbox("Pilih Kota", list(data_cuaca.keys()))

# Tampilkan hasil
if kota:
    info = data_cuaca[kota]
    st.markdown(f"""
        <div style='background-color: #E3F2FD; padding: 20px; border-radius: 10px;'>
            <h3 style='color: #0D47A1;'>🌍 Cuaca di {kota}</h3>
            <p><b>Suhu:</b> {info['suhu']} °C</p>
            <p><b>Kelembapan:</b> {info['kelembapan']}%</p>
            <p><b>Kondisi:</b> {info['cuaca']}</p>
        </div>
    """, unsafe_allow_html=True)
