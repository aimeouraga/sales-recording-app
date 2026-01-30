import streamlit as st
from pathlib import Path

# App configuration
st.set_page_config(
    page_title="Sales Recording App",
    page_icon = "📊",
    layout="centered"
    )

# Sidebar
with st.sidebar:
    st.title("📊 Sales App")
    st.write("Simple sales recording system.")
    st.markdown("---")
    st.write("Navigate using the menu above.")


# Main page content
st.title("🚀 The best app for your business")
st.write(
    """
    This **Sales Recording Application** allows merchants to easily:
    - Record daily sales
    - Automatically calculate totals
    - View sales history
    - Learn about the application creator

    👉 Use the **menu on the left** to get started.
    """
)