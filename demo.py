import numpy as np
import pandas as pd

data = {'date' : pd.to_datetime(['01/01/2022','02/01/2022','03/01/2022','04/01/2022','05/01/2022','06/01/2022','06/01/2022'],format='%d/%m/%Y'),
        'volumes_max' : [120.0, 123.0, 102.0, None, 111.0, None, 124.0],
        'volumes': [120.0, 130.0, 102.0, None, 111.0	,None , 124.0],
        'temperature' : [22.0, 23.0, 21.0, 36.0, None, 31.0, 25.0]}
df = pd.DataFrame(data)
df

df.index = ['Thứ 2','Thứ 3','Thứ 4','Thứ 5','Thứ 6','Thứ 7','Chủ nhật']
df

df.describe()
