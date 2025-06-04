import streamlit as st

# Styling custom menggunakan markdown dan HTML
st.markdown(
    """
    <style>
    .title {
        color: #4B8BBE;
        font-family: 'Arial Black', Gadget, sans-serif;
        font-size: 48px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
    }
    .subtitle {
        color: #306998;
        font-family: 'Arial', sans-serif;
        font-size: 20px;
        text-align: center;
        margin-bottom: 30px;
    }
    .output {
        background-color: #F0F8FF;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        font-size: 24px;
        color: #333333;
        margin-top: 20px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
    }
    .container {
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
        padding: 30px;
        background: #ffffff;
        box-shadow: 0 0 20px rgba(70, 130, 180, 0.2);
        border-radius: 15px;
    }
    </style>
    """, unsafe_allow_html=True
)

# Container utama aplikasi
with st.container():
    st.markdown('<div class="container">', unsafe_allow_html=True)

    st.markdown('<div class="title">Aplikasi Konversi Suhu</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Masukkan suhu dalam Celcius, lalu klik tombol untuk mengonversi ke Fahrenheit.</div>', unsafe_allow_html=True)

    # Menggunakan kolom untuk input dan tombol
    col1, col2 = st.columns([3,1])
    with col1:
        celcius = st.number_input("Suhu dalam Celcius", value=25.0, step=0.1)
    with col2:
        convert = st.button("Konversi")

    if convert:
        fahrenheit = (celcius * 9/5) + 32
        st.markdown(f'<div class="output">Suhu dalam Fahrenheit: <b>{fahrenheit:.2f}</b> °F</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="output">Tekan tombol konversi untuk melihat hasil.</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

