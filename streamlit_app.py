import streamlit as st
import pandas as pd
import numpy as np
import joblib
import pickle

# Load the model and preprocessor
with open("model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Streamlit web application
st.set_page_config(
    page_title="Student's Academic Achievement Analyzer",
    page_icon="🎓",
    layout="wide"
)

st.title("Student's Academic Achievement Analyzer")

# Function to transform the user input
def transform_input(data):
    le = joblib.load("label_encoders.joblib")
    for col in ['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']:
        data[col] = le[col].transform(data[col])
    data['reading_score'] = np.log(data['reading_score'])
    data['writing_score'] = np.log(data['writing_score'])
    return data

# User inputs
gender = st.selectbox("Gender:", options=['female', 'male'])
race_ethnicity = st.selectbox("Race/Ethnicity:", options=['group A', 'group B', 'group C', 'group D', 'group E'])
parental_level_of_education = st.selectbox("Parental Level of Education:", options=["bachelor's degree", 'some college', "master's degree", "associate's degree", 'high school', 'some high school'])
lunch = st.selectbox("Lunch:", options=['standard', 'free/reduced'])
test_preparation_course = st.selectbox("Test Preparation Course:", options=['none', 'completed'])
reading_score = st.number_input("Reading Score:", min_value=0, max_value=100, step=1)
writing_score = st.number_input("Writing Score:", min_value=0, max_value=100, step=1)

# Collect user input into a DataFrame
x_new = pd.DataFrame({
    'gender': [gender],
    'race_ethnicity': [race_ethnicity],
    'parental_level_of_education': [parental_level_of_education],
    'lunch': [lunch],
    'test_preparation_course': [test_preparation_course],
    'reading_score': [reading_score],
    'writing_score': [writing_score],
})

# Display the prediction
if st.button("Predict"):
    try:
        # Transform the input data
        x_new_transformed = transform_input(x_new)
        
        # Make prediction
        prediction = model.predict(x_new_transformed)
        
        st.info(f"The predicted math score is: {prediction[0]}")
    except Exception as e:
        st.error(f"Error making prediction: {e}")
