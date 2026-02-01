import streamlit as st
import requests

# ---------------- CONFIG (MUST BE FIRST ST CALL) ----------------
st.set_page_config(
    page_title="Crop Yield Predictor",
    page_icon="🌱",
    layout="centered",
)

API_URL = "http://localhost:8000/yield_predict"

# ---------------- SAFE DARK THEME ----------------
st.markdown("""
<style>
.stApp {
    background-color: #0f1117;
    color: #e6e6e6;
}

div[data-baseweb="input"] input,
div[data-baseweb="select"] > div {
    background-color: #1b1f2a;
    color: #ffffff;
    border-radius: 6px;
}

.stButton > button {
    background-color: #262a36;
    color: white;
    border-radius: 6px;
    border: 1px solid #3a3f50;
}

.stButton > button:hover {
    background-color: #323750;
    border-color: #4a4f65;
}

div[data-testid="metric-container"] {
    background-color: #1b1f2a;
    border-radius: 8px;
    padding: 12px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.title("🌾 Crop Yield Prediction")
st.caption("Minimal • Black Theme • AI-powered")
st.divider()

# ---------------- FORM ----------------
with st.form("yield_form"):
    col1, col2 = st.columns(2)

    with col1:
        area = st.text_input("Country", "Pakistan")
        item = st.selectbox(
            "Crop",
            [
                "Maize", "Potatoes", "Rice, paddy", "Sorghum",
                "Soybeans", "Wheat", "Cassava",
                "Sweet potatoes", "Plantains and others", "Yams"
            ]
        )
        year = st.number_input("Year", 1900, 2100, 2024)

    with col2:
        rainfall = st.number_input("Average Rainfall (mm/year)", 0.0, value=750.0)
        pesticides = st.number_input("Pesticides Used (tonnes)", 0.0, value=100.0)
        temp = st.number_input("Average Temperature (°C)", -10.0, value=25.0)

    submitted = st.form_submit_button("Predict Yield")

# ---------------- API CALL ----------------
if submitted:
    payload = {
        "Area": area,
        "Item": item,
        "Year": int(year),
        "average_rain_fall_mm_per_year": float(rainfall),
        "pesticides_tonnes": float(pesticides),
        "avg_temp": float(temp),
    }

    with st.spinner("Running prediction model..."):
        try:
            response = requests.post(API_URL, json=payload, timeout=10)

            if response.status_code == 200:
                result = response.json()
                st.success("Prediction Successful")
                st.metric(
                    "Predicted Crop Yield (hg/ha)",
                    f"{result['hg/ha_yield']:,.2f}"
                )
            else:
                st.error("Backend error")
                st.code(response.text)

        except requests.exceptions.RequestException as e:
            st.error("Backend unreachable")
            st.code(str(e))

st.divider()
st.caption("FastAPI + Streamlit • Stable Dark UI")
