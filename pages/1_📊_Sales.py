import streamlit as st
import pandas as pd
import os
from datetime import datetime


# File path #D4AF37
DATA_DIR = "data"
FILE_PATH = os.path.join(DATA_DIR, "sales.csv")


# ---- GLOBAL STYLE ----
st.markdown(
    """
    <style>
    .stApp {
        #background-color: white;
        color: #1f2937;
    }

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

# Sidebar content
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>📊 Sales App</h2>", unsafe_allow_html=True)
    #st.write("Simple sales recording system.")
    st.write(
    """
    This **Sales Recording Application** allows merchants to easily:
    - Record daily sales
    - Automatically calculate totals
    - View sales history
    - Visualize performance with metrics
    - Track business growth
    - Learn about the application creator
    """
)
    st.markdown("---")

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

col1, col2 = st.columns(2)
if not df.empty:
    col1.metric("Total Sales Amount", f"{df['total_price'].sum():,.2f}")
    col2.metric("Number of Sales", len(df))
else:
    st.info("No sales recorded yet")


# ---- SALES TABLE DISPLAY CONTROL ----

# Default selection
if "sales_view" not in st.session_state:
    st.session_state.sales_view = "First 10"

# Title + dropdown layout
col1, col2 = st.columns([4, 2])

with col1:
    st.subheader("🧾 Sales History")

with col2:
    st.session_state.sales_view = st.selectbox(
        "View",
        options=["First 10", "Last 10", "All"],
        index=0,  
        label_visibility="collapsed"
    )

# ---- DATA SELECTION ----
if st.session_state.sales_view == "First 10":
    display_df = df.head(10)

elif st.session_state.sales_view == "Last 10":
    display_df = df.tail(10)

else:
    display_df = df

# ---- DISPLAY TABLE ----
st.markdown("---")
st.write("All amounts are expressed in CFA francs.")
st.dataframe(display_df, use_container_width=True)
