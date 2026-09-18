import pandas as pd


data = {
    "Name": ["Amit", "Sneha", "Rahul", "Priya", "Neha", "Rohan"],
    "Marks": [78, 85, None, 92, 88, None],
    "Attendance": [85, None, 78, 92, None, 80]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)


print("\nMissing Values:")
print(df.isnull())

print("\nCount of Missing Values:")
print(df.isnull().sum())

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())

print("\nCleaned Dataset:")
print(df)
