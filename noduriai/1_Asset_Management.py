import streamlit as st
import pandas as pd
import numpy as np
import random
import datetime

# Simulated function to get sensor data
def get_sensor_data():
    trucks = ["Truck A", "Truck B", "Truck C", "Truck D", "Truck E"]
    sensor_data = []

    for truck in trucks:
        data = {
            "Truck ID": truck,
            "Engine Temp (C)": random.uniform(60, 110),  # Temperature between 60 and 110 degrees Celsius
            "Oil Level (%)": random.uniform(20, 100),   # Oil level percentage
            "Tire Pressure (PSI)": random.uniform(20, 35),  # Tire pressure in PSI
            "Brake Wear (%)": random.uniform(0, 100),    # Brake wear percentage
            "Timestamp": datetime.datetime.now(),
        }
        sensor_data.append(data)
    
    return pd.DataFrame(sensor_data)

# Predictive maintenance logic
def predictive_maintenance(df):
    alerts = []
    for _, row in df.iterrows():
        # Set thresholds
        if row['Engine Temp (C)'] > 90:
            alerts.append(f"High Engine Temperature Alert for {row['Truck ID']}")
        if row['Oil Level (%)'] < 30:
            alerts.append(f"Low Oil Level Alert for {row['Truck ID']}")
        if row['Tire Pressure (PSI)'] < 25:
            alerts.append(f"Low Tire Pressure Alert for {row['Truck ID']}")
        if row['Brake Wear (%)'] > 80:
            alerts.append(f"Brake Wear Alert for {row['Truck ID']}")
    return alerts

# Streamlit Frontend
st.set_page_config(page_title="Truck Fleet - Predictive Maintenance", page_icon="🚛", layout="wide")
st.title("Predictive Maintenance Dashboard")
st.markdown("Real-time monitoring and maintenance alerts for your truck fleet.")

# Display sensor data and alerts
sensor_data = get_sensor_data()
st.subheader("Sensor Readings")
st.write(sensor_data)

st.subheader("Maintenance Alerts")
alerts = predictive_maintenance(sensor_data)

if alerts:
    for alert in alerts:
        st.warning(alert)
else:
    st.success("All trucks are operating normally.")

# Simulate updating the data every few seconds
st.button("Refresh Data")

