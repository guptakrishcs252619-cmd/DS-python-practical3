import pandas as pd

data = {
    "Student_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
                   111, 112, 113, 114, 115, 116, 117, 118, 119, 120],

    "Name": ["Amit", "Sneha", "Rahul", "Priya", "Neha", "Rohan", "Pooja",
             "Karan", "Anjali", "Vikas", "Meena", "Arjun", "Simran",
             "Akash", "Kavita", "Manish", "Riya", "Raj", "Nisha", "Sachin"],

    "Gender": ["Male", "Female", "Male", "Female", "Female", "Male",
               "Female", "Male", "Female", "Male", "Female", "Male",
               "Female", "Male", "Female", "Male", "Female", "Male",
               "Female", "Male"],

    "Age": [19, 20, 19, 21, 20, 19, 21, 20, 19, 21,
            20, 19, 21, 20, 19, 21, 20, 19, 21, 20],

    "Course": ["BSc CS", "BSc CS", "BSc IT", "BSc CS", "BSc IT",
               "BSc CS", "BSc IT", "BSc CS", "BSc CS", "BSc IT",
               "BSc CS", "BSc IT", "BSc CS", "BSc IT", "BSc CS",
               "BSc IT", "BSc CS", "BSc IT", "BSc CS", "BSc IT"],

    "Marks": [78, 85, 67, 92, 88, 74, 81, 69, 95, 56,
              73, 64, 89, 71, 83, 49, 91, 58, 77, 86],

    "Attendance": [85, 92, 76, 95, 89, 81, 87, 72, 96, 68,
                   79, 74, 91, 82, 88, 65, 94, 70, 84, 90]
}

df = pd.DataFrame(data)

print("Complete Dataset:")
print(df)

print("\nFirst 5 Records:")
print(df.head())

print("\nLast 5 Records:")
print(df.tail())

print("\nShape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
df.info()

print("\nStatistical Information:")
print(df.describe())
