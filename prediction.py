import joblib
import pandas as pd

# Load the trained model
model = joblib.load("sales_prediction_model.pkl")

print("=" * 50)
print("AI-Powered Business Intelligence")
print("=" * 50)

# Sample data for prediction
sample = pd.DataFrame({
    "Quantity": [3],
    "Discount": [0.10],
    "Profit": [120]
})

# Predict Sales
prediction = model.predict(sample)

print("\nPredicted Sales")
print("---------------------------")
print(f"Estimated Sales: ₹{prediction[0]:.2f}")