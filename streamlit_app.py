
import streamlit as st

st.set_page_config(page_title="Aplikasi Kasir Mini", page_icon="🛒")

st.title("🛒 Aplikasi Kasir Mini")
st.markdown("Masukkan data barang yang dibeli pelanggan.")

# Inisialisasi session state
if "data_belanja" not in st.session_state:
    st.session_state["data_belanja"] = []

# Form input barang
with st.form("form_barang"):
    nama = st.text_input("Nama Barang")
    jumlah = st.number_input("Jumlah", min_value=1, value=1)
    harga = st.number_input("Harga Satuan (Rp)", min_value=0.0, value=0.0, step=100.0)
    tambah = st.form_submit_button("Tambah ke Daftar")

    if tambah and nama:
        total = jumlah * harga
        st.session_state["data_belanja"].append({
            "nama": nama,
            "jumlah": jumlah,
            "harga": harga,
            "total": total
        })
        st.success(f"{nama} berhasil ditambahkan!")

st.markdown("---")
st.subheader("🧾 Daftar Belanja")

if st.session_state["data_belanja"]:
    total_bayar = 0
    for item in st.session_state["data_belanja"]:
        st.write(f"- **{item['nama']}** ({item['jumlah']} x Rp{item['harga']:,.0f}) = Rp{item['total']:,.0f}")
        total_bayar += item["total"]
    
    st.markdown("---")
    st.success(f"💵 Total Bayar: **Rp{total_bayar:,.0f}**")
else:
    st.info("Belum ada barang yang dimasukkan.")

st.caption("📦 Dibuat dengan Streamlit oleh Kelompok X")
