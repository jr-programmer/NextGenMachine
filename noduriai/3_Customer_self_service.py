import streamlit as st
import random

# Function simulating Generative AI suggestion for Freight Mix (FTL vs LTL)
def generative_freight_mix(weight, volume, customer_preference):
    """Generative AI suggestion for Freight Mix"""
    if customer_preference == 'Cost-Effective':
        return "LTL (Less Than Truckload)" if weight < 12000 and volume < 25 else "FTL (Full Truckload)"
    elif customer_preference == 'Speed':
        return "FTL (Full Truckload)"
    else:
        return "LTL (Less Than Truckload)" if weight < 15000 and volume < 30 else "FTL (Full Truckload)"

# Function simulating Generative AI suggestion for Route Mix (Optimized vs Green)
def generative_route_mix(distance, priority, historical_preference):
    """Generative AI suggestion for Route Mix"""
    if priority == 'Fast Delivery' or historical_preference == 'Speed':
        return "Optimized Route (Speed Priority)"
    elif distance > 300 and historical_preference == 'Eco-friendly':
        return "Green Route (Eco-friendly, Less CO2 emissions)"
    else:
        return "Optimized Route (Balanced)"

# Function simulating Generative AI suggestion for Vehicle Mix (Electric vs Diesel)
def generative_vehicle_mix(distance, weight, cargo_sensitivity, green_policy):
    """Generative AI vehicle assignment based on distance, weight, and green policies"""
    if green_policy and distance <= 200 and weight <= 6000:
        return "Electric Truck"
    elif cargo_sensitivity == 'Sensitive' and distance <= 400:
        return "Electric Truck"
    else:
        return "Diesel Truck"

# Streamlit frontend with AI-based suggestions
st.title("Generative AI-Powered Transportation Mix Optimization Tool")
st.markdown("This tool provides AI-generated mix suggestions for Freight Mix, Route Mix, and Vehicle Mix.")

# User inputs for shipment details
st.header("Shipment Details")
weight = st.number_input("Enter Cargo Weight (kg)", min_value=0, value=5000)
volume = st.number_input("Enter Cargo Volume (m³)", min_value=0.0, value=10.0)
distance = st.number_input("Enter Route Distance (km)", min_value=0, value=100)
priority = st.selectbox("Select Delivery Priority", ["Fast Delivery", "Eco-friendly", "Balanced"])

# User-specific preferences for AI suggestions
st.header("Customer Preferences")
customer_preference = st.selectbox("Freight Preference", ["Cost-Effective", "Speed", "Balanced"])
historical_preference = st.selectbox("Route Historical Preference", ["Speed", "Eco-friendly", "Balanced"])
cargo_sensitivity = st.selectbox("Cargo Sensitivity", ["Normal", "Sensitive"])
green_policy = st.checkbox("Follow Green Policy (Electric vehicles where possible)")

# Generative AI suggestions
freight_mix = generative_freight_mix(weight, volume, customer_preference)
route_mix = generative_route_mix(distance, priority, historical_preference)
vehicle_mix = generative_vehicle_mix(distance, weight, cargo_sensitivity, green_policy)

# Display the AI-optimized mix
st.header("AI-Optimized Mix Suggestions")
st.subheader("Freight Mix (FTL vs. LTL)")
st.write(f"AI-Suggested Freight Mix: **{freight_mix}**")

st.subheader("Route Mix (Optimized vs. Green)")
st.write(f"AI-Suggested Route Mix: **{route_mix}**")

st.subheader("Vehicle Mix (Electric vs. Diesel)")
st.write(f"AI-Suggested Vehicle Mix: **{vehicle_mix}**")

# Option to refresh or recalculate
st.button("Recalculate AI-Generated Mix")
