import streamlit as st
import requests
import numpy as np

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="SecurePay AI",
    page_icon="💳",
    layout="wide"
)

# ---------------- DARK PURPLE THEME ----------------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f0c29, #1a1a2e, #000000);
    color: white;
}

.stButton>button {
    background-color: #6a0dad;
    color: white;
    font-weight: bold;
    border-radius: 10px;
    height: 3em;
    width: 100%;
}

.stNumberInput input {
    background-color: #1e1e2f !important;
    color: white !important;
}

h1, h2, h3 {
    color: #bb86fc;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("💳 SecurePay AI - Fraud Detection System")
st.write("Enter transaction details below to check fraud probability.")

# ---------------- INPUT SECTION ----------------
col1, col2, col3 = st.columns(3)

features = []

with col1:
    for i in range(1, 11):
        val = st.number_input(f"V{i}", value=0.0, format="%.5f")
        features.append(val)

with col2:
    for i in range(11, 21):
        val = st.number_input(f"V{i}", value=0.0, format="%.5f")
        features.append(val)

with col3:
    for i in range(21, 29):
        val = st.number_input(f"V{i}", value=0.0, format="%.5f")
        features.append(val)

    amount = st.number_input("Amount", value=0.0)
    time = st.number_input("Time", value=0.0)

    features.append(amount)
    features.append(time)

# ---------------- PREDICT BUTTON ----------------
if st.button("🚀 Predict Fraud"):

    try:
        url = "http://127.0.0.1:8000/predict"

        response = requests.post(
            url,
            json={"features": features}
        )

        result = response.json()

        prediction = result["prediction"]
        probability = result["fraud_probability"]

        st.markdown("---")

        if prediction == 1:
            st.error("🚨 Fraud Transaction Detected!")
        else:
            st.success("✅ Legitimate Transaction")

        st.write(f"**Fraud Probability:** {round(probability * 100, 2)} %")

    except Exception as e:
        st.error("❌ Backend connection failed. Make sure FastAPI server is running.")
        st.write(e)