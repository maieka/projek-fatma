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


