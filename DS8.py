import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

x_scatter = [1, 2, 3, 4, 5]
y_scatter = [5, 3, 4, 2, 6]

# -------------------------
# Line Plot (Figure 1)
# -------------------------
plt.figure(figsize=(8,5))
plt.plot(x, y,
         color="blue",
         marker="o",
         label="Line Plot")

plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()

# -------------------------
# Scatter Plot (Figure 2)
# -------------------------
plt.figure(figsize=(8,5))
plt.scatter(x_scatter, y_scatter,
            color="red",
            s=80,
            label="Scatter Plot")

plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()
