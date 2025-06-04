import streamlit as st

# Pengaturan halaman
st.set_page_config(page_title="Prediksi Nilai Akhir", page_icon="🎓", layout="centered")

# Judul
st.markdown("""
    <h2 style='text-align: center; color: #1E88E5;'>🎓 Aplikasi Prediksi Nilai Akhir</h2>
    <p style='text-align: center; color: grey;'>Masukkan nilai Tugas, UTS, dan UAS untuk melihat hasil akhir dan predikat Anda.</p>
    <hr style='border-top: 3px solid #1E88E5;'>
""", unsafe_allow_html=True)

# Input nilai
tugas = st.number_input("Masukkan Nilai Tugas (0-100)", min_value=0, max_value=100, value=80)
uts = st.number_input("Masukkan Nilai UTS (0-100)", min_value=0, max_value=100, value=75)
uas = st.number_input("Masukkan Nilai UAS (0-100)", min_value=0, max_value=100, value=85)

# Bobot (bisa diubah jika perlu)
bobot_tugas = 0.3
bobot_uts = 0.3
bobot_uas = 0.4

# Tombol prediksi
if st.button("🔍 Hitung Nilai Akhir"):
    total = (tugas * bobot_tugas) + (uts * bobot_uts) + (uas * bobot_uas)

    # Predikat
    if total >= 85:
        grade = "A"
        warna = "#4CAF50"
    elif total >= 75:
        grade = "B"
        warna = "#2196F3"
    elif total >= 65:
        grade = "C"
        warna = "#FFC107"
    elif total >= 50:
        grade = "D"
        warna = "#FF5722"
    else:
        grade = "E"
        warna = "#F44336"

    # Hasil
    st.markdown(f"""
        <div style='background-color:{warna}; padding:20px; border-radius:10px; color:white; text-align:center;'>
            <h3>Nilai Akhir: {total:.2f}</h3>
            <h2>Predikat: {grade}</h2>
        </div>
    """, unsafe_allow_html=True)
