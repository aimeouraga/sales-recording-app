import streamlit as st
import pandas as pd
import os

FILE_PATH = os.path.join("data", "sales.csv")

# ---- GLOBAL STYLE ----
st.markdown(
    """
    <style>
    h1, h2, h3, h4, h5 {
        color: #111827;
    }

    p, label, div {
        color: #D4AF37;
    }

    .stButton>button {
        background-color: #2563eb;
        color: white !important;
        border-radius: 6px;
    }

    .stMetric {
        background-color: #f9fafb;
        padding: 10px;
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    st.write("Here are some plots that summarize your sales data.")

    st.write("📌 These statistics help you analyse performance and trends.")
    st.markdown("---", unsafe_allow_html=True)

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
st.subheader("📊 Sales Distribution by Product")

quantity_sold = (
    df.groupby('product_name')['quantity']
    .sum()
    .reset_index()
    .rename(columns={'product_name': 'Product', 'quantity': 'Total Quantity Sold'})
    .sort_values(by='Total Quantity Sold', ascending=False)
)

#st.bar_chart(quantity_sold.set_index('Product'))
import plotly.express as px

fig = px.pie(
    quantity_sold,
    names="Product",
    values="Total Quantity Sold",
    #title="Sales Distribution by Product",
    hole=0.3  # donut style (optional, looks professional)
)

st.plotly_chart(fig, use_container_width=True)
st.markdown("---")