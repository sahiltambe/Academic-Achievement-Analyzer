import pandas as pd
import numpy as np
from pyscript import Element
from js import document, window
import pickle

# Disable warnings by pyscript appearing in the browser.
import warnings
warnings.filterwarnings("ignore")

with open("model.pkl", "rb") as f:
    loaded_model = pickle.load(f)

def get_predictions():
    data = {
            "gender": document.querySelector("#gender").value,
            "ethnicity": document.querySelector("#ethnicity").value,
            "parental_level_of_education": document.querySelector("#parental_level_of_education").value,
            "lunch": document.querySelector("#lunch").value,
            "test_preparation_course": document.querySelector("#test_preparation_course").value,
            "reading_score": document.querySelector("#reading_score").value,
            "writing_score": document.querySelector("#writing_score").value,
        }
    
    # print("Data", data)

    if data["gender"]=="Male":
        gender = 1
    elif data["gender"]=="Female":
        gender = 0
    
    if data["ethnicity"]=="Group A":
        ethnicity = 0
    elif data["ethnicity"]=="Group B":
        ethnicity = 1
    elif data["ethnicity"]=="Group C":
        ethnicity = 2
    elif data["ethnicity"]=="Group D":
        ethnicity = 3
    else:
        ethnicity = 4
    
    if data["parental_level_of_education"]=="associate's degree":
        parental_level_of_education = 0
    elif data["parental_level_of_education"]=="bachelor's degree":
        parental_level_of_education = 1
    elif data["parental_level_of_education"]=="high school":
        parental_level_of_education = 2
    elif data["parental_level_of_education"]=="master's degree":
        parental_level_of_education = 3
    elif data["parental_level_of_education"]=="some college":
        parental_level_of_education = 4
    elif data["parental_level_of_education"]=="some high school":
        parental_level_of_education = 5
    else:
        parental_level_of_education = 6

    if data["lunch"]=="free/reduced":
        lunch = 0
    elif data["lunch"]=="standard":
        lunch = 1
    else:
        lunch = 2

    if data["test_preparation_course"]=="None":
        test_preparation_course = 0
    elif data["test_preparation_course"]=="Completed":
        test_preparation_course = 1
    else:
        test_preparation_course = 2

    reading_score = np.log(int(data["reading_score"]))
    writing_score = np.log(int(data["writing_score"]))

    predictionData = [gender,ethnicity,parental_level_of_education,lunch,test_preparation_course,reading_score,writing_score]
    result = loaded_model.predict([predictionData])
    if result[0]==1:
        result = "will"
    else:
        result = "will not"

    document.querySelector(".prediction").hidden = False
    document.querySelector(".result").innerText = result
    
    return result