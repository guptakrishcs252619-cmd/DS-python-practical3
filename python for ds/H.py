import pandas as pd

df = pd.read_csv("employee_salary.csv.csv")

print("Number of Employees in Each Department:")
print(df.groupby("Department")["Name"].count())

print("\nAverage Salary by Department:")
print(df.groupby("Department")["Salary"].mean())

print("\nMaximum Salary by Department:")
print(df.groupby("Department")["Salary"].max())

print("\nAverage Experience by Department:")
print(df.groupby("Department")["Experience"].mean())
