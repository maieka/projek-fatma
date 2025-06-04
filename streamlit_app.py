import streamlit as st

st.title("Aplikasi Pertama Fatma ni bos")
st.header("Selamat datang di Web fatma")
st.write("Ini adalah web app pertama fatma menggunakan Python dan Streamlit!")

import streamlit as st

# Fungsi untuk menghitung luas
def hitung_luas(panjang, lebar):
    return panjang * lebar

# Judul Aplikasi
st.title("Kalkulator Luas Persegi Panjang")

# Input pengguna
panjang = st.number_input("Masukkan panjang (m)", min_value=0.0)
lebar = st.number_input("Masukkan lebar (m)", min_value=0.0)

# Tombol untuk memicu perhitungan
if st.button("Hitung Luas"):
    hasil = hitung_luas(panjang, lebar)
    st.success(f"Luasnya adalah {hasil} meter persegi")
