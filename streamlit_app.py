import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="Aplikasi Streamlit Interaktif",
    page_icon="🚀",
    layout="centered"
)

# ====================
# Header & Deskripsi
# ====================
st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>🚀 Web Aplikasi Interaktif</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: grey;'>Contoh aplikasi sederhana dengan tampilan menarik menggunakan Streamlit</h4>", unsafe_allow_html=True)
st.markdown("---")

# ====================
# Form Input (Dua Kolom)
# ====================
st.subheader("🔢 Input Data")

col1, col2 = st.columns(2)

with col1:
    angka1 = st.number_input("Masukkan Angka Pertama", step=1)

with col2:
    angka2 = st.number_input("Masukkan Angka Kedua", step=1)

# ====================
# Pilihan Operasi
# ====================
operasi = st.selectbox("Pilih Operasi", ["Tambah", "Kurang", "Kali", "Bagi"])

# ====================
# Tombol dan Hasil
# ====================
if st.button("💡 Hitung"):
    if operasi == "Tambah":
        hasil = angka1 + angka2
        st.success(f"Hasil penjumlahan: {hasil}")
    elif operasi == "Kurang":
        hasil = angka1 - angka2
        st.success(f"Hasil pengurangan: {hasil}")
    elif operasi == "Kali":
        hasil = angka1 * angka2
        st.success(f"Hasil perkalian: {hasil}")
    elif operasi == "Bagi":
        if angka2 != 0:
            hasil = angka1 / angka2
            st.success(f"Hasil pembagian: {hasil:.2f}")
        else:
            st.error("❌ Tidak bisa membagi dengan nol.")

st.markdown("---")
st.caption("📘 Dibuat oleh Kelompok X | Proyek Streamlit 2025")
