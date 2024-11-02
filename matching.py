import pandas as pd
import os

df = pd.read_csv('hds-devices.csv')

printer_ids = df['PrinterID'].to_numpy()
print( tuple(printer_ids))
import os

pids_to_stms = dict.fromkeys(printer_ids, [])

for filename in os.listdir("SMA_Hackathon/"):
    if filename.endswith(".stm"): 
        with open("SMA_Hackathon/" + filename, 'r') as file:
            content = file.read()
            for p_id in printer_ids:
                if str(p_id) in content:
                    pids_to_stms[p_id].append(filename)

# with open('', 'r') as file:
#     # Read the file content
#     content = file.read()
#     # Check if the string is present in the file
#     if 'your_string' in content:
#         print('String found!')
#     else:
#         print('String not found.')
