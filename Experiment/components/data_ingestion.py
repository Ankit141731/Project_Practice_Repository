from Experiment.constants import *
from Experiment.configs.configuration import *
import os , sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from Experiment.logger import logging
from Experiment.exception import CustomException
from Experiment.components.data_tranformation import DataTranformation

@dataclass
class DataIngestionConfig:
    train_data_path:str = TRAIN_FILE_PATH
    test_data_path :str = TEST_FILE_PATH
    raw_data_path :str = RAW_FILE_PATH

class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            df = pd.read_csv(DATASET_PATH)

            # df = pd.read_csv(os.path.join("cwd\finalTrain.csv"))

            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_path) , exist_ok = True)
             
            df.to_csv(self.data_ingestion_config.raw_data_path , index = False)

            train_set , test_set = train_test_split(df , test_size = 0.2 , random_state = 42)

            os.makedirs(os.path.dirname(self.data_ingestion_config.train_data_path) , exist_ok = True)
            train_set.to_csv(self.data_ingestion_config.train_data_path , header = True)

            os.makedirs(os.path.dirname(self.data_ingestion_config.test_data_path) , exist_ok = True)
            test_set.to_csv(self.data_ingestion_config.test_data_path , header = True)

            return  (
                self.data_ingestion_config.train_data_path ,
                self.data_ingestion_config.test_data_path , 
            )

        except Exception as e:
            raise CustomException(e , sys)

    
if __name__ == "__main__" :
    obj = DataIngestion() 
    train_data , test_data = obj.initiate_data_ingestion()
    data_transformation = DataTranformation()
    train_arr , test_arr = data_transformation.initiate_data_transformation(train_data , test_data)
