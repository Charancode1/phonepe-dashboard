import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="PhonePe Business Dashboard", layout="wide")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("phonepe csv data.csv")
    return df

df = load_data()

# Title
st.title("📱 PhonePe Business Insights Dashboard")

# Sidebar Filters
st.sidebar.header("Filter Options")
states = st.sidebar.multiselect("Select State(s)", options=df["state"].unique(), default=df["state"].unique())
years = st.sidebar.multiselect("Select Year(s)", options=sorted(df["year"].unique()), default=df["year"].unique())
quarters = st.sidebar.multiselect("Select Quarter(s)", options=sorted(df["quarter"].unique()), default=df["quarter"].unique())

# Filtered Data
filtered_df = df[
    (df["state"].isin(states)) &
    (df["year"].isin(years)) &
    (df["quarter"].isin(quarters))
]

# Display Summary
st.subheader("📊 Overview")
col1, col2 = st.columns(2)
col1.metric("Total Users", f"{filtered_df['total_users'].sum():,}")
col2.metric("Total Transaction Amount", f"₹{filtered_df['total_transaction_amount'].sum():,.2f}")

# Charts
st.subheader("📈 Transactions by State")
fig1, ax1 = plt.subplots(figsize=(12, 5))
sns.barplot(data=filtered_df.groupby("state").sum().reset_index().sort_values(by="total_transaction_amount", ascending=False),
            x="total_transaction_amount", y="state", palette="coolwarm", ax=ax1)
ax1.set_xlabel("Total Transaction Amount")
ax1.set_ylabel("State")
st.pyplot(fig1)

st.subheader("📱 Device Brand Usage")
fig2, ax2 = plt.subplots(figsize=(10, 5))
top_brands = filtered_df.groupby("brand").sum().sort_values(by="total_users", ascending=False).reset_index()
sns.barplot(data=top_brands, x="brand", y="total_users", palette="viridis", ax=ax2)
ax2.set_ylabel("Total Users")
ax2.set_xlabel("Device Brand")
st.pyplot(fig2)

st.markdown("ℹ️ Use filters in the sidebar to explore different timeframes and states.")
