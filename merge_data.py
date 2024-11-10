import pandas as pd
import glob
from tqdm import tqdm


paths = [ r"D:\UET\AI\DATA_SV\Precipitation\AWS.csv",
         r"D:\UET\AI\DATA_SV\ERA5\CAPE.csv",
         r"D:\UET\AI\DATA_SV\ERA5\CIN.csv",
         r"D:\UET\AI\DATA_SV\ERA5\EWSS.csv",
         r"D:\UET\AI\DATA_SV\ERA5\IE.csv",
         r"D:\UET\AI\DATA_SV\ERA5\ISOR.csv",
         r"D:\UET\AI\DATA_SV\ERA5\KX.csv",
         r"D:\UET\AI\DATA_SV\ERA5\PEV.csv",
         r"D:\UET\AI\DATA_SV\ERA5\R250.csv",
         r"D:\UET\AI\DATA_SV\ERA5\R500.csv",
         r"D:\UET\AI\DATA_SV\ERA5\R850.csv",
         r"D:\UET\AI\DATA_SV\ERA5\SLHF.csv",
         r"D:\UET\AI\DATA_SV\ERA5\SLOR.csv",
         r"D:\UET\AI\DATA_SV\ERA5\SSHF.csv",
         r"D:\UET\AI\DATA_SV\ERA5\TCLW.csv",
         r"D:\UET\AI\DATA_SV\ERA5\TCW.csv",
         r"D:\UET\AI\DATA_SV\ERA5\TCWV.csv",
         r"D:\UET\AI\DATA_SV\ERA5\U250.csv",
         r"D:\UET\AI\DATA_SV\ERA5\U850.csv",
         r"D:\UET\AI\DATA_SV\ERA5\V250.csv",
         r"D:\UET\AI\DATA_SV\ERA5\V850.csv",
]

merged_df = pd.read_csv(r"D:\UET\AI\DATA_SV\Precipitation\AWS.csv") 

for i, file in tqdm(enumerate(paths[1:], start=1)):
    df = pd.read_csv(file)

    suffix ="ERA5_" + (str(file)[:-4]).split('/')[-1]

    merged_df = pd.merge(merged_df, df, on=["lat", "lon", "time"], how="inner", suffixes=('', suffix))


merged_df.to_csv(r"D:\UET\AI\DATA_SV\MERGE_DATA.csv", index=False)

