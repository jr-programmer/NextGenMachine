import streamlit as st
import random

# Function to simulate distance calculation (You can replace this with an actual API like Google Maps)
def calculate_distance(start_point, destination):
    # This is a simulated distance in kilometers (in reality, you'd use a mapping API like Google Maps)
    return random.uniform(100, 1000)  # Distance between 100 km to 1000 km

# Function to estimate cost based on the load type (FTL or LTL)
def calculate_cost(distance, method, fuel_cost_per_km=1.5, ftl_rate=2.0, ltl_rate=1.0):
    if method == 'FTL':
        return distance * (fuel_cost_per_km + ftl_rate)
    elif method == 'LTL':
        return distance * (fuel_cost_per_km + ltl_rate)

# Simulate best route determination (this would normally involve a routing algorithm or API)
def get_best_route(start_point, destination):
    # For this example, we're returning a simple simulated route
    return f"The best route from {start_point} to {destination} passes through major highways and avoids tolls."

# Streamlit Frontend
st.title("Route Optimization - Truck Fleet")
st.markdown("Enter the start point and destination to estimate costs and suggest the best route.")

# User inputs
start_point = st.text_input("Enter Start Point")
destination = st.text_input("Enter Destination")

if start_point and destination:
    # Calculate distance
    distance = calculate_distance(start_point, destination)
    
    # Calculate cost estimates for FTL and LTL
    ftl_cost = calculate_cost(distance, 'FTL')
    ltl_cost = calculate_cost(distance, 'LTL')
    
    # Get the best route
    best_route = get_best_route(start_point, destination)
    
    # Display results
    st.subheader(f"Route Details: {start_point} to {destination}")
    st.write(f"Estimated Distance: {distance:.2f} km")
    
    st.subheader("Cost Estimation")
    st.write(f"**Full Truckload (FTL) Cost:** ${ftl_cost:.2f}")
    st.write(f"**Less Than Truckload (LTL) Cost:** ${ltl_cost:.2f}")
    
    st.subheader("Best Route")
    st.write(best_route)
else:
    st.write("Please enter both the start point and destination to calculate route and costs.")
