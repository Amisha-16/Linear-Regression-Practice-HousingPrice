# app.py
import streamlit as st
import pickle
import pandas as pd

# -----------------------------
# Page configuration
st.set_page_config(page_title="California Housing Predictor", layout="wide")

# -----------------------------
# Sidebar for inputs
st.sidebar.header("🏠 Enter Housing Features")
MedInc = st.sidebar.number_input("Median Income", value=3.0)
HouseAge = st.sidebar.number_input("House Age", value=20)
AveRooms = st.sidebar.number_input("Average Rooms", value=5.0)
AveBedrms = st.sidebar.number_input("Average Bedrooms", value=1.0)
Population = st.sidebar.number_input("Population", value=1000)
AveOccup = st.sidebar.number_input("Average Occupancy", value=3.0)
Latitude = st.sidebar.number_input("Latitude", value=34.0)
Longitude = st.sidebar.number_input("Longitude", value=-118.0)

# -----------------------------
# Main title + description
st.markdown("<h1 style='text-align:center; color:darkblue;'>🏡 California Housing Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:18px; color:gray;'>Predict the <b>median house value</b> based on your inputs</p>", unsafe_allow_html=True)
st.markdown("---")

# -----------------------------
# Load model
try:
    with open("model.pkl", "rb") as f:
        regression = pickle.load(f)
    st.success(" Model loaded successfully")
except Exception as e:
    st.error(f" Error loading model: {e}")
    regression = None

# -----------------------------
# Prediction button + result
if st.button("Predict 💰"):
    if regression:
        input_df = pd.DataFrame([[
            MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude
        ]], columns=['MedInc','HouseAge','AveRooms','AveBedrms','Population','AveOccup','Latitude','Longitude'])
        
        pred = regression.predict(input_df)
        st.markdown(f"<h2 style='text-align:center; color:green;'>💵 Predicted Median House Value: ${pred[0]*100000:.2f}</h2>", unsafe_allow_html=True)
    else:
        st.warning("Model not loaded, prediction not possible.")

# -----------------------------
# Footer tip
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray;'>🔹 Try changing the values in the sidebar to see how house prices vary!</p>", unsafe_allow_html=True)
import streamlit as st

st.write("App started")

import sklearn
st.write("sklearn loaded")
