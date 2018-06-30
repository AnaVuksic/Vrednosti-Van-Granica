import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

iris = pd.read_csv("iris.csv") 

#To view Iris data below:

print iris.head()

iris.plot(kind="scatter", x="sepal_length", y="sepal_width")
plt.show()

sns.boxplot(x="species", y="petal_length", data=iris )
plt.show()

ax= sns.boxplot(x="species", y="petal_length", data=iris)
ax= sns.stripplot(x="species", y="petal_length", data=iris, jitter=True, edgecolor="gray")
plt.show()

sns.violinplot(x="species", y="petal_length", data=iris, size=6)
plt.show()

df = sns.load_dataset('iris')
 
# Method 1: on the same Axis
sns.distplot( df["sepal_length"] , color="skyblue", label="Sepal Length")
sns.distplot( df["sepal_width"] , color="red", label="Sepal Width")

 
plt.show()

f, axes = plt.subplots(2, 2, figsize=(7, 7), sharex=True)
sns.distplot( df["sepal_length"] , color="skyblue", ax=axes[0, 0])
sns.distplot( df["sepal_width"] , color="olive", ax=axes[0, 1])
sns.distplot( df["petal_length"] , color="gold", ax=axes[1, 0])
sns.distplot( df["petal_width"] , color="teal", ax=axes[1, 1])

plt.show()

