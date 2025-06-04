import streamlit as st

# Set page config for title, icon, and layout
st.set_page_config(page_title="🌡️ Konversi Suhu Streamlit", page_icon="🌡️", layout="centered")

# Import Google Fonts - via custom CSS using @import (Streamlit allows embedded CSS)
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap');

    /* Animated gradient background */
    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    .stApp {
        font-family: 'Poppins', sans-serif;
        min-height: 100vh;
        background: linear-gradient(-45deg, #667eea, #764ba2, #6a11cb, #2575fc);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        color: #f0f0f0;
        padding: 3rem 1rem;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    /* Main container with glassmorphism */
    .container {
        background: rgba(255, 255, 255, 0.12);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 20px;
        max-width: 480px;
        width: 100%;
        padding: 2.5rem 3rem;
        text-align: center;
    }

    /* Title style */
    .title {
        font-weight: 800;
        font-size: 3.2rem;
        margin-bottom: 0.3rem;
        user-select: none;
    }

    /* Icon style */
    .title-icon {
        font-size: 3.5rem;
        margin-bottom: 1.2rem;
        user-select: none;
        display: inline-block;
        animation: bounce 2s infinite;
    }
    @keyframes bounce {
        0%, 100% {transform: translateY(0);}
        50% {transform: translateY(-10px);}
    }

    /* Subtitle style */
    .subtitle {
        font-weight: 500;
        font-size: 1.2rem;
        margin-bottom: 2.8rem;
        color: #e0e0e0cc;
        user-select: none;
        line-height: 1.5;
    }

    /* Input column tweaks */
    .stNumberInput {
        padding-bottom: 0 !important;
    }

    /* Button customization with transition and shadow */
    div.stButton > button:first-child {
        background-color: #764ba2;
        color: white;
        font-weight: 700;
        font-size: 1.1rem;
        padding: 0.65rem 1.5rem;
        border-radius: 12px;
        border: none;
        box-shadow: 0 6px 15px rgba(118, 75, 162, 0.5);
        cursor: pointer;
        transition: all 0.3s ease;
        user-select: none;
        width: 100%;
    }
    div.stButton > button:first-child:hover {
        background-color: #8a5fc3;
        box-shadow: 0 8px 22px rgba(138, 95, 195, 0.8);
        transform: translateY(-2px);
    }
    div.stButton > button:first-child:focus {
        outline: none;
        box-shadow: 0 0 0 3px #cba3ff66;
    }

    /* Output metric text with emoji and color variants */
    .output-cold {
        color: #59c3c3;
        font-weight: 700;
        font-size: 1.8rem;
        user-select: none;
        text-shadow: 1px 1px 6px rgba(0,0,0,0.35);
        margin-top: 2rem;
    }
    .output-normal {
        color: #f9d71c;
        font-weight: 700;
        font-size: 1.8rem;
        user-select: none;
        text-shadow: 1px 1px 6px rgba(0,0,0,0.35);
        margin-top: 2rem;
    }
    .output-hot {
        color: #ee6c4d;
        font-weight: 700;
        font-size: 1.8rem;
        user-select: none;
        text-shadow: 1px 1px 6px rgba(0,0,0,0.35);
        margin-top: 2rem;
    }

    /* Footer style */
    .footer {
        margin-top: 3rem;
        font-size: 0.9rem;
        color: #d1c4e9bb;
        user-select: none;
    }

    /* Responsive tweaks */
    @media (max-width: 520px) {
        .container {
            padding: 2rem 1.5rem;
        }
        .title {
            font-size: 2.4rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Main container div
st.markdown('<div class="container">', unsafe_allow_html=True)

# Title with bouncing icon
st.markdown('<div class="title-icon">🌡️</div>', unsafe_allow_html=True)
st.markdown('<div class="title">Konversi Suhu Streamlit</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Masukkan suhu dalam Celcius dan klik tombol Konversi untuk melihat hasilnya dalam Fahrenheit dengan indikator suhu.</div>', unsafe_allow_html=True)

# Create two columns for input and button with balanced width
col1, col2 = st.columns([3, 1])

with col1:
    celcius = st.number_input("Suhu (°C)", value=25.0, step=0.1, format="%.2f", key="temp_input")

with col2:
    convert = st.button("Konversi")

# Function to determine output style based on Fahrenheit value
def get_output_style_and_emoji(f):
    if f < 50:
        return "output-cold", "❄️"
    elif f < 86:
        return "output-normal", "🌤️"
    else:
        return "output-hot", "🔥"

if convert:
    fahrenheit = (celcius * 9/5) + 32
    style_class, emoji = get_output_style_and_emoji(fahrenheit)
    st.markdown(
        f'<div class="{style_class}">{emoji} Hasil: {fahrenheit:.2f} °F</div>',
        unsafe_allow_html=True
    )
else:
    st.markdown('<div class="output-normal">Tekan tombol Konversi untuk menampilkan hasil</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown(
    '<div class="footer">© 2024 Streamlit Aplikasi Konversi Suhu - dibuat dengan ❤️</div>',
    unsafe_allow_html=True
)

