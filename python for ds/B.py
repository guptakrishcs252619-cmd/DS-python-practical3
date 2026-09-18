import pandas as pd

df = pd.read_csv("movie_ratings.csv.csv")

print("Number of Movies in Each Genre:")
print(df.groupby("Genre")["Movie"].count())

print("\nAverage Rating by Genre:")
print(df.groupby("Genre")["Rating"].mean())

print("\nMaximum Rating by Genre:")
print(df.groupby("Genre")["Rating"].max())

print("\nAverage Votes by Genre:")
print(df.groupby("Genre")["Votes"].mean())

print("\nNumber of Movies by Language:")
print(df.groupby("Language")["Movie"].count())
