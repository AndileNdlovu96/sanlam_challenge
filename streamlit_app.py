import streamlit as st
import pandas as pd

# Load cleaned data
@st.cache_data
def load_data():
    return pd.read_parquet("output/sanctions_cleaned.parquet")

df = load_data()

st.title("🕵️ UN Sanctions List Explorer")

# Sidebar filters
st.sidebar.header("🔎 Filter Options")

# Filter: Full Name search
name_filter = st.sidebar.text_input("Search by Full Name").strip().lower()

# Filter: Nationality dropdown
nationalities = df["Nationality"].dropna().unique().tolist()
nationalities.sort()
selected_nationality = st.sidebar.selectbox("Filter by Nationality", ["All"] + nationalities)

# Filter: Alias contains
alias_filter = st.sidebar.text_input("Search by Alias").strip().lower()

# Apply filters
filtered_df = df.copy()

if name_filter:
    filtered_df = filtered_df[filtered_df["FullName"].str.lower().str.contains(name_filter)]

if selected_nationality != "All":
    filtered_df = filtered_df[filtered_df["Nationality"] == selected_nationality]

if alias_filter and "IndividualAlias" in filtered_df.columns:
    filtered_df = filtered_df[filtered_df["IndividualAlias"].str.lower().str.contains(alias_filter)]

# Show results
st.markdown(f"### Showing {len(filtered_df)} of {len(df)} records")
st.dataframe(filtered_df, use_container_width=True)
