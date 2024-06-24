import streamlit as st
import pickle
import numpy as np

# Load the model
model = pickle.load(open(r"C:\Users\User\Desktop\watt-sage\model.pkl", 'rb'))

# Define the Streamlit app
st.title("Energy Consumption Prediction")

# Create input fields
Global_active_power = st.number_input('Global Active Power', min_value=0.0, step=0.01)
Global_reactive_power = st.number_input('Global Reactive Power', min_value=0.0, step=0.01)
Voltage = st.number_input('Voltage', min_value=0.0, step=0.01)
Global_intensity = st.number_input('Global Intensity', min_value=0.0, step=0.01)
Total_metering = st.number_input('Total Metering', min_value=0.0, step=0.01)

# Predict button
if st.button('Predict'):
    try:
        # Make prediction
        input_features = np.array([Global_active_power, Global_reactive_power, Voltage, Global_intensity, Total_metering]).reshape(1, -1)
        result = model.predict(input_features)

        # Display the prediction
        st.success(f'Predicted Energy Consumption: {result[0]}')
    except ValueError as e:
        st.error("Error: Invalid input data. Please make sure all fields are filled with valid numbers.")

# Run the app
if __name__ == '__main__':
    st.write("Streamlit app is running...")
