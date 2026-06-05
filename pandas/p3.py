import pandas as pd
df = pd.read_csv("students.csv")
print(df)

print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.columns)
print(df["Name"])
print(df[["Name","Age"]])
print(df.iloc[1])
df["Salary"]= [30000,40000,50000]
print(df)
df.drop("Salary",axis=1,inplace=True)
print(df)
print(df[df["Age"]>20])
df.sort_values("Age",ascending=False,inplace=True)
print(df)