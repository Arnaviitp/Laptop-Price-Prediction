import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("rf_model.pkl")

# Set page config
st.set_page_config(page_title="LapApp - Laptop Price Estimator", page_icon="💻", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            background-color: #f4f4f4;
        }
        h1 {
            color: #3b82f6;
            font-family: 'Segoe UI', sans-serif;
            text-align: center;
        }
        .stButton>button {
            background-color: #3b82f6;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            height: 3em;
            width: 100%;
        }
        .stButton>button:hover {
            background-color: #2563eb;
        }
        .center-text {
            text-align: center;
            font-size: 18px;
        }
    </style>
""", unsafe_allow_html=True)

# Title and intro
st.title("💻 Laptop Price Prediction App")
st.markdown("<div class='center-text'>Estimate laptop prices with AI based on Processor Speed, RAM and Storage 🚀</div>", unsafe_allow_html=True)

st.divider()

# Input section
with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        Processor_Speed = st.number_input("⚙️ Processor Speed (GHz)", value=2.5, step=0.5)
        storage_capacity = st.number_input("💾 Storage Capacity (GB)", value=512, step=256)
    
    with col2:
        ram_size = st.number_input("🧠 RAM Size (GB)", value=16, step=8)

st.divider()

# Predict button
if st.button("🔍 Estimate Price"):
    X = [Processor_Speed, ram_size, storage_capacity]
    x1 = np.array(X)
    prediction = model.predict([x1])[0]
    st.success(f"💰 Estimated Price: ₹ {prediction:,.2f}")
    st.balloons()
else:
    st.info("Click the button above to get the laptop price estimate.")

st.divider()

# Footer
st.markdown("---")
st.markdown("<div class='center-text'>Made with ❤️ by Arnav</div>", unsafe_allow_html=True)
