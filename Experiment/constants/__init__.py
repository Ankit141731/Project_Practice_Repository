import os, sys 
from datetime import datetime
 

def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%d-%m-%H-%M-%S')}"

CURRENT_TIME_STAMP = get_current_time_stamp()

ROOT_DIR_KEY = os.getcwd()
DATA_DIR = "Data"
DATA_DIR_KEY = "finalTrain.csv"
 
# DATA INGESTION
ARTIFACT_DIR_KEY = "Artifact"

DATA_INGESTION_KEY = "data_ingestion"
DATA_INGESTION_RAW_DIR = "raw_data_dir"
INGESTED_DIR_KEY = "ingested_dir"
RAW_DATA_DIR_KEY = "raw.csv"
TRAIN_DATA_DIR_KEY = "train.csv"
TEST_DATA_DIR_KEY = "test.csv"

# DATA TRANSFORMATION

DATA_TRANSFROM_ARTIFACT = "data_transformation"
DATA_PROCESSED_DIR = "Processed"
DATA_TRANSFORMATION_KEY = "Processor.pkl"
DATA_TRANSFORM_DIR = "tranformed_Data"
TRANSFORM_TRAIN_KEY = "train.csv"
TRANSFORM_TEST_KEY = "test.csv"




    