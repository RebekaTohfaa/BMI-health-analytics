import streamlit as st
import plotly.graph_objects as go

# 🔥 PAGE CONFIG (must be first Streamlit command)
st.set_page_config(layout="wide")

# 🎯 HEADER (Centered)
st.markdown("<h1 style='text-align: center;'>📊 BMI Calculator</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Check your Body Mass Index and health category</h4>", unsafe_allow_html=True)

# 🎯 CREATE LAYOUT
col1, col2 = st.columns([1, 1.2])

# 🟦 LEFT SIDE → BMI TABLE
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

# 🟩 RIGHT SIDE → INPUTS + RESULTS
with col2:
    st.markdown("### Enter your details")

    weight = st.number_input("Weight (lbs)", min_value=1.0, step=1.0)
    height = st.number_input("Height (inches)", min_value=1.0, step=1.0)

    # 🎯 BUTTON
    if st.button("Calculate BMI"):

        BMI = (weight * 703) / (height * height)

        st.subheader(f"Your BMI: {round(BMI, 2)}")

        # 🎯 BMI CATEGORY LOGIC (YOUR ORIGINAL LOGIC)
        if BMI > 0:
            if BMI < 18.5:
                category = "Underweight"
                st.warning("You are underweight.")
            elif BMI < 24.9:
                category = "Normal Weight"
                st.success("You are Normal Weight.")
            elif BMI < 29.9:
                category = "Overweight"
                st.warning("You are Overweight.")
            elif BMI < 34.9:
                category = "Obese"
                st.error("You are Obese.")
            elif BMI < 39.9:
                category = "Severely Obese"
                st.error("You are Severely Obese.")
            else:
                category = "Morbidly Obese"
                st.error("You are Morbidly Obese.")

        # 🔥 BMI GAUGE CHART (VISUAL UPGRADE)
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=BMI,
            title={'text': "BMI Scale"},
            gauge={
                'axis': {'range': [10, 45]},
                'bar': {'color': "blue"},
                'steps': [
                    {'range': [10, 18.5], 'color': "lightblue"},
                    {'range': [18.5, 24.9], 'color': "green"},
                    {'range': [25, 29.9], 'color': "orange"},
                    {'range': [30, 45], 'color': "red"}
                ],
            }
        ))

        st.plotly_chart(fig, use_container_width=True)

        # 💡 INSIGHTS (ANALYST THINKING)
        st.markdown("### 💡 Health Insight")

        if BMI < 18.5:
            st.info("Low BMI may indicate undernutrition. Consider consulting a healthcare provider.")
        elif BMI < 24.9:
            st.info("Great! You are in a healthy range. Maintain your lifestyle.")
        elif BMI < 29.9:
            st.info("You are slightly above the normal range. Regular exercise is recommended.")
        else:
            st.info("Higher BMI may increase health risks. Consider lifestyle changes or medical advice.")

# 🎯 FOOTER
st.markdown("---")
st.caption("Developed by Rebeka Islam | Data Analytics Project")
st.markdown("""
---
<center>Built by Rebeka | Fashion Tech Studio</center>
""", unsafe_allow_html=True)
