import streamlit as st

# Set up the page configuration
st.set_page_config(
    page_title="Business Operations Platform",
    page_icon=":gear:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Sidebar - Navigation
st.sidebar.title("Business Operations Platform")
st.sidebar.markdown("Navigate through the modules")

# Define navigation options
pages = {
    "Asset Management": "Manage and track your assets efficiently in real-time.",
    "Route Optimization": "Optimize logistics routes to reduce time and cost.",
    "Customer Self-Service": "Empower customers with AI-driven self-service tools.",
    "AI Bidding Procurement": "Utilize AI to enhance procurement and bidding processes."
}

# Sidebar - Module Selection
selection = st.sidebar.radio("Choose a module", list(pages.keys()))

# Header
st.title(f"{selection} Module")
st.markdown(f"### {pages[selection]}")

# Main area
if selection == "Asset Management":
    st.subheader("Asset Overview")
    st.write("Track assets in real-time and manage lifecycle status.")
    
    # Example interactive elements for asset management
    st.text_input("Search for an asset by ID or Name")
    st.selectbox("Asset Type", ["Vehicles", "Machinery", "Buildings", "Tools"])
    st.button("View Asset Details")

elif selection == "Route Optimization":
    st.subheader("Logistics Optimization")
    st.write("Improve logistics efficiency by optimizing routes based on traffic, distance, and cost.")
    
    # Example interactive elements for route optimization
    st.text_input("Enter Origin")
    st.text_input("Enter Destination")
    st.slider("Weight Importance of Time vs Cost", 0, 100, 50)
    st.button("Optimize Route")

elif selection == "Customer Self-Service":
    st.subheader("AI-Powered Customer Portal")
    st.write("Provide your customers with seamless, self-service options.")
    
    # Example interactive elements for customer self-service
    st.text_input("Customer ID")
    st.selectbox("Select Service Request", ["Check Order Status", "Raise Issue", "Get a Quote"])
    st.button("Submit Request")
    
elif selection == "AI Bidding Procurement":
    st.subheader("AI-Driven Procurement")
    st.write("Leverage AI to enhance procurement decisions and bid strategies.")
    
    # Example interactive elements for AI bidding
    st.text_input("Enter Procurement ID")
    st.number_input("Bid Amount ($)", min_value=0.0, format="%.2f")
    st.selectbox("Supplier", ["Supplier A", "Supplier B", "Supplier C"])
    st.button("Submit Bid")

# Footer - Add some description and user support
st.sidebar.markdown("---")
st.sidebar.write("For assistance, contact support@example.com")
st.sidebar.markdown("© 2024 Business Operations Platform")

