import pandas as pd

df = pd.read_csv("students.csv.csv")

print("Average Marks:", df["Marks"].mean())
print("Maximum Marks:", df["Marks"].max())
print("Minimum Marks:", df["Marks"].min())
print("Median Marks:", df["Marks"].median())
print("Standard Deviation:", df["Marks"].std())
print("Average Attendance:", df["Attendance"].mean())
print("Number of Students:", df["Name"].count())
print("Students scoring above 75:", (df["Marks"] > 75).sum())s
