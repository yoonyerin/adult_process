    
import random
import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder
tabular_data="/home/yerin/yerin_data/azoo/Cubigate_ai_engine/dp/data/adult.csv"
filepath=os.listdir("/home/yerin/yerin_data/azoo/Cubigate_ai_engine/dp/data/adult_process/preprocess/much/private")
result_folder=["/home/yerin/yerin_data/azoo/Cubigate_ai_engine/dp/data/adult_process/text_adult/less/private", "/home/yerin/yerin_data/azoo/Cubigate_ai_engine/dp/data/adult_process/text_adult/much/private"]


origin=pd.read_csv(tabular_data)
less=origin[origin["income"]=="<=50K"]
much=origin[origin["income"]==">50K"]
categorical=origin.dtypes.index[origin.dtypes.values==object]
num_origin=origin.drop(categorical, axis=1)
cat_origin=origin[categorical]
columns=""


column=list(num_origin.columns)+list(categorical)


for num, data in enumerate([less, much]):
    for idx in range(100):
        input_query=""
        if idx==0:
            _mode="w"
        else:
            _mode="a"
        idx_data=[]
        imp_data=[]
        for col in column:
            
            print(col)
            print(idx)
            print(data.shape)
        
            value=data.iloc[idx][col]


            text=f"{col} is {value}"
            if col=="income":
                pass
            else:
                idx_data.append(text)
            # if column_list[col] in categorical_column:
            #     imp_data.append(text)
            # else:
            #     idx_data.append(text)
            
        # random.shuffle(idx_data)
        idx_text=",".join(idx_data)
        # input_query="[INST] "
        # input_query+="[/INST]"
        print(idx_text)

        print(idx_text)
        print(num)
        
        with open(os.path.join(result_folder[num], filepath[idx]), mode=_mode) as _file:
            _file.write(idx_text)


