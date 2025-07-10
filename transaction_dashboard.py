import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide")
st.title("📊 PhonePe Business Case Studies Dashboard")

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv("phonepe csv data.csv")

df = load_data()

# Sidebar selection
case_study = st.sidebar.selectbox(
    "Select Business Case Study",
    [
        "1️⃣ Decoding Transaction Dynamics",
        "2️⃣ Device Dominance & User Engagement",
        "3️⃣ Insurance Penetration & Growth",
        "4️⃣ Transaction Analysis for Market Expansion",
        "5️⃣ User Engagement & Growth Strategy"
    ]
)

# --- CASE STUDY 1 ---
if case_study.startswith("1"):
    st.header("1️⃣ Decoding Transaction Dynamics")
    st.write("Analyzing state-wise, quarter-wise transaction trends and user growth.")
    grouped = df.groupby(["state", "year", "quarter"]).agg({
        "total_transaction_amount": "sum",
        "total_users": "sum"
    }).reset_index()

    st.subheader("Total Transaction Amount by Year and State")
    fig1, ax1 = plt.subplots(figsize=(12, 6))
    sns.barplot(data=grouped, x="year", y="total_transaction_amount", hue="state", ax=ax1)
    st.pyplot(fig1)

    st.subheader("Total Users by Year")
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=grouped, x="year", y="total_users", hue="state", marker="o", ax=ax2)
    st.pyplot(fig2)

# --- CASE STUDY 2 ---
elif case_study.startswith("2"):
    st.header("2️⃣ Device Dominance and User Engagement Analysis")
    st.write("Examining which device brands dominate in user registrations.")
    brand_group = df.groupby("brand").agg({
        "total_users": "sum"
    }).reset_index().sort_values(by="total_users", ascending=False)

    st.subheader("Top Device Brands by Total Users")
    fig3, ax3 = plt.subplots()
    sns.barplot(data=brand_group, y="brand", x="total_users", palette="coolwarm", ax=ax3)
    st.pyplot(fig3)

# --- CASE STUDY 3 ---
elif case_study.startswith("3"):
    st.header("3️⃣ Insurance Penetration and Growth Potential")
    st.write("Analyzing how PhonePe can expand its insurance adoption.")
    st.warning("Note: This dataset may not include insurance-specific data directly. Placeholder analysis using users & brands.")

    fig4, ax4 = plt.subplots(figsize=(10, 5))
    insurance_proxy = df[df['brand'].str.lower().str.contains("others")]  # assuming 'others' = less popular devices = insurance target
    sns.barplot(data=insurance_proxy, x="state", y="total_users", hue="year", ax=ax4)
    plt.xticks(rotation=90)
    st.pyplot(fig4)

# --- CASE STUDY 4 ---
elif case_study.startswith("4"):
    st.header("4️⃣ Transaction Analysis for Market Expansion")
    st.write("Identifying top states with high transaction volume.")
    top_states = df.groupby("state")["total_transaction_amount"].sum().sort_values(ascending=False).head(10)

    st.subheader("Top 10 States by Transaction Amount")
    fig5, ax5 = plt.subplots()
    sns.barplot(x=top_states.values, y=top_states.index, palette="viridis", ax=ax5)
    st.pyplot(fig5)

# --- CASE STUDY 5 ---
elif case_study.startswith("5"):
    st.header("5️⃣ User Engagement and Growth Strategy")
    st.write("Analyzing growth of user registrations over time across states.")
    user_trend = df.groupby(["year", "state"])["total_users"].sum().reset_index()

    st.subheader("User Growth Trend Across States")
    fig6, ax6 = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=user_trend, x="year", y="total_users", hue="state", ax=ax6)
    st.pyplot(fig6)

# Footer
st.markdown("---")
st.markdown("✅ Created by Charan | Powered by Streamlit")
