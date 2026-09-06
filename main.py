import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load a classic dataset that ships with seaborn
iris = sns.load_dataset("iris")

print("Rows and columns:", iris.shape)
print()
print(iris.head())
print()
print(iris.groupby("species")["petal_length"].describe())

# Draw and save a figure
sns.scatterplot(data=iris, x="sepal_length", y="petal_length", hue="species")
plt.title("Sepal length against petal length")
plt.savefig("iris_scatter.png", dpi=150, bbox_inches="tight")
print("\nFigure saved as iris_scatter.png")