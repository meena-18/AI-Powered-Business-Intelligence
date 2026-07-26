import pandas as pd

# Load dataset
data = pd.read_csv("superstore.csv")

print("=" * 50)
print("AI Powered Business Intelligence")
print("=" * 50)

# Total Sales
total_sales = data["Sales"].sum()
print("\nTotal Sales : ₹", round(total_sales, 2))

# Total Profit
total_profit = data["Profit"].sum()
print("Total Profit : ₹", round(total_profit, 2))

# Total Orders
total_orders = data["Order ID"].nunique()
print("Total Orders :", total_orders)

# Sales by Region
print("\nSales by Region")
print(data.groupby("Region")["Sales"].sum())

# Sales by Category
print("\nSales by Category")
print(data.groupby("Category")["Sales"].sum())

# Top 10 Customers
print("\nTop 10 Customers")
print(data.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False).head(10))