import streamlit as st
import pandas as pd
import os

FILE_PATH = os.path.join("data", "sales.csv")

st.title("📈 Sales Statistics")

if not os.path.exists(FILE_PATH):
    st.warning("No sales data found. Please add sales records first.")
    st.stop()

df = pd.read_csv(FILE_PATH)

if df.empty:
    st.info("No sales recorded yet.")
    st.stop()

# Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

st.markdown("------------")

# Metrics
st.subheader("📊 Key Metrics")
col1, col2, col3 = st.columns(3)

col1.metric("Total Sales Amount", f"{df['total_price'].sum():,.2f}")
col2.metric("Number of Sales", len(df))
col3.metric("Products Sold", df['product_name'].nunique())

st.markdown("---")

# Daily Sales
st.subheader("📅 Daily Revenue")

daily_sales = (
    df.groupby(df['date'].dt.date)['total_price']
    .sum()
    .reset_index()
    .rename(columns={'date': 'Date', 'total_price': 'Total Revenue'})
)

st.line_chart(daily_sales.set_index('Date'))

st.markdown("---")  

# Top Products
st.subheader("🏆 Top Selling Products")
top_products = (
    df.groupby('product_name')['total_price']
    .sum()
    .reset_index()
    .rename(columns={'product_name': 'Product', 'total_price': 'Total Sales'})
    .sort_values(by='Total Sales', ascending=False)
    .head(10)
)

st.bar_chart(top_products.set_index('Product'))

st.markdown("---")

# Display full sales data
st.subheader("📊 Quantity Sold per Product")

quantity_sold = (
    df.groupby('product_name')['quantity']
    .sum()
    .reset_index()
    .rename(columns={'product_name': 'Product', 'quantity': 'Total Quantity Sold'})
    .sort_values(by='Total Quantity Sold', ascending=False)
)

st.bar_chart(quantity_sold.set_index('Product'))

st.markdown("---")

st.caption("📌 These statistics help you analyse performance and trends.")