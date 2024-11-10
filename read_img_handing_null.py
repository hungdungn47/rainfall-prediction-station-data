import collections
import os
import pandas as pd
from tqdm import tqdm
import math
from datetime import datetime
import os
import tifffile as tiff
import numpy as np
import gspread_dataframe

from multiprocessing import Pool

def read_data(path):
    img = tiff.imread(path)
    # img = np.nan_to_num(img)
    return img
def export_time(file_name):
    time = file_name.split("_")[-1]
    year = time[:4]
    month = time[4:6]
    day = time[6:8]
    hour = time[8:10]
    return year,month,day,hour
def extract(path):
    data_count = collections.defaultdict(lambda: {"null": 0, "not_null": 0})
    data = collections.defaultdict(list) 
    for root,_,files in tqdm(os.walk(path)):
        # print(files)
        for file_name in files: 
            #read img
            img = read_data(os.path.join(root,file_name))
            for lat in range(int(img.shape[0])):
                for lon in range(int(img.shape[1])):
                    val = img[lat, lon]
                    if np.isnan(val) or np.isneginf(val):
                        data_count[(lat, lon)]["null"] += 1
                    else:
                        data_count[(lat, lon)]["not_null"] += 1
    for root,_,files in tqdm(os.walk(path)):
        # print(files)
        for file_name in files:  
            year,month,day,hour = export_time(file_name)
            time = f"{year}-{month}-{day} {hour}:00:00"  

            img = read_data(os.path.join(root,file_name))                
            
            for lat in range(int(img.shape[0])):
                for lon in range(int(img.shape[1])):
                    if (data_count[(lat, lon)]["not_null"] > 0):
                        data['lat'].append(lat)
                        data['lon'].append(lon)
                        data['time'].append(time)
                        if np.isneginf(img[lat,lon]) or np.isnan(img[lat,lon]):
                            data['AWS'].append(0)
                        else: data['AWS'].append(img[lat][lon])
            
    df = pd.DataFrame(data)
    df = df.sort_values(by='time')
    out_dir = path.split("/")[-1]
    df.to_csv(f"{out_dir}.csv",index = False)
extract(r"D:\UET\AI\DATA_SV\Precipitation\AWS")