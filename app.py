import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="📊")

st.title("📊 BMI Calculator")
st.markdown("### Check your Body Mass Index and health category")

# Input section
st.subheader("Enter your details")

weight = st.number_input("Weight (lbs)", min_value=1.0)
height = st.number_input("Height (inches)", min_value=1.0)

# Button
if st.button("Calculate BMI"):
    BMI = (weight * 703) / (height * height)

    st.subheader(f"Your BMI: {BMI:.2f}")

    # Category
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

    # Insight section
    st.markdown("---")
    st.subheader("📌 Insight")
    st.write("BMI is a simple indicator used to assess body weight relative to height. It helps identify potential health risks.")
