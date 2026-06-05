import pandas as pd

df1 = pd.DataFrame({
    "ID":[1,2,3],
    "Name":["John","David","Tom"]
})

df2 = pd.DataFrame({
    "ID":[1,2,3],
    "Salary":[30000,40000,50000]
})

result = pd.merge(df1, df2, on="ID")

print(result)