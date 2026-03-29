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

st.markdown("### 📊 BMI Categories")

st.table({
    "Category": ["Underweight", "Normal", "Overweight", "Obese", "Severely Obese", "Morbidly Obese"],
    "BMI Range": ["< 18.5", "18.5 - 24.9", "25 - 29.9", "30 - 34.9", "35 - 39.9", "40+"]
})

if BMI < 18.5:
    st.info("Consider a balanced diet and consult a healthcare provider.")
elif BMI < 24.9:
    st.info("Great! Maintain your healthy lifestyle.")
elif BMI < 29.9:
    st.info("Try increasing physical activity and improving diet habits.")
else:
    st.info("Consider consulting a healthcare professional for guidance.")
