import streamlit as st

st.set_page_config(page_title="Aplikasi Kasir Mini", page_icon="🛒", layout="centered")

# Header aplikasi
st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>🛒 Aplikasi Kasir Mini</h1>
    <h4 style='text-align: center; color: grey;'>Catat & Hitung Total Belanja Pelanggan</h4>
    <hr style='border-top: 3px solid #4CAF50;'>
""", unsafe_allow_html=True)

# Inisialisasi session state
if "data_belanja" not in st.session_state:
    st.session_state["data_belanja"] = []

# Form input barang dengan kolom
st.markdown("### ➕ Tambah Barang")
col1, col2 = st.columns([3, 2])
with col1:
    nama = st.text_input("Nama Barang")
with col2:
    jumlah = st.number_input("Jumlah", min_value=1, value=1, step=1)

harga = st.number_input("Harga Satuan (Rp)", min_value=0.0, value=0.0, step=100.0)
tambah = st.button("🧾 Tambahkan ke Daftar")

if tambah and nama:
    total = jumlah * harga
    st.session_state["data_belanja"].append({
        "nama": nama,
        "jumlah": jumlah,
        "harga": harga,
        "total": total
    })
    st.success(f"✅ {nama} berhasil ditambahkan!")

# Tampilkan daftar belanja
st.markdown("---")
st.markdown("### 📋 Daftar Belanja")

if st.session_state["data_belanja"]:
    total_bayar = 0
    for item in st.session_state["data_belanja"]:
        with st.container():
            st.markdown(f"""
                <div style='border:1px solid #ccc; border-radius:10px; padding:10px; margin-bottom:10px; background-color:#f9f9f9;'>
                    <b>{item['nama']}</b> — {item['jumlah']} x Rp{item['harga']:,.0f}<br>
                    <span style='color: #4CAF50;'>Total: Rp{item['total']:,.0f}</span>
                </div>
            """, unsafe_allow_html=True)
        total_bayar += item["total"]
    
    st.markdown("---")
    st.markdown(f"<h3 style='text-align: center; color: #d32f2f;'>💵 Total Bayar: Rp{total_bayar:,.0f}</h3>", unsafe_allow_html=True)
else:
    st.info("Belum ada barang yang dimasukkan.")

st.markdown("<hr>", unsafe_allow_html=True)
st.caption("📦 Dibuat oleh Kelompok X – Streamlit Kasir App")
