# This file is part of the data feature engineering


import sys
from dataclasses import dataclass

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import CustomException
from src.logger import logging
import os

from src.utils import save_object

@dataclass
class DataTransformationConfig:
    # The name of the pkl file where the preprocessor object will be saved
    preprocessor_obj_file_path=os.path.join('artifacts',"proprocessor.pkl") # pkl file  path

class DataTransformation:
    '''
    The __init__ method is a special method in Python classes that is automatically called when an instance of the class is created. In this case, when a new instance of the DataTransformation class is created, it initializes an attribute called data_transformation_config with a value of a DataTransformationConfig object.

    The DataTransformationConfig class is a simple data class that has a single attribute, preprocessor_obj_file_path, which is a string representing the path where the preprocessor object will be saved as a pickle file. The __init__ method of the DataTransformationConfig class simply assigns a default value to the preprocessor_obj_file_path attribute.

    In the context of the DataTransformation class, the data_transformation_config attribute is used to store the configuration for saving the preprocessor object. This configuration is then used in the get_data_transformer_object and initiate_data_transformation methods of the DataTransformation class.
    '''
    def __init__(self):
        # 
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
        This function si responsible for data trnasformation
        '''
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]
            
            # Create a list of column names that will be used in the pipeline
            num_pipeline= Pipeline(
                steps=[
                ("imputer",SimpleImputer(strategy="median")), # Fill missing values with the median of the column
                ("scaler",StandardScaler()) # Standardize the data
                ]
            )   
            # Create a pipeline for categorical columns
            cat_pipeline=Pipeline(
                steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")), # Fill missing values with the most frequent value in the column ie the mode
                ("one_hot_encoder",OneHotEncoder()), # Encode the categorical variables into one-hot vectors
                ("scaler",StandardScaler(with_mean=False)) # Standardize the data
                ]
            )
            
            logging.info(f"Numerical columns: {numerical_columns}")
            logging.info(f"Categorical columns: {categorical_columns}")

            preprocessor=ColumnTransformer(
                [
                ("num_pipeline",num_pipeline,numerical_columns), # pipeline name , what pipeline is used, columns are for the numerical columns
                ("cat_pipelines",cat_pipeline,categorical_columns) # pipeline name , what pipeline is used, columns are for the categorical columns
                ]
            )

            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):
        '''
        This function is responsible for data transformation techniques. It will transform the training data into the training data and testing data
        '''
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")

            preprocessing_obj=self.get_data_transformer_object() # get preprocessing object from preprocessor=ColumnTransformer object

            target_column_name="math_score" # output column name
            numerical_columns = ["writing_score", "reading_score"]

            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

            save_object(
                # Save preprocessing object to file with preprocessing parameters and parameters values
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj # preprocessing object
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        except Exception as e:
            raise CustomException(e,sys)