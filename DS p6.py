import matplotlib.pyplot as plt
import numpy as np

# 1. Line Plot Basics
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.figure(figsize=(6,4))
plt.plot(x, y)
plt.title(" krish 085 Simple Line Plot")
plt.xlabel("Numbers")
plt.ylabel("Doubles")
plt.grid(True)
plt.show()

# 2. Customize a Line Plot
plt.figure(figsize=(6,4))
plt.plot(x, y, color="red", linestyle="--", marker="o")
plt.title("Customized Line Plot")
plt.xlabel("Numbers")
plt.ylabel("Doubles")
plt.grid(True)
plt.show()

# 3. Bar Chart
categories = ["vada pav ", "pani puri",
              "bhel", "samosa"]
scores = [65, 70, 74, 60]

plt.figure(figsize=(8,5))
plt.bar(categories, scores, color="skyblue")
plt.title("MENU")
plt.xlabel("Subjects")
plt.ylabel("Scores")
plt.show()

# 4. Horizontal Bar Chart
plt.figure(figsize=(8,5))
plt.barh(categories, scores, color="orange")
plt.title(" krish 085 Student Scores (Horizontal Bar Chart)")
plt.xlabel("Scores")
plt.ylabel("Subjects")
plt.show()

# 5. Pie Chart
explode = (0, 0, 0, 0.2)

plt.figure(figsize=(6,6))
plt.pie(scores,
        labels=categories,
        autopct="%1.1f%%",
        explode=explode,
        shadow=True,
        startangle=90)
plt.title("MENU Scores Pie Chart")
plt.show()

# 6. Scatter Plot
x_scatter = [5, 7, 8, 7, 6, 9, 5]
y_scatter = [99, 86, 87, 88, 100, 86, 103]

plt.figure(figsize=(6,5))
plt.scatter(x_scatter, y_scatter,
            color="green",
            s=100)
plt.title("Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.grid(True)
plt.show()

# 7. Histogram
data = np.random.normal(0, 1, 100)

plt.figure(figsize=(6,5))
plt.hist(data, bins=20)
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# 8. Two Plots in One Figure
plt.figure(figsize=(8,5))

plt.plot(x, y,
         color="blue",
         marker="o",
         label="Line Plot")

plt.scatter(x_scatter, y_scatter,
            color="red",
            s=80,
            label="Scatter Plot")

plt.title("Two Plots in One Figure")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()

# 9. Four Subplots 
fig, axs = plt.subplots(2, 2, figsize=(10,8))

# Top Left - Line Plot
axs[0,0].plot(x, y, color="blue", marker="o")
axs[0,0].set_title("Line Plot")

# Top Right 
axs[0,1].bar(categories, scores)
axs[0,1].set_title(" krish 085 Bar Chart")
axs[0,1].tick_params(axis='x', rotation=20)

# Bottom Left - Scatter Plot
axs[1,0].scatter(x_scatter, y_scatter,
                 color="green",
                 s=70)
axs[1,0].set_title("Scatter Plot")

# Bottom Right - Histogram
axs[1,1].hist(data, bins=20)
axs[1,1].set_title("Histogram")

plt.tight_layout()
plt.show()

# 10. Sales Comparison (2023 vs 2024)
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

sales_2023 = [150, 200, 250, 300, 280, 350]
sales_2024 = [180, 220, 270, 320, 300, 400]

plt.figure(figsize=(8,5))

# 2023 Line
plt.plot(months,
         sales_2023,
         color="blue",
         linestyle="--",
         marker="o",
         linewidth=2,
         label="Sales 2023")

# 2024 Line
plt.plot(months,
         sales_2024,
         color="green",
         linestyle="-",
         marker="s",
         linewidth=2,
         label="Sales 2024")

plt.title(" krish 085 Monthly Sales Comparison (2023 vs 2024)")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()

# Highlight highest sales month of 2024
highest_sale = max(sales_2024)
highest_index = sales_2024.index(highest_sale)

plt.annotate(
    "Highest Sales",
    xy=(months[highest_index], highest_sale),
    xytext=(months[highest_index], highest_sale + 25),
    arrowprops=dict(facecolor="black", shrink=0.05)
)

plt.grid(True)

# Save the figure
plt.savefig("sales_comparison.png")

plt.show()

print("Program Executed Successfully!")
print("sales_comparison.png has been saved in the current folder.")
