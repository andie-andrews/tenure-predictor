import streamlit as st
import pandas as pd
import joblib

# Load model artifacts
rf = joblib.load("rf_model.pkl")
feature_columns = joblib.load("model_features.pkl")

st.title("Employee Turnover Risk Predictor")

st.write("Enter employee information to predict turnover risk.")

# Sidebar inputs
satisfaction = st.slider("Satisfaction Level", 0.0, 1.0, 0.5)
evaluation = st.slider("Last Evaluation Score", 0.0, 1.0, 0.5)
projects = st.number_input("Number of Projects", 1, 10, 3)
hours = st.number_input("Average Monthly Hours", 80, 320, 160)
tenure = st.number_input("Years at Company", 1, 10, 3)
accident = st.selectbox("Work Accident", [0, 1])
promotion = st.selectbox("Promotion in Last 5 Years", [0, 1])

# Build input dict
input_data = {
    "satisfaction_level": satisfaction,
    "last_evaluation": evaluation,
    "number_project": projects,
    "average_montly_hours": hours,
    "time_spend_company": tenure,
    "Work_accident": accident,
    "promotion_last_5years": promotion
}

# Convert to DataFrame
input_df = pd.DataFrame([input_data])
input_df = input_df.reindex(columns=feature_columns, fill_value=0)

# Predict
prob = rf.predict_proba(input_df)[0][1]

st.metric("Turnover Probability", f"{prob:.2%}")

# Risk zone
if prob < 0.20:
    st.success("Safe Zone (Green)")
elif prob < 0.60:
    st.warning("Low Risk Zone (Yellow)")
elif prob < 0.90:
    st.warning("Medium Risk Zone (Orange)")
else:
    st.error("High Risk Zone (Red)")
st.info("Note: This prediction is based on historical data and may not be definitive.")