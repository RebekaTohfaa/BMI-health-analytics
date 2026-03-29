import streamlit as st

st.set_page_config(layout="wide") 
if st.screen_width < 768:
    st.write("Using mobile layout")
    
# 👉 CENTERED TITLE & DESCRIPTION
st.markdown("<h1 style='text-align: center;'>📊 BMI Calculator</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Check your Body Mass Index and health category</h4>", unsafe_allow_html=True)

# 👉 CREATE 2 COLUMNS
col1, col2 = st.columns(2)

# 🟦 LEFT SIDE → TABLE
with col1:
    st.markdown("### 📊 BMI Categories")

    st.table({
        "Category": [
            "Underweight",
            "Normal",
            "Overweight",
            "Obese",
            "Severely Obese",
            "Morbidly Obese"
        ],
        "BMI Range": [
            "< 18.5",
            "18.5 - 24.9",
            "25 - 29.9",
            "30 - 34.9",
            "35 - 39.9",
            "40+"
        ]
    })

# 🟩 RIGHT SIDE → INPUTS + RESULT
with col2:
    st.markdown("### Enter your details")

    weight = st.number_input("Weight (lbs)", min_value=1.0)
    height = st.number_input("Height (inches)", min_value=1.0)

    if st.button("Calculate BMI"):
        BMI = (weight * 703) / (height * height)

        st.write(f"Your BMI: {round(BMI, 2)}")

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
