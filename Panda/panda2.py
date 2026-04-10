import pandas as pd

df = pd.read_csv('dataset.csv')
print(df.to_string())
print(f"After Cleaning the empty data : ${df.dropna()}")
read = pd.read_csv('dataset3.csv')

print("Working with dataset3 : ")
print(f"Relationship between datas : ${read.corr()} ")
