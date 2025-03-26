#Project 8 
#BMI Calculator Web App using Python and Streamlit by Rida Fatima!


import streamlit as st
import time

# Page configuration
st.set_page_config(page_title="BMI Calculator", page_icon="⚖️", layout="centered")

# App Title
st.title("Body Mass Index (BMI) Calculator")
#Description
st.write("Easily calculate your BMI and check if you're in a healthy range.")

# User input section
st.markdown("### Enter Your Details:")
col1, col2 = st.columns(2)

with col1:
    weight = st.number_input("Weight (kg):", min_value=1.0, format="%.2f")

with col2:
    height = st.number_input("Height (m):", min_value=1.0, format="%.2f")

# Calculate BMI when valid values are entered
if height > 0 and weight > 0:
    bmi = weight / (height ** 2)

    # Show progress bar effect
    with st.spinner("Calculating BMI..."):
        time.sleep(1)

    st.subheader("Your BMI Score:")
    st.markdown(f"### **{bmi:.2f}**")

    # Determine BMI category
    if bmi < 18.5:
        st.warning("**Underweight** - Your BMI is below the healthy range.")
        advice = "Consider increasing your calorie intake with a nutritious diet."
    elif 18.5 <= bmi < 24.9:
        st.success("**Normal Weight** - Your BMI is within the healthy range!")
        advice = "Maintain a balanced diet and regular physical activity."
    elif 25 <= bmi < 29.9:
        st.warning("**Overweight** - Your BMI is slightly above the healthy range.")
        advice = "A combination of healthy eating and regular exercise is recommended."
    else:
        st.error("**Obese** - Your BMI is significantly above the healthy range.")
        advice = "Consulting a healthcare professional for guidance is advisable."

    # Display advice
    st.info(f"💡 {advice}")

    # Add progress bar (BMI normalized to a 0-1 scale)
    st.progress(min(bmi / 40, 1))

else:
    st.info("Please enter a valid weight and height.")

# Footer
st.markdown("---")
st.write("Developed with ❤️ by **Rida Fatima**")
