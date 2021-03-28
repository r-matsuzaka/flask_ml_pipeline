import pickle

import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

# Read data
df = pd.read_csv("data/50_Startups.csv")

# Prepare feature and label
df = pd.get_dummies(df, columns=["State"])
df_X = df.drop("Profit", axis=1)
df_y = df["Profit"]

X = df_X.to_numpy()
y = df_y.to_numpy()

# Create Decision tree model
reg = DecisionTreeRegressor(max_depth=2)
reg.fit(X, y)

# Save model
with open("model.pickle", mode="wb") as fp:
    pickle.dump(reg, fp)
