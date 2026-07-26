import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("superstore.csv")

# ----------------------------
# Sales by Region
# ----------------------------
region_sales = data.groupby("Region")["Sales"].sum()

plt.figure(figsize=(8,5))
region_sales.plot(kind="bar", color="skyblue")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("sales_by_region.png")
plt.show()

# ----------------------------
# Sales by Category
# ----------------------------
category_sales = data.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8,5))
category_sales.plot(kind="bar", color="lightgreen")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("sales_by_category.png")
plt.show()

# ----------------------------
# Profit by Category
# ----------------------------
category_profit = data.groupby("Category")["Profit"].sum()

plt.figure(figsize=(8,5))
category_profit.plot(kind="bar", color="orange")
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Total Profit")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("profit_by_category.png")
plt.show()

# ----------------------------
# Top 10 Customers by Sales
# ----------------------------
top_customers = (
    data.groupby("Customer Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,6))
top_customers.plot(kind="bar", color="purple")
plt.title("Top 10 Customers by Sales")
plt.xlabel("Customer")
plt.ylabel("Sales")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("top_customers.png")
plt.show()

print("Visualization completed successfully!")