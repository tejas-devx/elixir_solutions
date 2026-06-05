import pandas as pd

data = {
    "Department":["IT","IT","HR","HR"],
    "Month":["Jan","Feb","Jan","Feb"],
    "Salary":[1000,2000,1500,2500]
}

df = pd.DataFrame(data)

table = pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    columns="Month"
)

print(table)

df = pd.DataFrame({
    "Date":["2025-01-01","2025-02-01"]
})

df["Date"] = pd.to_datetime(df["Date"])

df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day

df.to_csv("output.csv", index=False)