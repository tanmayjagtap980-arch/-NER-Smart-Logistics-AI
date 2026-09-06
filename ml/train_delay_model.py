import os
import joblib
import numpy as np

from sklearn.ensemble import RandomForestRegressor


X = np.array([
    [100, 10, 20, 80, 10, 10],
    [200, 20, 30, 75, 20, 15],
    [300, 40, 50, 65, 40, 30],
    [400, 60, 70, 50, 60, 60],
    [500, 80, 80, 40, 80, 75],
    [150, 30, 40, 70, 25, 20],
    [250, 50, 60, 60, 45, 40],
    [350, 70, 75, 55, 65, 60],
    [450, 90, 90, 45, 85, 80]
])


y = np.array([
    10,
    18,
    35,
    60,
    100,
    22,
    45,
    70,
    120
])


model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)


os.makedirs(
    "ml/models",
    exist_ok=True
)


joblib.dump(
    model,
    "ml/models/delay_model.pkl"
)


print("Delay model trained successfully.")