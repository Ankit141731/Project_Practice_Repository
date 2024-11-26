from Experiment.constants import *
import os , sys

ROOT_DIR = ROOT_DIR_KEY

DATASET_PATH = os.path.join(ROOT_DIR , DATA_DIR , DATA_DIR_KEY)

RAW_FILE_PATH = os.path.join(

                        ROOT_DIR_KEY ,
                        ARTIFACT_DIR_KEY ,
                        DATA_INGESTION_KEY,
                        CURRENT_TIME_STAMP ,
                        DATA_INGESTION_RAW_DIR ,
                        RAW_DATA_DIR_KEY
                        
                         )

TRAIN_FILE_PATH =  os.path.join(

                        ROOT_DIR_KEY ,
                        ARTIFACT_DIR_KEY ,
                        DATA_INGESTION_KEY,
                        CURRENT_TIME_STAMP ,
                        INGESTED_DIR_KEY ,
                        TRAIN_DATA_DIR_KEY 
                        
                              )

TEST_FILE_PATH =  os.path.join(

                        ROOT_DIR_KEY ,
                        ARTIFACT_DIR_KEY ,
                        DATA_INGESTION_KEY,
                        CURRENT_TIME_STAMP ,
                        INGESTED_DIR_KEY ,
                        TEST_DATA_DIR_KEY 
                        
                              )
 

# DATA TRANSFORMATION STEPS 

PREPROCESSING_OBJ_FILE_PATH = os.path.join(
    
                              ROOT_DIR,
                              ARTIFACT_DIR_KEY ,
                              DATA_TRANSFROM_ARTIFACT, 
                              DATA_PROCESSED_DIR , 
                              DATA_TRANSFORMATION_KEY
                                    
                                    )

TRANSFORM_TRAIN_FILE_PATH = os.path.join(
                              
                              ROOT_DIR , 
                              ARTIFACT_DIR_KEY , 
                              DATA_TRANSFROM_ARTIFACT , 
                              DATA_TRANSFORM_DIR,
                              TRANSFORM_TRAIN_KEY
    

                                        )

TRANSFORM_TEST_FILE_PATH = os.path.join(
                              
                              ROOT_DIR , 
                              ARTIFACT_DIR_KEY , 
                              DATA_TRANSFROM_ARTIFACT , 
                              DATA_TRANSFORM_DIR,
                              TRANSFORM_TEST_KEY
    
                                     )

FEATURE_ENGINEERING_OBJ_FILE_PATH = os.path.join(
    
                              ROOT_DIR,
                              ARTIFACT_DIR_KEY, 
                              DATA_TRANSFROM_ARTIFACT, 
                              DATA_PROCESSED_DIR,
                              "feature_Eng.pkl"

                                       )