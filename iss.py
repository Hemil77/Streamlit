import streamlit as st
import requests
import pandas as pd
from datetime import datetime

# ==========================================
# CONFIG
# ==========================================

st.set_page_config(
    page_title="🚀 Space Mission Dashboard",
    page_icon="🚀",
    layout="wide"
)

NASA_API_KEY = "XoVPNsaL5Fpg5cO4EWrkfxdSV5LESkwgAg4LsLOP"

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

.big-title {
    text-align:center;
    color:#00D4FF;
    font-size:55px;
    font-weight:bold;
}

.subtitle {
    text-align:center;
    color:#B8C1EC;
    font-size:18px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# HEADER
# ==========================================

st.markdown(
    '<p class="big-title">🚀 SPACE MISSION DASHBOARD</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Live ISS Tracking + NASA Space Data</p>',
    unsafe_allow_html=True
)

st.divider()

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("🚀 Mission Control")

st.sidebar.write("🕒 Last Updated")
st.sidebar.write(datetime.now().strftime("%H:%M:%S"))

st.sidebar.info("""
Data Sources

🛰️ ISS API 

🚀 NASA APOD API

""")

# ==========================================
# REFRESH BUTTON
# ==========================================

if st.button("🔄 Refresh Data"):
    st.rerun()

# ==========================================
# ISS TRACKER
# ==========================================

st.header("🛰️ International Space Station")

try:

    iss_url = "https://api.wheretheiss.at/v1/satellites/25544"
    iss = requests.get(iss_url).json()

    latitude = float(iss["latitude"])
    longitude = float(iss["longitude"])
    altitude = float(iss["altitude"])
    velocity = float(iss["velocity"])
    visibility = iss["visibility"]

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("🌍 Latitude", f"{latitude:.2f}°")
    col2.metric("🌎 Longitude", f"{longitude:.2f}°")
    col3.metric("📏 Altitude", f"{altitude:.1f} km")
    col4.metric("🚀 Velocity", f"{velocity:.0f} km/h")

    st.success(
        f"📍 Current Position: {latitude:.2f}°, {longitude:.2f}°"
    )

    # WORKING MAP
    st.subheader("🌍 Current ISS Location")

    map_df = pd.DataFrame({
        "lat": [latitude],
        "lon": [longitude]
    })

    st.map(map_df)

    st.info(f"👁️ Visibility: {visibility}")

except Exception as e:

    st.error("Unable to fetch ISS data.")
    st.write(e)

st.divider()

# ==========================================
# ASTRONAUTS
# ==========================================

st.header("👨‍🚀 Astronauts Currently In Space")

try:

    astro_url = "http://api.open-notify.org/astros.json"
    astro = requests.get(astro_url).json()

    st.success(
        f"Total Astronauts In Space: {astro['number']}"
    )

    df = pd.DataFrame(astro["people"])

    st.dataframe(
        df,
        use_container_width=True
    )

except:
    st.warning("Astronaut API unavailable.")

st.divider()

# ==========================================
# NASA APOD
# ==========================================

st.header("🌌 NASA Astronomy Picture of the Day")

try:

    apod_url = (
        f"https://api.nasa.gov/planetary/apod"
        f"?api_key={NASA_API_KEY}"
    )

    apod = requests.get(apod_url).json()

    st.image(
        apod["url"],
        use_container_width=True
    )

    st.subheader(apod["title"])

    st.write(apod["explanation"])

except:
    st.warning("Unable to load NASA APOD.")

# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "🚀 Built with Streamlit | ISS API | NASA APOD API"
)




