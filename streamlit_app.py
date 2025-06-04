import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Pengantar Streamlit", page_icon="📘")

# Judul dan Deskripsi
st.title("📘 Pengantar Streamlit")
st.markdown("Selamat datang di pembelajaran *Web Aplikasi Python* menggunakan **Streamlit**.")

st.markdown("---")
st.subheader("👀 Apa itu Streamlit?")
st.markdown("""
Streamlit adalah framework Python yang digunakan untuk membuat **aplikasi web interaktif** secara **mudah dan cepat**.

### Keunggulan:
- Sederhana & cepat dipelajari
- Langsung dari script Python
- Ideal untuk prototipe, dashboard, dan aplikasi data

""")

st.markdown("---")
st.subheader("💡 Contoh Program Pertama:")
st.code("""
import streamlit as st

st.title("Halo Dunia!")
st.write("Ini adalah aplikasi web pertamaku menggunakan Streamlit.")
""", language="python")

st.markdown("Coba jalankan kode ini dengan perintah terminal:")
st.code("streamlit run app.py")

st.markdown("---")
st.success("✅ Selamat! Kamu telah mengenal dasar-dasar Streamlit.")



import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Konversi Suhu", page_icon="🌡️")

# Header
st.markdown("<h1 style='text-align: center; color:#FF4B4B;'>🌡️ Konversi Suhu</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color:grey;'>Celsius ↔ Fahrenheit</h4>", unsafe_allow_html=True)
st.markdown("---")

# Fungsi Konversi
def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

# Kolom Input
col1, col2 = st.columns(2)

with col1:
    suhu = st.number_input("Masukkan suhu", value=0.0)

with col2:
    konversi = st.selectbox("Pilih konversi", ["Celsius ke Fahrenheit", "Fahrenheit ke Celsius"])

# Tombol & Output
if st.button("🔁 Konversi"):
    if konversi == "Celsius ke Fahrenheit":
        hasil = c_to_f(suhu)
        st.success(f"Hasil: {suhu:.2f} °C = {hasil:.2f} °F")
    else:
        hasil = f_to_c(suhu)
        st.success(f"Hasil: {suhu:.2f} °F = {hasil:.2f} °C")

st.markdown("---")
st.caption("👨‍💻 Dibuat oleh Kelompok X – Materi Fungsi dan Web Aplikasi")
