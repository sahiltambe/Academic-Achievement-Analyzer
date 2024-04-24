import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

# Any input data will be passed to this class
# It will read the data from the source
# It will split the data into train and test
# It will save the data into the artifact folder
@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    # It will read the data from the source
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            # It will read the data from the source here we have dataset in respective path. we can collect data from various source
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info('Read the dataset as dataframe')

            # It will make directory to save the data
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            
            # It will save the data into the artifact folder
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            # It will split the data into train and test
            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            logging.info("Train test split completed")

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            logging.info("Ingestion of the data is completed")

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
                # It will return the path of train and test data
            )
        except Exception as e:
            raise CustomException(e,sys) # It will raise the exception
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data, test_data=obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr,test_arr,_ = data_transformation.initiate_data_transformation(train_data,test_data)

    modeltrainer = ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr, test_arr,_))