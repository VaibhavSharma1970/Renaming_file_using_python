import os

directory = "C:\\Users\\user\\OneDrive\\Desktop\\Informatica param automation\\Input\\MDM_INBOUND_PROD\\ECM2"

variable_name = "$$IPC_FILE_NAME_PREFIX"
new_value = "CUSTOMER_LGLSFDCGLI_DELTA_"

# Define the name and initial value of the new variable
variable_name2 = "$$IPC_FILE_NAME"
new_value_2 = "CUSTOMER_LGLSFDCGLI_DELTA_DDMMYYYY.csv"
variable_name_3 = "$$IPC_REJ_FILE_NAME"
new_value_3 = "CUSTOMER_LGLSFDCGLI_DDMMYYYY_REJ.csv"

# file_path =  "C:\\Users\\user\\OneDrive\\Desktop\\Renaming_file_using_python\\PRM_ECM2_FACT_Load.prm"

for filename in os.listdir(directory):
    if filename.endswith(".prm"):
        file_path = os.path.join(directory, filename)

        with open(file_path, 'r') as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            if line.startswith(variable_name):
                lines[i] = new_value
                lines[i] = f"{variable_name} = {new_value}\n"

        new_line = f"{variable_name2} = {new_value_2}"
        lines.append(new_line)
        new_line2 = f"\n{variable_name_3} = {new_value_3}"
        lines.append(new_line2)

        with open(file_path, 'w') as file:
            file.writelines(lines)

        file.close()
