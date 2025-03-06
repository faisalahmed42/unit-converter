import streamlit as st  # Import Streamlit for building the web app

# Function to convert units based on predefined conversion factors
def convert_units(value, unit_from, unit_to):
    conversions = {
        "meters_kilometers": 0.001,    # 1 meter = 0.001 kilometers
        "kilometers_meters": 1000,     # 1 kilometer = 1000 meters
        "grams_kilograms": 0.001,      # 1 gram = 0.001 kilograms
        "kilograms_grams": 1000,       # 1 kilogram = 1000 grams
    }
    
    key = f"{unit_from}_{unit_to}"  # Generate a key based on the input and output units
    return value * conversions[key] if key in conversions else "Conversion not supported"

# Set up the app title with a styled header
st.title("⚖️ Unit Converter")
st.markdown("Convert between different units effortlessly!")

# User input for numerical value
value = st.number_input("Enter the value:", min_value=1.0, step=1.0)

# Dropdown menus for unit selection
unit_from = st.selectbox("Convert from:", ["meters", "kilometers", "grams", "kilograms"])
unit_to = st.selectbox("Convert to:", ["meters", "kilometers", "grams", "kilograms"])

# Button to perform conversion
if st.button("🔄 Convert"):
    result = convert_units(value, unit_from, unit_to)
    
    # Display result with styling
    st.success(f"✅ Converted value: {result}")
