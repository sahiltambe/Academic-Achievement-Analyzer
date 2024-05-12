import pandas as pd
import numpy as np
from pyscript import Element
from js import document, window
import pickle
import pyodide.http
import io
import asyncio
import os
import joblib


# Disable warnings by pyscript appearing in the browser.
import warnings
warnings.filterwarnings("ignore")

# loading pkl file from local filesystem
# async def load_model():
#     model_path = "model.pkl"
#     if os.path.exists(model_path):
#         with open(model_path, "rb") as f:
#             loaded_model = pickle.load(f)
#             return loaded_model
#     else:
#         print("Model file not found locally.")
#         return None

# # Load the model asynchronously when the script runs
# async def load_model():
#     url = "model.pkl"
#     print("Attempting to load model from:", url)
#     response = await pyodide.http.pyfetch(url)
#     if response.status == 200:
#         content = await response.bytes()
#         model = pickle.loads(content)
#         print("Model loaded successfully")
#         return model
#     else:
#         print("Failed to load model, status code:", response.status)
#         return None

with open("model.pkl", "rb") as f:
    loaded_model = pickle.load(f)

# Load the model asynchronously when the script runs
# loaded_model = None

async def init_model():
    # loaded_model = await load_model()
    if loaded_model is not None:
        print("Model loaded successfully")
    else:
        print("Failed to load model")

#############################################################################


def get_predictions():
    if loaded_model is None:
        document.querySelector(".result").innerText = "Model not loaded."
        return
    else:
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

        if data["gender"]=="male":
            gender = 1
        elif data["gender"]=="female":
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

        try:
            reading_score = np.log(int(data["reading_score"]))
            writing_score = np.log(int(data["writing_score"]))
        except ValueError:
            document.querySelector(".result").innerText = "Invalid input for scores. Please enter numeric values."
            return

    

        predictionData = [gender,ethnicity,parental_level_of_education,lunch,test_preparation_course,reading_score,writing_score]
        # result = loaded_model.predict([predictionData])

        # predicted_math_score = loaded_model.predict(predictionData)
        if loaded_model is not None:
            # Make predictions using the loaded model
            result = loaded_model.predict(predictionData)
            document.querySelector(".prediction").hidden = False
            document.querySelector(".result").innerText = result
        else:
            document.querySelector(".result").innerText = "Model not loaded... Unable to make predictions."

        # document.querySelector(".prediction").hidden = False
        # document.querySelector(".result").innerText = result
        
        return result

# Ensure that init_model() is called when the script runs
init_model()