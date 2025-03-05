import streamlit as st

st.title("Unit Converter")

measurement_type = st.selectbox("Choose Measurement Type:", ["Length"])
length_units = {
    "Meter (m)": 1.0,
    "Centimeter (cm)": 0.01,
    "Kilometer (km)": 1000.0,
    "Inch (in)": 0.0254,
    "Foot (ft)": 0.3048
}

if measurement_type == "Length":
    from_unit = st.selectbox("From Unit:", list(length_units.keys()))
    to_unit = st.selectbox("To Unit:", list(length_units.keys()))
    
    input_value = st.number_input("Enter the value to convert:", value=1.0, step=0.1)

    if st.button("Convert"):
       
        value_in_meters = input_value * length_units[from_unit]
        
        result = value_in_meters / length_units[to_unit]
        
        st.write(f"{input_value} {from_unit} = {result} {to_unit}")