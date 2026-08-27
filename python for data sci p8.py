import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

print(tips.head())

sns.scatterplot(x="total_bill", y="tip", data=tips)

plt.title(" krish 085 Restaurant Bill vs Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")

plt.show()
print("krish 085")
