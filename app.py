import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
data = pd.read_csv("data/superstore.csv")

# Dashboard Title
st.set_page_config(page_title="AI-Powered Business Intelligence", layout="wide")

st.title("📊 AI-Powered Business Intelligence Dashboard")
st.write("Analyze sales performance and business insights.")

# ==========================
# Key Performance Indicators
# ==========================
total_sales = data["Sales"].sum()
total_profit = data["Profit"].sum()
total_orders = data["Order ID"].nunique()

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"₹{total_sales:,.2f}")
col2.metric("Total Profit", f"₹{total_profit:,.2f}")
col3.metric("Total Orders", total_orders)

# ==========================
# Sales by Region
# ==========================
st.subheader("Sales by Region")

region_sales = data.groupby("Region")["Sales"].sum()

fig1, ax1 = plt.subplots(figsize=(6,4))
region_sales.plot(kind="bar", ax=ax1)
ax1.set_xlabel("Region")
ax1.set_ylabel("Sales")
st.pyplot(fig1)

# ==========================
# Sales by Category
# ==========================
st.subheader("Sales by Category")

category_sales = data.groupby("Category")["Sales"].sum()

fig2, ax2 = plt.subplots(figsize=(6,4))
category_sales.plot(kind="bar", ax=ax2)
ax2.set_xlabel("Category")
ax2.set_ylabel("Sales")
st.pyplot(fig2)

# ==========================
# Top 10 Customers
# ==========================
st.subheader("Top 10 Customers")

top_customers = (
    data.groupby("Customer Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.dataframe(top_customers)

st.success("Dashboard Loaded Successfully!")