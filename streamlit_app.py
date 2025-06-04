import streamlit as st

st.title("Aplikasi Pertama Fatma ni bos")
st.header("Selamat datang di Web fatma")
st.write("Ini adalah web app pertama fatma menggunakan Python dan Streamlit!")

import streamlit as st

# Judul Aplikasi
st.title("Konversi Suhu")
st.write("Aplikasi ini mengubah suhu dari Celsius ke Fahrenheit dan sebaliknya.")

# Pilihan arah konversi
konversi = st.selectbox(
    "Pilih konversi:",
    ["Celsius ke Fahrenheit", "Fahrenheit ke Celsius"]
)

# Input suhu
suhu = st.number_input("Masukkan suhu:")

# Fungsi konversi
def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

# Tombol konversi
if st.button("Konversi"):
    if konversi == "Celsius ke Fahrenheit":
        hasil = c_to_f(suhu)
        st.success(f"{suhu}°C = {hasil:.2f}°F")
    else:
        hasil = f_to_c(suhu)
        st.success(f"{suhu}°F = {hasil:.2f}°C")
