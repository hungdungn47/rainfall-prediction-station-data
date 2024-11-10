import collections
import os
import pandas as pd
from tqdm import tqdm
import math
from datetime import datetime
import os
import tifffile as tiff
import numpy as np

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

# base_name = r"D:\uet_doc\AI\DATA_SV\Precipitation\Radar\year\month\day\file_name"
def extract(path):
    data = collections.defaultdict(list)
    for root,_,files in tqdm(os.walk(path)):
        for file_name in files:
            year,month,day,hour = export_time(file_name)
            time = f"{year}-{month}-{day} {hour}:00:00"
            #read img
            img = read_data(os.path.join(root,file_name))
            # print(img.shape)
            for lat in range(int(img.shape[0])):
                for lon in range(int(img.shape[1])):
                    # print(img[lat,lon])
                    if np.isneginf(img[lat,lon]) or np.isnan(img[lat,lon]):
                        continue
                    data['lat'].append(lat)
                    data['lon'].append(lon)
                    data['time'].append(time)
                    data['radar'].append(img[lat][lon])
    print("export to csv")
    df = pd.DataFrame(data)
    print("sorting ......")
    df = df.sort_values(by='time')
    print('exporting .......')
    out_dir = path.split("/")[-1]
    df.to_csv(f"{out_dir}.csv",index = False)

extract(r"D:\UET\AI\DATA_SV\ERA5\R500")  