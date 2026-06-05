import pandas as pd 
data= {
    "Name":["John","David",None],
    "Age":[20,None,22]
    }
df=pd.DataFrame(data)
print(df.isnull())

df.fillna(0,inplace=True)
print(df)