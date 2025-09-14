import streamlit as st
import pandas as pd
import numpy as np
import pickle

model=pickle.load(open("rfmodel.pkl","rb"))
scaler=pickle.load(open("scaler.pkl","rb"))

st.title("Sustainable Energy Consumption Prediction")
st.write("Predict appliance energy usage based on environmental factors.")

temp = st.number_input("Temperature (°C)", 0.0, 50.0, 20.0)
hum = st.number_input("Humidity (%)", 0.0, 100.0, 40.0)
windspeed = st.number_input("Windspeed (m/s)", 0.0, 20.0, 2.0)
hour = st.slider("Hour of Day", 0, 23, 12)
day = st.slider("Day of Week (0=Monday, 6=Sunday)", 0, 6, 2)

features = np.array([[temp, hum, windspeed, hour, day]])
features_scaled = scaler.transform(features)

prediction = model.predict(features_scaled)[0]

st.subheader(f"Predicted Appliance Energy Usage: {prediction:.2f} Wh")
