

# Step 1: Load the dataset

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv('D:\\PROJECTS\\House Price Prediction System\\notebook_and_dataset\\csvdata.csv')

# Step 2: Handle Missing Values
# Example: Replace missing values with the mean of each column
df.fillna('null', inplace=True)

# Step 3: Handle Categorical Variables
# Example: One-hot encode categorical variables
# Assuming 'city' and 'location' are categorical variables
df = pd.get_dummies(df, columns=['City', 'Location'], drop_first=True)

# Step 4: Split the data into features and target variable
X = df.drop('Price', axis=1)  # Features
y = df['Price']               # Target variable

# Step 5: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 6: Feature Scaling (if necessary)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 7: Initialize the XGBoost model
model = XGBRegressor(
    n_estimators=1000,  # number of trees (boosting rounds)
    learning_rate=0.05,  # step size shrinkage to prevent overfitting
    max_depth=5,  # maximum depth of each tree
    subsample=0.7,  # fraction of samples used in each boosting round
    colsample_bytree=0.7,  # fraction of features used in each boosting round
    random_state=42
)

# Step 8: Train the model
model.fit(X_train_scaled, y_train, eval_set=[(X_test_scaled, y_test)], verbose=False)

# Step 9: Evaluate the model
y_pred = model.predict(X_test_scaled)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Absolute Error (MAE): {mae:.2f}')
print(f'Mean Squared Error (MSE): {mse:.2f}')
print(f'R-squared (R^2): {r2:.2f}')
