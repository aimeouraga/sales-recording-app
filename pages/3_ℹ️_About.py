import streamlit as st

# ---- GLOBAL STYLE ----
st.markdown(
    """
    <style>
    .stApp {
        #background-color: white;
        #color: #1f2937;
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

with st.sidebar:
    st.markdown("---", unsafe_allow_html=True)

st.title("ℹ️ About This Application")

st.markdown(
    """
    ### 📊 Sales Recording Application

    **Developed by:**  
    **David OURAGA**  
    **Role:** Python Developer, DevOps Engineer  

    ---

    ### 🎯 Purpose
    This application was designed to help small merchants:
    - Record daily sales
    - Automatically calculate totals
    - Maintain a simple sales history without complex systems

    ---

    ### 🛠 Technologies Used
    - Python
    - Streamlit
    - Pandas
    - CSV file storage

    ---

    ### 📌 Notes
    This application is simple, lightweight, and does not require
    an internet connection or database server.

    © 2026 — All rights reserved
    """
)
