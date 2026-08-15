import joblib 
import pandas as pd 
import streamlit as st  

from src.config import MODEL_PATH

st.title("Academic Success Tool")
st.warning("This prediction supports human review. It's not a final decision!")

pipeline = joblib.load(MODEL_PATH)

st.header("Week-4 student information")

age_band = st.selectbox("Age band", ["18-20", "21-24", "25+"])

entry_route = st.selectbox("Entry route", ["Direct", "Access", "Transfer"])

prior_gpa = st.number_input("Prior GPA", min_value=0.0, max_value=4.0, value=2.6, step=0.01)

first_generation = st.selectbox("First generation student?", ["No", "Yes"])

financial_support = st.selectbox("Receiving financial support?", ["No", "Yes"])

distance_km = st.number_input("Distance from campus (km)", min_value=0.0, value=15.0, step=0.5)

week4_attendance_rate = st.slider("Week-4 attendance rate", 0.0, 1.0, 0.8)

week4_lms_logins = st.number_input("Week-4 LMS logins", min_value=0, value=5, step=1)

assignment1_score = st.number_input("Assignment 1 score", min_value=0.0, max_value=100.0, value=65.0, step=0.5)

support_sessions_week4 = st.number_input("Support sessions used (week 4)", min_value=0, value=1, step=1)

if st.button("Predict"):
  input_df = pd.DataFrame([{
    "age_band": age_band,
    "entry_route": entry_route,
    "prior_gpa": prior_gpa,
    "first_generation": 1 if first_generation == "Yes" else 0,
    "financial_support": 1 if financial_support == "Yes" else 0,
    "distance_km": distance_km,
    "week4_attendance_rate": week4_attendance_rate,
    "week4_lms_logins": week4_lms_logins,
    "assignment1_score": assignment1_score,
    "support_sessions_week4": support_sessions_week4,
  }])
  
  probability = pipeline.predict_proba(input_df)[0][1]
  st.metric("Predicted probability of academic success", f"{probability:.1%}")