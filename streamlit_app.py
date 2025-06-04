import streamlit as st
import requests

st.set_page_config(page_title="Aplikasi Cuaca", page_icon="⛅", layout="centered")

st.markdown("""
    <h1 style='text-align: center; color: #4A90E2;'>⛅ Aplikasi Cek Cuaca</h1>
    <h4 style='text-align: center; color: grey;'>Gunakan API OpenWeather untuk melihat suhu, kelembapan, dan kondisi cuaca.</h4>
    <hr style='border-top: 3px solid #4A90E2;'>
""", unsafe_allow_html=True)

# Ganti ini dengan API key dari OpenWeatherMap.org
api_key = "MASUKKAN_API_KEY_ANDA_DI_SINI"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Input kota dari user
city_name = st.text_input("Masukkan nama kota (misal: Jakarta):")

if st.button("🔍 Cek Cuaca"):
    if not api_key or api_key == "MASUKKAN_API_KEY_ANDA_DI_SINI":
        st.warning("⚠️ Silakan masukkan API key Anda di dalam kode terlebih dahulu.")
    elif city_name:
        complete_url = f"{base_url}appid={api_key}&q={city_name}&units=metric"
        response = requests.get(complete_url)
        data = response.json()

        if data["cod"] != "404":
            main = data["main"]
            weather = data["weather"][0]
            temp = main["temp"]
            humidity = main["humidity"]
            desc = weather["description"].capitalize()

            st.markdown(f"""
                <div style='background-color: #E3F2FD; padding: 20px; border-radius: 10px;'>
                    <h3 style='color: #0D47A1;'>🌍 Cuaca di {city_name.title()}</h3>
                    <p><b>Suhu:</b> {temp} °C</p>
                    <p><b>Kelembapan:</b> {humidity}%</p>
                    <p><b>Kondisi:</b> {desc}</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.error("Kota tidak ditemukan. Coba lagi.")
