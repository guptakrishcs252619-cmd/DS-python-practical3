import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer", "Tablet", "Speaker", "Webcam"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics", "Electronics", "Electronics", "Accessories", "Accessories"],
    "Sales": [110000, 8000, 12000, 48000, 36000, 75000, 15000, 18000]
}

df = pd.DataFrame(data)

plt.figure(figsize=(8, 5))
plt.bar(df["Product"], df["Sales"])
plt.xlabel("Product")
plt.ylabel("Sales")
plt.title("Product Sales")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8, 5))
plt.plot(df["Product"], df["Sales"], marker="o")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.title("Product Sales - Line Chart")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(df["Sales"], bins=5)
plt.xlabel("Sales")
plt.ylabel("Number of Products")
plt.title("Distribution of Sales")
plt.show()

category_count = df["Category"].value_counts()

plt.figure(figsize=(7, 7))
plt.pie(category_count, labels=category_count.index, autopct="%1.1f%%")
plt.title("Products by Category")
plt.show()
