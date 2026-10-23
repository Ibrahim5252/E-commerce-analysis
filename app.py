import streamlit as st
from src.cleaning import load_and_clean_data

df = load_and_clean_data(
    "data/Superstore_sales_dataset.csv"
)

st.title("E-commerce Analysis Dashboard")

# ---------------- SIDEBAR ----------------
st.sidebar.header("Filters")

region = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

category = st.sidebar.multiselect(
    "Select Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

# Apply filters
filtered_df = df[
    (df["Region"].isin(region)) &
    (df["Category"].isin(category))
]

# ---------------- KPI ----------------
col1, col2, col3 = st.columns(3) #! Creates 3 side-by-side columns for layout

col1.metric("Total Sales", int(filtered_df["Sales"].sum())) #! .metric() renders a styled KPI card with a label and value
col2.metric("Total Profit", int(filtered_df["Profit"].sum()))
col3.metric("Avg Profit Margin", round(filtered_df["Profit Margin"].mean(), 2))

# ---------------- CHARTS ----------------
st.subheader("Sales Over Time")
sales_trend = filtered_df.groupby("Order Date")["Sales"].sum().sort_index()
st.line_chart(sales_trend)

st.subheader("Profit by Category")
profit_cat = filtered_df.groupby("Category")["Profit"].sum().sort_values()
st.bar_chart(profit_cat)

# ---------------- LOSS ANALYSIS ----------------
st.subheader("Loss Making Products")
loss_df = filtered_df[filtered_df["Profit"] < 0]

st.dataframe(loss_df[["Product Name", "Sales", "Profit"]])