# -*- coding: utf-8 -*-
"""dashboard_streamlit.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/suhaodatascichem/dashboard-streamlit/blob/main/dashboard_streamlit.ipynb
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load your dataset
# Replace 'your_data.csv' with your actual data file
url = 'https://github.com/suhaodatascichem/dashboard-streamlit/raw/refs/heads/main/Soybean%20meal.xlsx'
df = pd.read_excel(url, engine="openpyxl")

df.columns

# Sidebar options
st.sidebar.header("Filters")

# Customer filter
customers = df["Customer"].unique()
selected_customer = st.sidebar.multiselect("Select Customer(s)", customers, default=customers)

# Material Type filter
material_types = df["Material"].unique()
selected_material = st.sidebar.multiselect("Select Material Type(s)", material_types, default=material_types)

# Filter the dataframe
filtered_df = df[df["Customer"].isin(selected_customer) & df["Material"].isin(selected_material)]

# ---- Display Data ----
st.write("### Filtered Data")

# Display count of rows after filtering
st.write(f"🔍 **Total Records After Filtering:** {filtered_df.shape[0]}")

st.dataframe(filtered_df)

# create Visualization
chart_type = st.sidebar.selectbox("Select Chart Type", ["Scatter Plot", "Bar Chart"])

# Column selection
numeric_columns = df.select_dtypes(include=['number']).columns.tolist()

if len(numeric_columns) < 2:
    st.error("Dataset must contain at least two numeric columns for visualization.")
else:
    x_axis = st.sidebar.selectbox("Select X-Axis", numeric_columns)
    y_axis = st.sidebar.selectbox("Select Y-Axis", numeric_columns)

    # Generate chart
    st.title("📊 Data Visualization Dashboard")

    if chart_type == "Scatter Plot":
        fig = px.scatter(df, x=x_axis, y=y_axis, title=f"Scatter Plot: {x_axis} vs {y_axis}")
        st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "Bar Chart":
        fig = px.bar(df, x=x_axis, y=y_axis, title=f"Bar Chart: {x_axis} vs {y_axis}")
        st.plotly_chart(fig, use_container_width=True)

    # Show dataset preview
    with st.expander("🔍 View Dataset"):
        st.write(df.head())

