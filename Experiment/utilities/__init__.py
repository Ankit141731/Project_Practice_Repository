from Experiment.exception import CustomException
from Experiment.logger import logging
import pickle
import sys , os

def save_obj(file_path , obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path , exist_ok = True)

        with open(file_path , "w") as file_obj:
            pickle.dump(file_obj)
    except Exception as e:
        raise CustomException(e , sys)