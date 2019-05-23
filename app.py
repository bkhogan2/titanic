import pandas as pd

test = pd.read_csv("input/test.csv")
test_shape = test.shape
print(test_shape)

train = pd.read_csv("input/train.csv")
train_shape = train.shape
print(train.head(10))
