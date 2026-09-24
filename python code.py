import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("krish_chaat_corner_300_records.csv")

print("KRISH CHAAT CORNER")
print("DATA SCIENCE MINI PROJECT")

print("\nFIRST 5 RECORDS")
print(df.head())

print("\nLAST 5 RECORDS")
print(df.tail())

print("\nNUMBER OF ROWS AND COLUMNS")
print(df.shape)

print("\nCOLUMN NAMES")
print(df.columns.tolist())

print("\nDATA TYPES")
print(df.dtypes)

print("\nSTATISTICAL INFORMATION")
print(df.describe())

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nDUPLICATE RECORDS")
print(df.duplicated().sum())

df = df.drop_duplicates()

df.columns = df.columns.str.strip()

df["Total"] = pd.to_numeric(df["Total"], errors="coerce")

df = df.dropna(subset=["Total"])

print("\nDATA AFTER CLEANING")
print(df.head())

total_orders = len(df)
total_customers = df["Name"].nunique()
total_revenue = np.sum(df["Total"])
average_order = np.mean(df["Total"])
median_order = np.median(df["Total"])
maximum_order = np.max(df["Total"])
minimum_order = np.min(df["Total"])
standard_deviation = np.std(df["Total"])

print("\nDATA ANALYSIS")

print("Total Orders:", total_orders)
print("Total Customers:", total_customers)
print("Total Revenue: ₹", total_revenue)
print("Average Order: ₹", average_order)
print("Median Order: ₹", median_order)
print("Maximum Order: ₹", maximum_order)
print("Minimum Order: ₹", minimum_order)
print("Standard Deviation: ₹", standard_deviation)

def get_items(order):
    items = []

    for part in str(order).split(","):
        item = part.strip()

        if " x" in item:
            item = item.rsplit(" x", 1)[0]

        items.append(item)

    return items

item_data = []

for _, row in df.iterrows():

    items = get_items(row["Order"])

    for item in items:

        item_data.append({
            "No.": row["No."],
            "Name": row["Name"],
            "Item": item,
            "Total": row["Total"]
        })

item_df = pd.DataFrame(item_data)

item_counts = item_df["Item"].value_counts()

print("\nITEM-WISE ORDERS")

print(item_counts)

print("\nMOST ORDERED ITEM")

print(item_counts.idxmax())

print("\nLEAST ORDERED ITEM")

print(item_counts.idxmin())

print("\nNUMBER OF DIFFERENT ITEMS")

print(item_df["Item"].nunique())

customer_orders = df["Name"].value_counts()

print("\nTOP CUSTOMERS")

print(customer_orders.head(10))

customer_sales = df.groupby("Name")["Total"].sum()

print("\nCUSTOMER-WISE SALES")

print(customer_sales.sort_values(ascending=False).head(10))

highest_customer = customer_sales.idxmax()

highest_customer_value = customer_sales.max()

print("\nHIGHEST SPENDING CUSTOMER")

print(highest_customer)

print("Amount: ₹", highest_customer_value)

print("\nSORTED ORDERS")

print(df.sort_values("Total", ascending=False).head(10))

plt.figure(figsize=(10, 6))

item_counts.plot(kind="bar")

plt.title("Item-wise Orders")
plt.xlabel("Food Item")
plt.ylabel("Number of Orders")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()

plt.figure(figsize=(8, 8))

plt.pie(
    item_counts.values,
    labels=item_counts.index,
    autopct="%1.1f%%"
)

plt.title("Orders by Food Item")

plt.show()

plt.figure(figsize=(10, 6))

plt.hist(
    df["Total"],
    bins=10
)

plt.title("Order Total Distribution")
plt.xlabel("Order Total")
plt.ylabel("Frequency")

plt.show()

plt.figure(figsize=(10, 5))

sns.boxplot(
    x=df["Total"]
)

plt.title("Order Total Box Plot")
plt.xlabel("Order Total")

plt.show()

sales = df.groupby("No.")["Total"].sum()

plt.figure(figsize=(10, 6))

plt.plot(
    sales.index,
    sales.values,
    marker="o",
    markersize=3
)

plt.title("Order-wise Revenue")
plt.xlabel("Order Number")
plt.ylabel("Revenue")

plt.grid(True)

plt.tight_layout()

plt.show()

most_ordered_item = item_counts.idxmax()

print("\nKEY FINDINGS")

print("1. The dataset contains", total_orders, "orders.")

print("2. There are", total_customers, "different customers.")

print("3. Total revenue is ₹", total_revenue)

print("4. Average order value is ₹", round(average_order, 2))

print("5. The highest order value is ₹", maximum_order)

print("6. The lowest order value is ₹", minimum_order)

print("7. The most ordered item is", most_ordered_item)

print("8. The highest spending customer is", highest_customer)

print("9. Highest customer spending is ₹", highest_customer_value)
