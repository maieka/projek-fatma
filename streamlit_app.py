import streamlit as st

# Page configuration
st.set_page_config(page_title="Konversi Suhu Streamlit", page_icon="🌡️", layout="centered")

# Custom CSS for styling and background gradient
st.markdown(
    """
    <style>
    /* Background gradient */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: #f0f0f0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        min-height: 100vh;
        padding-top: 3rem;
        padding-bottom: 3rem;
    }

    /* Container styling */
    .container {
        background: rgba(255, 255, 255, 0.1);
        max-width: 480px;
        margin: auto;
        padding: 2rem 2.5rem;
        border-radius: 15px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.2);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
    }

    /* Title styling */
    .title {
        font-size: 3rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0.1rem;
        text-shadow: 2px 2px 6px rgba(0,0,0,0.3);
        user-select: none;
    }

    /* Subtitle styling */
    .subtitle {
        font-weight: 500;
        text-align: center;
        margin-bottom: 2.5rem;
        font-size: 1.2rem;
        user-select: none;
        color: #e0e0e0cc;
    }

    /* Input and button columns */
    .stNumberInput {
        padding-bottom: 0 !important;
    }

    /* Button style override */
    div.stButton > button:first-child {
        background-color: #764ba2;
        color: white;
        padding: 0.5rem 1.4rem;
        font-size: 1.1rem;
        font-weight: 600;
        border-radius: 10px;
        border: none;
        box-shadow: 0 4px 8px rgba(118,75,162,0.35);
        transition: background-color 0.3s ease, box-shadow 0.3s ease;
        cursor: pointer;
        user-select: none;
    }
    div.stButton > button:first-child:hover {
        background-color: #8673b8;
        box-shadow: 0 6px 12px rgba(134,115,184,0.7);
    }

    /* Output metric styling */
    .stMetric {
        margin-top: 2rem;
        font-size: 1.7rem;
        font-weight: 700;
        text-align: center;
        user-select: none;
        color: #fff;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.4);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Main container
st.markdown('<div class="container">', unsafe_allow_html=True)

# Title and subtitle
st.markdown('<div class="title">🌡️ Konversi Suhu Streamlit</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Masukkan suhu dalam Celcius dan klik Konversi untuk melihat hasil dalam Fahrenheit.</div>', unsafe_allow_html=True)

# Input and button columns for balanced layout
col1, col2 = st.columns([3,1])

with col1:
    celcius = st.number_input("Suhu dalam Celcius", value=25.0, step=0.1, format="%.2f", key="temp_input")

with col2:
    convert = st.button("Konversi")

if convert:
    fahrenheit = (celcius * 9/5) + 32
    st.markdown(f'<div class="stMetric">🔥 Hasil: {fahrenheit:.2f} °F</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="stMetric">Tekan tombol Konversi untuk menampilkan hasil</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

