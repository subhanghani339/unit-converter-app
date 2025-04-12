import streamlit as st

# Conversion data
unit_conversions = {
    "Length": {
        "Meter": 1.0,
        "Kilometer": 0.001,
        "Centimeter": 100.0,
        "Millimeter": 1000.0,
        "Mile": 0.000621371,
        "Yard": 1.09361,
        "Foot": 3.28084,
        "Inch": 39.3701
    },
    "Weight": {
        "Kilogram": 1.0,
        "Gram": 1000.0,
        "Milligram": 1_000_000.0,
        "Pound": 2.20462,
        "Ounce": 35.274
    },
    "Temperature": {
        "Celsius": "C",
        "Fahrenheit": "F",
        "Kelvin": "K"
    },
    "Time": {
        "Second": 1.0,
        "Minute": 1 / 60,
        "Hour": 1 / 3600,
        "Day": 1 / 86400
    },
    "Speed": {
        "Meter per second": 1.0,
        "Kilometer per hour": 3.6,
        "Mile per hour": 2.23694,
        "Foot per second": 3.28084
    }
}

# Function to convert length, weight, time, and speed
def convert_units(value, from_unit, to_unit, category):
    if category in ["Length", "Weight", "Time", "Speed"]:
        return value * (unit_conversions[category][to_unit] / unit_conversions[category][from_unit])
    return value  # Default return

# Function to convert temperature separately
def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
    return value  # Default return

# Streamlit UI
st.title("🔢 Unit Converter")
st.markdown("Convert Length, Weight, Temperature, Time, and Speed dynamically in real-time.")

# Select Category
category = st.selectbox("Select conversion category:", list(unit_conversions.keys()), index=0)

# Create two columns
col1, col2, col3 = st.columns([4, 1, 4])  # Left for input, Right for result

with col1:
    # User input value
    value = st.number_input("Enter Value:", min_value=0.0, format="%.2f", key="from_value")

    # Select 'From' unit
    from_unit = st.selectbox("From:", list(unit_conversions[category].keys()), key="from_unit")

with col2:
    # Display equal sign
    st.markdown("<h2 style='text-align: center; margin-top: 50px;'>=</h2>", unsafe_allow_html=True)

with col3:
    # Convert and display converted value
    if category == "Temperature":
        result = convert_temperature(value, from_unit, from_unit)  # Default value in case of no change
    else:
        result = convert_units(value, from_unit, from_unit, category)

    st.number_input("Converted Value:", value=result, key="to_value", disabled=True)

    # Select 'To' unit
    to_unit = st.selectbox("To:", list(unit_conversions[category].keys()), key="to_unit")

# Recalculate conversion on user input
if category == "Temperature":
    result = convert_temperature(value, from_unit, to_unit)
else:
    result = convert_units(value, from_unit, to_unit, category)

# Display the final result dynamically
st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")