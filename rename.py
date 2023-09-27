import os
from datetime import datetime

# get current date and time
current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
# print("Current date & time : ", current_datetime)

path = os.chdir("C:\\Users\\user\\OneDrive\\Desktop\\IFPC_PARAM_FILES_SAMPLES_1")
current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

i = 0

for file in os.listdir(path):
    new_file_name = f"IPFS {i} {current_datetime}.prm"
    os.rename(file, new_file_name)
    i+=1
    
    