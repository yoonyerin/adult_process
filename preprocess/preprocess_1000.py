import pandas as pd

data=pd.read_csv("/home/yerinyoon/cubigate/Cubigate_ai_engine/dp/data/adult/preprocess/private_16280.csv")
up=data[data["income"]=="<=50K"].iloc[:500]
down=data[data["income"]==">50K"].iloc[:500]
df=pd.concat([up, down], axis=0)
print(df.shape)
df.to_csv("/home/yerinyoon/cubigate/Cubigate_ai_engine/dp/data/adult/preprocess/preprocess_1000.csv", index=False)