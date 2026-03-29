import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="BMI Analytics Dashboard", layout="wide")

# -------------------------------
# CUSTOM CSS
# -------------------------------
st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
}
.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
}
.subtitle {
    text-align: center;
    font-size: 18px;
    color: gray;
    margin-bottom: 30px;
}
.card {
    padding: 20px;
    border-radius: 12px;
    background-color: #f9f9f9;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
}
.result-box {
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# TITLE
# -------------------------------
st.markdown('<div class="title">📊 BMI Analytics Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Check your Body Mass Index and health category</div>', unsafe_allow_html=True)

# -------------------------------
# LAYOUT
# -------------------------------
col1, col2 = st.columns([1, 1])

# -------------------------------
# LEFT SIDE: BMI TABLE
# -------------------------------
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📋 BMI Categories")

    bmi_data = {
        "Category": [
            "Underweight", "Normal", "Overweight",
            "Obese", "Severely Obese", "Morbidly Obese"
        ],
        "BMI Range": [
            "< 18.5", "18.5 - 24.9", "25 - 29.9",
            "30 - 34.9", "35 - 39.9", "40+"
        ]
    }

    df = pd.DataFrame(bmi_data)
    st.dataframe(df, use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# RIGHT SIDE: INPUT + RESULT
# -------------------------------
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📥 Enter your details")

    weight = st.number_input("Weight (lbs)", min_value=1.0, value=150.0)
    height = st.number_input("Height (inches)", min_value=1.0, value=65.0)

    # Initialize BMI
    bmi = None

    if st.button("Calculate BMI"):
        bmi = (weight / (height ** 2)) * 703

        # CATEGORY LOGIC
        if bmi < 18.5:
            category = "Underweight"
            color = "#3498db"
        elif 18.5 <= bmi < 25:
            category = "Normal"
            color = "#2ecc71"
        elif 25 <= bmi < 30:
            category = "Overweight"
            color = "#f1c40f"
        elif 30 <= bmi < 35:
            category = "Obese"
            color = "#e67e22"
        else:
            category = "Severely Obese"
            color = "#e74c3c"

        # RESULT BOX
        st.markdown(
            f"""
            <div class="result-box" style="background-color:{color}; color:white;">
                Your BMI: {bmi:.2f} <br>
                Status: {category}
            </div>
            """,
            unsafe_allow_html=True
        )

        # PROGRESS BAR
        progress = min(bmi / 40, 1.0)
        st.progress(progress)
        st.caption("BMI progress relative to maximum scale (40)")

        # -------------------------------
        # GAUGE CHART (SAFE - NO ERROR)
        # -------------------------------
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=bmi,
            title={'text': "BMI Score"},
            gauge={
                'axis': {'range': [0, 40]},
                'bar': {'color': "black"},
                'steps': [
                    {'range': [0, 18.5], 'color': "#3498db"},
                    {'range': [18.5, 25], 'color': "#2ecc71"},
                    {'range': [25, 30], 'color': "#f1c40f"},
                    {'range': [30, 40], 'color': "#e74c3c"},
                ],
            }
        ))

        st.plotly_chart(fig, use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("""
---
<center>Built by Rebeka | Fashion Tech Studio</center>
""", unsafe_allow_html=True)
