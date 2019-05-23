import pandas as pd
import matplotlib.pyplot as plt

test = pd.read_csv("input/test.csv")
test_shape = test.shape
print(test_shape)

train = pd.read_csv("input/train.csv")
train_shape = train.shape
# print(train.head(10))

sex_pivot = train.pivot_table(index="Sex", values="Survived")

sex_pivot.plot.bar()
plt.show()
