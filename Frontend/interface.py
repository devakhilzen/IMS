import streamlit as st
import os
import requests
import pandas as pd
from PIL import Image

BASE_URL= os.getenv("BASE_URL")

st.set_page_config(page_title="Inventory Management System", layout="wide")

def fetch_data(endpoint):
    try:
        response = requests.get(f"{BASE_URL}/{endpoint}")
        response.raise_for_status()
        data = response.json()
        
        # Debugging: Print the raw response to see if data is being returned
        st.write(data)  # This will show the raw data in Streamlit for debugging
        
        return data
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return None



# Home Dashboard
def home_dashboard():
    st.title("Welcome to the Inventory Management System")
    st.header("Dashboard Overview")

    # Add project-related image
    image = Image.open("ims.png")
    new_image = image.resize((800, 800))
    st.image(new_image)

    # Fetch data
    total_items_data = fetch_data("items/count")
    total_transactions_data = fetch_data("transactions/count")

    # Metrics
    total_items = total_items_data.get("total_items", 0) if total_items_data else 0
    total_transactions = total_transactions_data.get("total_transactions", 0) if total_transactions_data else 0

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Items", total_items)
    with col2:
        st.metric("Total Transactions", total_transactions)

    # Option to display all items
    st.header("All Items")
    items = fetch_data("items/")
    if items:
        items_df = pd.DataFrame(items)
        st.dataframe(items_df)
    else:
        st.warning("No items found!")

# Inventory Management
def inventory_management():
    st.title("Inventory Management")

    # Add New Item
    st.header("Add New Item")
    with st.form("add_item_form"):
        name = st.text_input("Item Name")
        description = st.text_input("Description")
        quantity = st.number_input("Quantity", min_value=1)
        price = st.number_input("Price", min_value=0.0)
        submitted = st.form_submit_button("Add Item")
        if submitted:
            data = {
                "name": name,
                "description": description,
                "quantity": quantity,
                "price": price,
            }
            response = requests.post(f"{BASE_URL}/items/", json=data)
            if response and response.status_code == 200:
                st.success("Item added successfully")
            else:
                st.error("Failed to add item")

     # Fetch data
    items = fetch_data("items/")

    # Display Items Table
    if items:
        st.header("Current Inventory")
        items_df = pd.DataFrame(items)
        st.dataframe(items_df)
    else:
        st.warning("No items found!") # Fetch dat


# Transaction Management
def transaction_management():
    st.title("Transaction Management")



    # Add New Transaction
    st.header("Add New Transaction")
    with st.form("add_transaction_form"):
        transaction_id = st.text_input("Transaction ID")
        item_name = st.text_input("Item Name")
        user_id = st.number_input("User ID", min_value=1)
        quantity = st.number_input("Quantity", min_value=1)
        transaction_type = st.selectbox("Transaction Type", ["Purchase", "Sale"])
        date = st.date_input("Date")
        submitted = st.form_submit_button("Add Transaction")
        if submitted:
            data = {
                "transaction_id": transaction_id,
                "item_name": item_name,
                "user_id": user_id,
                "quantity": quantity,
                "transaction_type": transaction_type,
                "date": str(date),
            }
            response = requests.post(f"{BASE_URL}/transactions/", json=data)
            if response and response.status_code == 200:
                st.success("Transaction added successfully")
            else:
                st.error("Failed to add transaction")

        # Fetch data
    transactions = fetch_data("transactions/")

    # Display Transactions Table
    if transactions:
        st.header("Recent Transactions")
        transactions_df = pd.DataFrame(transactions)
        st.dataframe(transactions_df)
    else:
        st.warning("No transactions found!")

# Sidebar Navigation
st.sidebar.title("Navigation")
pages = {
    "Home Dashboard": home_dashboard,
    "Inventory Management": inventory_management,
    "Transaction Management": transaction_management,
}
selected_page = st.sidebar.radio("Go to", list(pages.keys()))
pages[selected_page]()