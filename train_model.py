import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

# Load dataset
data = pd.read_csv("superstore.csv")

# Select features
X = data[["Quantity", "Discount", "Profit"]]

# Target
y = data["Sales"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("=" * 50)
print("AI-Powered Business Intelligence")
print("=" * 50)

print("\nModel Trained Successfully!")

print("\nR2 Score :", round(r2_score(y_test, y_pred), 2))
print("Mean Absolute Error :", round(mean_absolute_error(y_test, y_pred), 2))

# Save model
joblib.dump(model, "sales_prediction_model.pkl")

print("\nModel saved as sales_prediction_model.pkl")