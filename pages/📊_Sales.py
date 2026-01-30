import streamlit as st
import pandas as pd
import os
from datetime import datetime

# File path
DATA_DIR = "data"
FILE_PATH = os.path.join(DATA_DIR, "sales.csv")

# Ensure data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# Load or create CSV
if os.path.exists(FILE_PATH):
    df = pd.read_csv(FILE_PATH)
else:
    df = pd.DataFrame(columns=[
        "date",
        "product_name",
        "quantity",
        "unit_price",
        "total_price"
    ])
    df.to_csv(FILE_PATH, index=False)

st.title("📊 Record a Sale")

# Sales form
with st.form("sales_form"):
    product_name = st.text_input("Product Name")
    quantity = st.number_input("Quantity", min_value=1, step=1)
    unit_price = st.number_input("Unit Price", min_value=0.0, step=0.1)
    submit = st.form_submit_button("Add Sale")

# Handle form submission
if submit:
    if product_name.strip() == "":
        st.error("Product name cannot be empty")
    else:
        total_price = quantity * unit_price

        new_sale = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "product_name": product_name,
            "quantity": quantity,
            "unit_price": unit_price,
            "total_price": total_price
        }

        df = pd.concat([df, pd.DataFrame([new_sale])], ignore_index=True)
        df.to_csv(FILE_PATH, index=False)

        st.success("Sale recorded successfully ✅")

# Display metrics
st.markdown("---")
st.subheader("📈 Sales Summary")

if not df.empty:
    st.metric("Total Sales Amount", f"{df['total_price'].sum():,.2f}")
    st.metric("Number of Sales", len(df))
else:
    st.info("No sales recorded yet")

# Display sales table
st.markdown("---")
st.subheader("🧾 Sales History")
st.dataframe(df, use_container_width=True)
