import os
import sys
import logging
from datetime import datetime

LOG_DIR = "logs"
LOG_DIR = os.path.join(os.getcwd() , LOG_DIR)

os.makedirs(LOG_DIR , exist_ok = True)

CURRENT_TIME_STAMP = f"{datetime.now().strftime("%d-%m-%y-%H-%M-%S")}"
new_log = f"log_{CURRENT_TIME_STAMP}.log"

log_file_path = os.path.join(LOG_DIR , new_log)

logging.basicConfig(

    filename = log_file_path , 
    filemode = "w" , 
    format = "%(asctime)s-%(name)s-%(levelname)s-%(message)s" ,
    level = logging.INFO

) 




