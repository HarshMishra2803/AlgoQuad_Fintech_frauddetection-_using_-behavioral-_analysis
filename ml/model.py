import pandas as pd # type: ignore

data = pd.read_csv("../data/creditcard.csv")
print(data.shape)