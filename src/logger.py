import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # text file in datetime
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE) # path for a log file along with the current working directories
os.makedirs(logs_path,exist_ok=True) # make diretories for logpath

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE) # log file path 

# 
logging.basicConfig(
    filename=LOG_FILE_PATH, # give file path
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s", # then format with best practice
    level=logging.INFO, # for which level! this for info


)
