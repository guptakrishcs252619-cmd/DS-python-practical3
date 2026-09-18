import pandas as pd

df = pd.read_csv("sales.csv.csv")

print("Sales in Ascending Order:")
print(df.sort_values("Sales"))

print("\nSales in Descending Order:")
print(df.sort_values("Sales", ascending=False))

print("\nQuantity in Descending Order:")
print(df.sort_values("Quantity", ascending=False))

print("\nTop 5 Orders:")
print(df.sort_values("Sales", ascending=False).head(5))

print("\nBottom 3 Orders:")
print(df.sort_values("Sales").head(3))
