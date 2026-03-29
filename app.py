import streamlit as st

st.title("📊 BMI Calculator")

# Input
weight = st.number_input("Enter your weight (lbs)", min_value=1.0)
height = st.number_input("Enter your height (inches)", min_value=1.0)

# Button
if st.button("Calculate BMI"):
    BMI = (weight * 703) / (height * height)

    st.write(f"Your BMI is: {BMI:.2f}")

    # Your logic (converted properly)
    if BMI > 0:
        if BMI < 18.5:
            st.warning("You are underweight.")
        elif BMI < 24.9:
            st.success("You are Normal Weight.")
        elif BMI < 29.9:
            st.warning("You are Overweight.")
        elif BMI < 34.9:
            st.error("You are Obese.")
        elif BMI < 39.9:
            st.error("You are Severely Obese.")
        elif BMI >= 40:
            st.error("You are Morbidly Obese.")
