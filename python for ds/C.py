import pandas as pd

df = pd.read_csv("employee_salary.csv.csv")

print("Name and Salary:")
print(df[["Name", "Salary"]])

print("\nEmployees earning more than 50000:")
print(df[df["Salary"] > 50000])

print("\nEmployees with experience above 5 years:")
print(df[df["Experience"] > 5])

print("\nFemale Employees:")
print(df[df["Gender"] == "Female"])

print("\nIT Department Employees:")
print(df[df["Department"] == "IT"])

print("\nEmployees earning more than 50000 and experience above 5 years:")
print(df[(df["Salary"] > 50000) & (df["Experience"] > 5)])
