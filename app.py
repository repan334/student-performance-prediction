import streamlit as st
import pandas as pd
import joblib

model = joblib.load("models/student_model.pkl")

st.title("Student Performance Prediction")

st.write(
    "Predict whether a student is likely to pass based on selected characteristics."
)

studytime = st.slider(
    "Study Time",
    min_value=0,
    max_value=4,
    value=2
)

failures = st.number_input(
    "Number of Failures",
    min_value=0,
    max_value=3,
    value=0
)

absences = st.number_input(
    "Number of Absences",
    min_value=0,
    max_value=100,
    value=5
)

freetime = st.slider(
    "Free Time",
    min_value=1,
    max_value=5,
    value=3
)

goout = st.slider(
    "Going Out",
    min_value=1,
    max_value=5,
    value=3
)

health = st.slider(
    "Health",
    min_value=1,
    max_value=5,
    value=3
)

Medu = st.slider(
    "Mother Education",
    min_value=0,
    max_value=4,
    value=2
)

Fedu = st.slider(
    "Father Education",
    min_value=0,
    max_value=4,
    value=2
)

if st.button("Predict Performance"):

    input_data = pd.DataFrame({
        "studytime": [studytime],
        "failures": [failures],
        "absences": [absences],
        "freetime": [freetime],
        "goout": [goout],
        "health": [health],
        "Medu": [Medu],
        "Fedu": [Fedu]
    })
    
    prediction = model.predict(input_data)[0]
    st.success(f"Prediction: {prediction}")