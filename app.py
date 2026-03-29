import streamlit as st

# Title
st.title("📊 BMI Calculator")
st.markdown("### Check your Body Mass Index and health category")

# 👉 MOVE TABLE HERE
st.markdown("### 📊 BMI Categories")

st.table({
    "Category": ["Underweight", "Normal", "Overweight", "Obese", "Severely Obese", "Morbidly Obese"],
    "BMI Range": ["< 18.5", "18.5 - 24.9", "25 - 29.9", "30 - 34.9", "35 - 39.9", "40+"]
})

# Inputs
st.markdown("### Enter your details")

weight = st.number_input("Weight (lbs)", min_value=1.0)
height = st.number_input("Height (inches)", min_value=1.0)

# Button
if st.button("Calculate BMI"):
    BMI = (weight * 703) / (height * height)

    st.write(f"Your BMI: {round(BMI,2)}")

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
        else:
            st.error("You are Morbidly Obese.")
