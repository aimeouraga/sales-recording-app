import streamlit as st
from pathlib import Path

# App configuration
st.set_page_config(
    page_title="Sales Recording App",
    page_icon = "📊",
    layout="centered"
    )

# ---- GLOBAL STYLE ----
st.markdown(
    """
    <style>
    .stApp {
        background-color: white;
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
        color: white;
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

# Force sidebar background to white
st.markdown(
    """
    <style>
        background-color: #D4AF37;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
        [data-testid="stSidebar"] * {
            color: white !important;
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
    #st.write("Navigate using the menu above.")


# Main page content
st.title("🚀 The best app for your business")
st.image("assets/logo1.png", width=650)
st.write(
    """
    👈 Use the **menu on the left** to get started.
    """
)